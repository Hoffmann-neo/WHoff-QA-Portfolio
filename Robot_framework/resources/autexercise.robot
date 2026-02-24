*** Settings ***

Resource    ../resources/base.resource

*** Variables ***
${URL}        https://automationexercise.com/login

# --- avisos ---
${AVISO_ERRO_LOGIN}        xpath=//p[contains(text(), 'Your email or password is incorrect!')]


# --- Mapeamento doLogin ---


${LOGAR_EMAIL_CAMPO}     css=[data-qa="login-email"]
${LOGAR_SENHA_CAMPO}     css=[data-qa="login-password"]
${CONECTAR_BOTAO}       css=[data-qa="login-button"]

# --- Criar Novo Usuario ---

${NOVO_NOME_CAMPO}     css=[data-qa="signup-name"]
${NOVO_EMAIL_CAMPO}     css=[data-qa="signup-email"]
${INSCREVER_BOTAO}     css=[data-qa="signup-button"]

*** Keywords ***

Preencher Login
    [Arguments]     ${EMAIL}     ${SENHA}
    Input Text      ${LOGAR_EMAIL_CAMPO}     ${EMAIL}
    Input Text      ${LOGAR_SENHA_CAMPO}     ${SENHA}

Clicar No Botao Login
    Click Button     ${CONECTAR_BOTAO}

Validar Mensagem de Erro
    # O Wait garante que o sistema teve tempo de processar o erro e exibir o aviso
    Wait Until Element Is Visible    ${AVISO_ERRO_LOGIN}    10s
    Element Should Contain           ${AVISO_ERRO_LOGIN}    Your email or password is incorrect!