from playwright.sync_api import expect
import re


class ObjetosGerais:

    def __init__(self, page):
        self.page = page
        self.botao_submit = page.locator('#submit')
        self.botao_login = page.locator('#login-button')
        self.botao_add_to_cart = page.locator('#add-to-cart')
        self.botao_voltar = page.locator('#back-to-products')
        self.botao_carrinho_compras = page.locator('#shopping_cart_container')

    def validar_grid(
            self,
            grid_locator: str,
            esperado: dict,
            timeout: int = 30000,
            separador=":"
    ):
        """
        Valida qualquer output baseado em texto exibido na tela.

        Exemplo esperado:

        {
            "name": "Fulano",
            "email": "teste@email.com"
        }
        """

        def normalizar(texto: str) -> str:
            """
            Remove caracteres especiais, espaços e deixa minúsculo.
            """
            return re.sub(r"[^a-z0-9]", "", texto.lower())

        # Localiza container
        container = self.page.locator(grid_locator)

        expect(container).to_be_visible(timeout=timeout)

        # Busca qualquer texto dentro
        elementos = container.locator("*")

        expect(elementos.first).to_be_visible(timeout=timeout)

        dados_tela = {}

        total = elementos.count()

        for i in range(total):

            texto = elementos.nth(i).inner_text(timeout=timeout).strip()

            if not texto:
                continue

            # Remove espaços invisíveis
            texto = " ".join(texto.split())

            if separador not in texto:
                continue

            chave, valor = texto.split(separador, 1)

            chave = normalizar(chave)
            valor = valor.strip()

            if chave and valor:
                dados_tela[chave] = valor

        # Debug automático
        print("\n📌 Dados encontrados na tela:")
        for k, v in dados_tela.items():
            print(f"{k}: {v}")

        # Validação
        erros = []

        for campo, esperado_valor in esperado.items():

            campo_norm = normalizar(campo)

            tela_valor = dados_tela.get(campo_norm)

            if tela_valor is None:
                erros.append(
                    f"Campo '{campo}' não encontrado"
                )
                continue

            if tela_valor != esperado_valor:
                erros.append(
                    f"{campo} | Esperado: '{esperado_valor}' | Tela: '{tela_valor}'"
                )

        if erros:
            msg = "\n".join(erros)

            raise AssertionError(
                f"""
    ❌ ERROS NA VALIDAÇÃO

    {msg}

    📌 Tela:
    {dados_tela}
    """
            )

        print("\n✅ Grid validado com sucesso")
