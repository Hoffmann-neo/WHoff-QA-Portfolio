from Python_Playwright.pages.nopcommerce import LoginRegistro, MyAccount

def test_registro(page):
    registro = LoginRegistro(page)
    registro.acessar_novo_registro()

    registro.adicionar_registro(
        genero= "male",
        nome='Teste',
        sobrenome='Beltrano',
        email='beltrano_qa@test.com',
        company='QA',
        senha='123456',
        confirme_senha='123456')

def test_adicionar_endereco(page):
    login = LoginRegistro(page)
    login.acessar_nop_commerce()
    login.login(
        email='beltrano_qa@test.com',
        senha='123456',
    )
    login.botao_minha_conta.click()
    page.pause()

    minha_conta = MyAccount(page)
    minha_conta.cadastrar_endereco(
        nome='test',
        sobrenome='beltrano',
        email='beltrano_qa@test.com',
        company='QA',
        pais='Brazil',
        estado='Rio Grande do Sul',
        cidade='Canoas',
        endereco_1='Rua cacique norte 111',
        endereco_2='Rua eduardo monteiro 123',
        codigo_postal='92340111',
        telefone='5191919191'
    )

    minha_conta.validar_grid(
        grid_locator=".page-body",
        esperado=['test beltrano'
                  'test beltranoe'
                  'mail beltrano_qatestcomphone '
                  'number 5191919191'
                  'fax numberqa'
                  'brazilrio grande do sulcanoasrua '
                  'cacique norte 111rua eduardo monteiro 12392340111]'
                  'edit deleteadd new']

    )