from pages.swaglbs import SwagLabs

def test_comprar(page):
    """
    - Acessar site: saucedemo
    - Efetuar login
        - username='standard_user',
        - password='secret_sauce'
    - Adicionar os produtos ao carrinho de compras
        "Sauce Labs Fleece Jacket",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt"
    - Etapas
        - Clicar no nome do produto
        - clicar botao add to cart
        - clicar em voltar
    - depois de adicionar todos produtos no carrinho
    - clicar no carrinho
    - validar grid
    - clicar em checkout
    - preencher informações
        - nome='Fulano',
        - sobrenome='de santas',
        - codigo_postal='92998789'
    - clicar botao continue
    - validar grid de valores
    - clicar em finish
    - validar expect
    - clicar em back home
    """
    login = SwagLabs(page)
    login.acessar_swag_labs()
    page.pause()
    login.criar_login(
        username='standard_user',
        password='secret_sauce',
    )
    meus_produtos = [
        "Sauce Labs Fleece Jacket",
        "Test.allTheThings() T-Shirt (Red)",
        "Sauce Labs Bolt T-Shirt"
    ]
    compra = SwagLabs(page)
    compra.comprar_item(
        lista_itens=meus_produtos
    )
    compra.conferir_carrinho_compras()

    compra.validar_grid(
        grid_locator='#cart_contents_container',
        esperado=['qtydescription1sauce labs fleece jacketits not every day that you come across a midweight quarterzip'
                  ' fleece jacket capable of handling everything from a relaxing day outdoors to a busy day at the '
                  'office4999remove1testallthethings tshirt redthis classic sauce labs tshirt is perfect to wear when '
                  'cozying up to your keyboard to automate a few tests supersoft and comfy ringspun combed '
                  'cotton1599remove1sauce labs bolt tshirtget your testing superhero on with the sauce labs bolt '
                  'tshirt from american apparel 100 ringspun combed cotton heather gray with red bolt1599removecontinue '
                  'shoppingcheckout']
    )

    compra.checkuot(
        nome='Fulano',
        sobrenome='de santas',
        codigo_postal='92998789'
    )

    compra.validar_grid(
        grid_locator='#checkout_summary_container .summary_info',
        esperado=['payment informationsaucecard 31337shipping informationfree pony express deliveryprice totalitem '
                  'total 8197tax 656total 8853cancelfinish']
    )
    compra.finalizar_carrinho_compras()