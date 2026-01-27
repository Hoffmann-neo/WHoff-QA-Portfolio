from pages.swaglbs import SwagLabs


def test_login(page):
    login = SwagLabs(page)
    login.acessar_swag_labs()
    login.criar_login(
        username='standard_user',
        password='secret_sauce',
    )
    page.pause()
    meus_produtos = [
        "Sauce Labs Fleece Jacket",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt"
    ]
    compra = SwagLabs(page)
    compra.comprar_item(
        lista_itens=meus_produtos
    )
    page.pause()
