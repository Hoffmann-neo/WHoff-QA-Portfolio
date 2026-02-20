from Python_Playwright.pages.objetosgerais import ObjetosGerais
from playwright.sync_api import expect

class NopCommerce(ObjetosGerais):

    def acessar_nop_commerce(self):
        self.page.goto(
            'https://demo.nopcommerce.com/')
        self.page.wait_for_load_state()

    def acessar_novo_registro(self):
        self.page.goto(
            'https://demo.nopcommerce.com/register?returnUrl=%2F'
        )
        self.page.wait_for_load_state()

class LoginRegistro(NopCommerce):

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.check_box_male = page.get_by_role("radio", name="Male", exact=True)
        self.check_box_female = page.get_by_role("radio", name="Female")
        self.campo_nome = page.locator("#FirstName")
        self.campo_sobre_nome = page.locator("#LastName")
        self.campo_email = page.locator("#Email")
        self.campo_company = page.locator("#Company")
        self.campo_senha = page.locator("#Password")
        self.campo_confirme_senha = page.locator("#ConfirmPassword")
        self.botao_registrar = page.locator("#register-button")
        self.botao_continuar = page.get_by_role("link", name="Continue")
        self.botao_minha_conta = page.locator(".ico-account")
        self.botao_login = page.locator(".ico-login")
        self.botao_logar = page.locator(".login-button")

    def adicionar_registro(self,
                          genero: str,
                          nome='',
                          sobrenome='',
                          email='',
                          company='',
                          senha='',
                          confirme_senha=''):


        if genero:
            selecionar={
                'male': self.check_box_male,
                'female': self.check_box_female
            }
            selecionar[genero.lower()].check()

        if nome:
            self.campo_nome.clear()
            self.campo_nome.fill(nome)
            self.campo_nome.press('Tab')
        if sobrenome:
            self.campo_sobre_nome.clear()
            self.campo_sobre_nome.fill(sobrenome)
            self.campo_sobre_nome.press('Tab')
        if email:
            self.campo_email.clear()
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        if company:
            self.campo_company.clear()
            self.campo_company.fill(company)
            self.campo_company.press('Tab')
        if senha:
            self.campo_senha.clear()
            self.campo_senha.fill(senha)
            self.campo_senha.press('Tab')
        if confirme_senha:
            self.campo_confirme_senha.clear()
            self.campo_confirme_senha.fill(confirme_senha)
            self.campo_confirme_senha.press('Tab')

        self.botao_registrar.click()
        self.page.wait_for_timeout(2000)

        expect(self.page.get_by_test("Your registration completed")).to_be_visible(timeout=2000)
        self.botao_continuar.click()

    def login(self, email, senha):

        self.botao_login.click()
        self.page.wait_for_timeout(1000)

        if email:
            self.campo_email.clear()
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        if senha:
            self.campo_senha.clear()
            self.campo_senha.fill(senha)
            self.campo_senha.press('Tab')

        self.botao_logar.click()
        self.page.wait_for_timeout(1000)


class MyAccount(NopCommerce):

    def __init__(self, page):
        super().__init__(page)
        self.botao_endereco = page.locator("#main").get_by_role("link", name="Addresses")
        self.botao_novo_endereco = page.locator(".add-address-button")
        self.campo_nome = page.locator("#Address_FirstName")
        self.campo_sobre_nome = page.locator("#Address_LastName")
        self.campo_email =  page.get_by_role("textbox", name="Email:")
        self.campo_company = page.locator("#Address_Company")
        self.combobox_pais = page.locator("#Address_CountryId")
        self.combobox_estado = page.locator("#Address_StateProvinceId")
        self.campo_cidade = page.locator("#Address_City")
        self.campo_endereco_1 = page.locator("#Address_Address1")
        self.campo_endereco_2 = page.locator("#Address_Address2")
        self.campo_codigo_postal = page.get_by_role("textbox", name="Zip / postal code:")
        self.campo_telefone = page.locator("#Address_PhoneNumber")
        self.botao_salvar = page.locator(".save-address-button")

    def cadastrar_endereco(self,
                           nome='',
                           sobrenome='',
                           email='',
                           company='',
                           pais='',
                           estado='',
                           cidade='',
                           endereco_1='',
                           endereco_2='',
                           codigo_postal='',
                           telefone=''
                        ):
        self.page.wait_for_timeout(1000)
        self.botao_endereco.click()
        self.page.wait_for_timeout(1000)
        self.botao_novo_endereco.click()
        self.page.wait_for_timeout(1000)

        if nome:
            self.campo_nome.clear()
            self.campo_nome.fill(nome)
            self.campo_nome.press('Tab')
        if sobrenome:
            self.campo_sobre_nome.clear()
            self.campo_sobre_nome.fill(sobrenome)
            self.campo_sobre_nome.press('Tab')
        if email:
            self.campo_email.clear()
            self.campo_email.fill(email)
            self.campo_email.press('Tab')
        if company:
            self.campo_company.clear()
            self.campo_company.fill(company)
            self.campo_company.press('Tab')
        if pais:
            self.combobox_pais.select_option(pais)
        if estado:
            self.combobox_estado.select_option(estado)
        if cidade:
            self.campo_cidade.clear()
            self.campo_cidade.fill(cidade)
            self.campo_cidade.press('Tab')
        if endereco_1:
            self.campo_endereco_1.clear()
            self.campo_endereco_1.fill(endereco_1)
            self.campo_endereco_1.press('Tab')
        if endereco_2:
            self.campo_endereco_2.clear()
            self.campo_endereco_2.fill(endereco_2)
            self.campo_endereco_2.press('Tab')
        if codigo_postal:
            self.campo_codigo_postal.clear()
            self.campo_codigo_postal.fill(codigo_postal)
            self.campo_codigo_postal.press('Tab')
        if telefone:
            self.campo_telefone.clear()
            self.campo_telefone.fill(telefone)

        self.botao_salvar.click()
        self.page.wait_for_timeout(2000)



class Produtos(NopCommerce):

    def __init__(self, page):
        super().__init__(page)
        self.botao_eletronicos = page.get_by_role("button", name="Electronics")
        self.botao_telefones = page.get_by_role("link", name="Cell phones")
        self.botao_iphone_16 = page.get_by_role("link", name="Apple iPhone 16 128GB").nth(3)
        self.botao_add_carrinho = page.locator("#add-to-cart-button-21")

    def produtos(self):





















