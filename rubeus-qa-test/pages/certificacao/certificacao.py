from pages.objetosgerais import ObjetosGerais

class Certificacao(ObjetosGerais):

    def acessar_certificacao(self):
        self.page.goto(
            'https://qualidade.apprbs.com.br/certificacao')
        self.page.wait_for_load_state()

class Inscricao(Certificacao):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.botao_avancar = page.locator('#i1nsld')


    def fazer_inscricao(self,
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

