from playwright.sync_api import expect
import re


class ObjetosGerais:

    def __init__(self, page):
        self.page = page
        self.campo_nome = page.locator('[name="pessoa.nome"]')
        self.campo_telefone = page.get_by_placeholder("(11) 96123-")
        self.campo_email = page.locator('[name="pessoa.emailPrincipal"]')


    def validar_grid(
        self,
        grid_locator: str,
        esperado,
        timeout: int = 30000,
        normalizar: bool = True,
        parcial: bool = True
    ):
        """
        Valida textos dentro de qualquer container da página.

        Serve para:
        - tabelas
        - grids
        - listas
        - resumos
        - outputs
        - carrinho
        - formulários

        Parâmetro "esperado" pode ser:

        - str  → "Texto único"
        - list → ["Texto A", "Texto B"]
        - dict → {"campo": "valor"}  (usa só os valores)
        """

        # =========================================
        # FUNÇÃO PARA LIMPAR / PADRONIZAR TEXTO
        # =========================================
        def limpar(texto: str) -> str:
            """
            Remove diferenças de maiúscula, espaços e símbolos.
            Ajuda a evitar erro por detalhe bobo.
            """

            if not normalizar:
                return texto.strip()

            # Tudo minúsculo
            texto = texto.lower()

            # Remove espaços repetidos
            texto = re.sub(r"\s+", " ", texto)

            # Remove símbolos estranhos
            texto = re.sub(r"[^\w\sáéíóúâêôãõç]", "", texto)

            return texto.strip()

        # =========================================
        # LOCALIZA O CONTAINER (GRID / DIV / BLOCO)
        # =========================================
        container = self.page.locator(grid_locator)

        # Espera aparecer na tela
        expect(container).to_be_visible(timeout=timeout)

        # Pega TODO texto de dentro (mais seguro)
        texto_bruto = container.text_content(timeout=timeout)

        if not texto_bruto:
            raise AssertionError("❌ Nenhum texto encontrado no container")

        # =========================================
        # QUEBRA TEXTO EM LINHAS
        # =========================================
        linhas = [
            limpar(linha)
            for linha in texto_bruto.split("\n")
            if linha.strip()
        ]

        # Texto completo em uma linha só
        texto_completo = " ".join(linhas)

        # =========================================
        # DEBUG → MOSTRA NO TERMINAL
        # =========================================
        print("\n📌 Textos encontrados na tela:")

        for t in linhas:
            print("-", t)

        # =========================================
        # ORGANIZA O ESPERADO
        # =========================================
        esperados = []

        # Se for string
        if isinstance(esperado, str):
            esperados = [esperado]

        # Se for lista
        elif isinstance(esperado, list):
            esperados = esperado

        # Se for dicionário → usa só valores
        elif isinstance(esperado, dict):
            esperados = list(esperado.values())

        else:
            raise TypeError("❌ esperado deve ser str, list ou dict")

        # Limpa todos
        esperados = [limpar(e) for e in esperados]

        # =========================================
        # VALIDAÇÃO
        # =========================================
        erros = []

        for valor in esperados:

            # Procura dentro do texto inteiro
            if parcial:
                encontrado = valor in texto_completo

            # Procura exatamente na lista
            else:
                encontrado = valor in linhas

            if not encontrado:
                erros.append(f"❌ Não encontrado: {valor}")

        # =========================================
        # RESULTADO FINAL
        # =========================================
        if erros:
            raise AssertionError(
                "\n".join(erros)
                + "\n\n📌 Texto da tela:\n"
                + texto_completo
            )

        print("\n✅ Validação concluída com sucesso")