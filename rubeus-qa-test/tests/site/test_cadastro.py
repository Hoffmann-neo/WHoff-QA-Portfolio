from pages.site.site import Newsletter

def test_cadastro(page):
    """
    Cenário: Inscrição com dados válidos.

    Regra de negócio:
    A Cadastro deveria ser concluída com sucesso após o preenchimento dos campos obrigatórios.

    Comportamento atual identificado:
    O sistema retorna a mensagem:
    "É necessário informar a base legal".

    Observação:
    Este teste valida o comportamento atual identificado como defeito.
    Após a correção do bug, o teste deverá ser atualizado
    para validar o fluxo de sucesso da inscrição.

    TESTE:

    Passos executados:
    - Acessar página de Certificação
    - Preencher:
        nome='Teste Fulano Beltrano'
        telefone='51919191919'
        email='Fulano@gmail.com'
    - Clicar em "Avançar"
    - Validar exibição da mensagem de erro
    """
    cadastro = Newsletter(page)
    cadastro.acessar_site()
    cadastro.fazer_cadastro(
        nome='Teste Fulano Beltrano',
        telefone='51919191919',
        email='Fulano@gmail.com'
    )
    cadastro.validar_grid(
        grid_locator="#toast-container",
        esperado=['É necessário informar a base legal'])
