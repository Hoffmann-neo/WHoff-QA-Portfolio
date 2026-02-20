from Python_Playwright.pages.nopcommerce import LoginRegistro, MyAccount



def test_compra(page):
    login = LoginRegistro(page)
    login.acessar_nop_commerce()
    login.login(
        email='beltrano_qa@test.com',
        senha='123456',
    )
    page.pause()
