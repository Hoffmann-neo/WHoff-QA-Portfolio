from page_objects.objetosgerais import ObjetosGerais

class TextBox(ObjetosGerais):

    def acessar_text_box(self):
        self.page.goto(
                'https://demoqa.com/text-box')
        self.page.wait_for_load_state()

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_nome = page.locator('#userName')
        self.campo_email = page.locator('#userEmail')
        self.campo_endereco_atual = page.locator('#currentAddress')
        self.campo_endereco_permanente = page.locator('#permanentAddress')

    def preencher_text_box(self,
                           nome='',
                           email='',
                           endereco_atual='',
                           endereco_permanente=''):
        if nome:
            self.campo_nome.fill(nome)
            self.campo_nome.press('Tab')
        if email:
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        if endereco_atual:
            self.campo_endereco_atual.fill(endereco_atual)
            self.campo_endereco_atual.press('Tab')
        if endereco_permanente:
            self.campo_endereco_permanente.fill(endereco_permanente)
            self.campo_endereco_permanente.press('Tab')
