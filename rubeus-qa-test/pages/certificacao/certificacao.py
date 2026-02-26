from pages.objetosgerais import ObjetosGerais


class Certificacao(ObjetosGerais):

    def acessar_certificacao(self):
        self.page.goto(
            'https://qualidade.apprbs.com.br/certificacao')
        self.page.wait_for_load_state()

    def acessar_text_box(self):
        self.botao_text_box.click()
        self.page.wait_for_load_state()

    def acessar_web_tables(self):
        self.botao_web_tables.click()
        self.page.wait_for_load_state()

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.botao_text_box = page.get_by_text("Text Box")
        self.botao_web_tables = page.get_by_text("Web Tables")


class Incricao(Certificacao):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_nome =  page.locator('[name="pessoa.nome"]')
        self.campo_telefone = page.get_by_placeholder("(11) 96123-")
        self.campo_email = page.locator('[name="pessoa.emailPrincipal"]')
        self.botao_avancar = page.locator('#i1nsld')

    def fazer_incricao(self,
                       nome='',
                       telefone='',
                       email='',
                           ):
        if nome:
            self.campo_nome.fill(nome)
            self.campo_nome.press('Tab')
        if telefone:
            self.campo_telefone.fill(telefone)
            self.campo_telefone.press('Tab')
        if email:
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        self.botao_avancar.click()
        self.page.wait_for_timeout(2000)



class WebTables(Certificacao):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_nome = page.locator('#firstName')
        self.campo_sobrenome = page.locator('#lastName')
        self.campo_email = page.locator('#userEmail')
        self.campo_idade = page.locator('#age')
        self.campo_salario = page.locator('#salary')
        self.campo_departamento = page.locator('#department')
        self.campo_buscar = page.locator('#searchBox')
        self.botao_editar = page.locator("#edit-record-4 > svg")
        self.botao_delete = page.locator("#delete-record-4 > svg")

    def preencher_web_tables(self,
                             nome='',
                             sobrenome='',
                             email='',
                             idade='',
                             salario='',
                             departamento=''):

        if nome:
            self.campo_nome.fill(nome)
        if sobrenome:
            self.campo_sobrenome.fill(sobrenome)
        if email:
            self.campo_email.fill(email)
        if idade:
            self.campo_idade.fill(idade)
        if salario:
            self.campo_salario.fill(salario)
        if departamento:
            self.campo_departamento.fill(departamento)

    def filtrar_web_tables(self,buscar=''):

        if buscar:
            self.campo_buscar.fill(buscar)
            self.campo_buscar.press('Tab')

