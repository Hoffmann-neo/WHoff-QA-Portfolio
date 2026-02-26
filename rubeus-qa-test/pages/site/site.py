from pages.objetosgerais import ObjetosGerais

class Site(ObjetosGerais):

    def acessar_site(self):
        self.page.goto(
            'https://qualidade.apprbs.com.br/site')
        self.page.wait_for_load_state()

class Newsletter(Site):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.botao_concluir = page.get_by_role("button", name="Concluir")

    def fazer_cadastro(self,
                       nome='',
                       email='',
                       telefone='',
                       ):
        if nome:
            self.campo_nome.fill(nome)
            self.campo_nome.press('Tab')
        if email:
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        if telefone:
            self.campo_telefone.fill(telefone)
        self.botao_concluir.click()
        self.page.wait_for_timeout(2000)

