from pages.text_box import TextBox


def test_text_box(page):
    text_box = TextBox(page)
    text_box.acessar_text_box()
    text_box.preencher_text_box(
        nome='Teste de fulano',
        email='fulano@gmail.com',
        endereco_atual='Rua cecilia capital',
        endereco_permanente='Av goularte camara'
    )
    text_box.botao_submit.click()
    text_box.validar_grid(
        grid_locator="#output",
        esperado={'name': 'Teste de fulano', 'email': 'fulano@gmail.com', 'currentaddress': 'Rua cecilia capital',
                  'permananetaddress': 'Av goularte camara'}
    )
