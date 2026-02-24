*** Settings ***

#Declaramos a bicliotecas ou mapeamentos

Resource    ../resources/autexercise.robot
Resource    ../resources/base.resource
Library    Dialogs

*** Test Cases ***

Validar Novo Cadastro
    Open Browser ${URL}    ${BROWSER}


Validar Login com Erro
    Open Browser    ${URL}    ${BROWSER}
    Preencher Login    email@exemplo.com    123456
    Clicar No Botao Login
    Validar Mensagem de Erro



