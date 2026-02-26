from pages.objetosgerais import ObjetosGerais
from pages.certificacao.certificacao import Inscricao

def test_inscricao(page):
    """
    Cenário: Inscrição com dados válidos.

    Regra de negócio:
    A inscrição deveria ser concluída com sucesso após o preenchimento dos campos obrigatórios.

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
    inscricao = Inscricao(page)
    inscricao.acessar_certificacao()
    inscricao.fazer_inscricao(
        nome='Teste Fulano Beltrano',
        telefone='51919191919',
        email='Fulano@gmail.com'
    )
    inscricao.validar_grid(
        grid_locator="#toast-container",
        esperado=['É necessário informar a base legal'])


def test_inscricao_nao_deve_aceitar_telefone_com_letras(page):
    """
    Cenário: Tentativa de inscrição com telefone contendo letras.

    Regra de negócio:
    O campo telefone deve aceitar apenas caracteres numéricos.

    Comportamento atual identificado:
    O sistema permite inserção de letras no campo telefone.

    Observação:
    Este teste valida o comportamento atual identificado como defeito.

    TESTE

       Passos executados:
    - Acessar página de Certificação
    - Preencher:
        nome='Teste QA'
        telefone='5192899978ss'
        email='teste@email.com'
    - Clicar em "Avançar"
    - Validar exibição da mensagem de erro
    """

    inscricao = Inscricao(page)
    inscricao.acessar_certificacao()
    page.pause()
    inscricao.fazer_inscricao(
        nome='Teste QA',
        telefone='5192899978ss',
        email='teste@email.com'
    )