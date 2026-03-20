from pages.demoqa import WebTables


def test_crud_web_tables(page):
    """
        CADASTRO
    - Acessar site DemoQA
    - Clique em web Tables
    - Clicar em Add
    - Preencher:
        - nome='DemoQA',
        - sobrenome='testes',
        - email='demoqa@gmail.com',
        - idade='31',
        - salario='4500',
        - departamento='Administrador',
    - clicar botao submit
    - validar grid

        EDITAR
    - Clique no campo filtro
    - digite = DemoQA
    - clicar botao editar
    - alterar campos:
        - sobrenome='teste',
        - email='demoqa2@gmail.com',
        - idade='35',
        - salario='4700',
        - departamento='Administrador'
    - clicar botao submit
    - Limpar o campo filtro
    - validar grid

        EXCLUIR
    - Clique no campo filtro
    - digite = DemoQA
    - clicar botao excluir
    - clicar botao submit
    - Limpar o campo filtro
    - validar grid
    """
    #-------------------
    #   Cadastrar
    #-------------------
    webtables = WebTables(page)
    webtables.acessar_demoqa()
    webtables.acessar_web_tables()
    webtables.botao_add.click()
    webtables.preencher_web_tables(
        nome='DemoQA',
        sobrenome='testes',
        email='demoqa@gmail.com',
        idade='31',
        salario='4500',
        departamento='Administrador',
    )
    webtables.botao_submit.click()
    webtables.validar_grid(
        grid_locator=".web-tables-wrapper",
        esperado=['addfirst namelast nameageemailsalarydepartmentactioncierravega39cierraexamplecom10000insuranceal'
                  'dencantrell45aldenexamplecom12000compliancekierragentry29kierraexamplecom2000legaldemoqatestes31'
                  'demoqagmailcom4500administradorfirstpreviousnextlastpage 1 of 1show 10show 20show 30show 40show 50']
    )
    # -------------------
    #   Editar
    # -------------------
    webtables.filtrar_web_tables(
        buscar='DemoQA',
    )
    webtables.botao_editar.click()
    webtables.preencher_web_tables(
        sobrenome='teste',
        email='demoqa2@gmail.com',
        idade='35',
        salario='4700',
        departamento='Administrador',
    )
    webtables.botao_submit.click()
    webtables.campo_buscar.clear()
    page.wait_for_timeout(timeout=5000)
    webtables.validar_grid(
        grid_locator=".web-tables-wrapper",
        esperado=['addfirst namelast nameageemailsalarydepartmentactioncierravega39cierraexamplecom10000'
                  'insurancealdencantrell45aldenexamplecom12000compliancekierragentry29kierraexamplecom2000'
                  'legaldemoqateste35demoqa2gmailcom4700administradorfirstpreviousnextlastpage 1 of 1show 10show '
                  '20show 30show 40show 50']
    )
    # -------------------
    #   Excluir
    # -------------------
    webtables.filtrar_web_tables(
        buscar='DemoQA',
    )
    webtables.botao_delete.click()
    webtables.campo_buscar.clear()
    page.wait_for_timeout(timeout=5000)
    webtables.validar_grid(
        grid_locator=".web-tables-wrapper",
        esperado=['addfirst namelast nameageemailsalarydepartmentactioncierravega39cierraexamplecom10000'
                  'insurancealdencantrell45aldenexamplecom12000compliancekierragentry29kierraexamplecom2000'
                  'legalfirstpreviousnextlastpage 1 of 1show 10show 20show 30show 40show 50']
    )