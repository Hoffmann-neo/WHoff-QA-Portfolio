from page_objects.objetosgerais import ObjetosGerais
from playwright.sync_api import expect

class SwagLabs(ObjetosGerais):

    def acessar_swag_labs(self):
        self.page.goto(
                'https://www.saucedemo.com/')
        self.page.wait_for_load_state()

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.campo_username = page.locator('#user-name')
        self.campo_password = page.locator('#password')
        self.item_produto_name = page.locator(".inventory_item_name")

    def criar_login(self,
              username,
              password):
        if username:
            self.campo_username.fill(username)
            self.campo_password.press('Tab')

        if password:
            self.campo_password.fill(password)
            self.campo_password.press('Tab')

        self.botao_login.click()
        self.page.wait_for_load_state(timeout=5000)

    def comprar_item(self,
                     lista_itens):
        for nome in lista_itens:
            self.item_produto_name.filter(has_text=nome).click()
            self.botao_add_to_cart.click()
            expect(self.page.get_by_text('Remove')).to_be_visible(timeout=5000)
            self.botao_voltar.click()
            self.page.wait_for_timeout(5000)

    def conferir_carrinho_compras(self):
        self.botao_carrinho_compras.click()
        self.page.wait_for_load_state(timeout=5000)
