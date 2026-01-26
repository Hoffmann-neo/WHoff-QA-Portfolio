from playwright.sync_api import expect


class ObjetosGerais:

    def __init__(self, page):
        self.page = page
        self.botao_submit = page.locator('#submit')
        self.botao_login = page.locator('#login-button')
        self.botao_add_to_cart = page.locator('#add-to-cart')
        self.botao_voltar = page.locator('#back-to-products')
        self.botao_carrinho_compras = page.locator('#shopping_cart_container')

    def validar_valores(self,validar):
        expect(self.page.get_by_text(validar)).to_be_visible(timeout=5000)
