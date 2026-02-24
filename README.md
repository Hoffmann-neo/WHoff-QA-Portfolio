🧪 Portfólio de Automação de QA – Multi-Framework (Python + Playwright | Robot Framework)
Este repositório contém meu portfólio pessoal de automação de testes End-to-End (E2E), aplicando boas práticas de engenharia de software, arquitetura escalável e padrões de projeto como Page Object Model (POM) e Keyword Driven Development (KDD).

O projeto simula um ambiente real de QA, com foco em manutenção facilitada, reutilização de código e relatórios detalhados.

🎯 Objetivos do Projeto
Automatizar fluxos críticos em diferentes tecnologias de automação.

Garantir cobertura funcional com cenários positivos e negativos.

Demonstrar proficiência tanto em frameworks baseados em código (Playwright) quanto em keywords (Robot Framework).

Estrutura modular preparada para integração contínua (CI/CD).

🧰 Stack Tecnológica
Core
Linguagem: Python

Versionamento: Git / GitHub

Frameworks de Automação
Playwright + Pytest: Automação moderna com foco em performance e execução paralela.

Robot Framework: Automação baseada em palavras-chave (KDD) com SeleniumLibrary, ideal para legibilidade e documentação técnica.

🌐 Ecossistema de Testes (Sistemas Automatizados)
Aplicações utilizadas para os cenários de teste:

Automation Exercise (Foco atual em Robot Framework)

SauceDemo (Foco em Playwright)

DemoQA

🏗 Arquitetura e Organização
O projeto está dividido para demonstrar organização em ambas as ferramentas:

Estrutura Playwright (POM)
Focada em classes e métodos, separando a lógica de negócio do mapeamento de elementos.

Estrutura Robot Framework (KDD/Layers)
Utiliza a separação por camadas para garantir escalabilidade:

Tests: Scripts de teste de alto nível.

Resources: Arquivos .resource contendo Keywords e Variables (Mapeamento de elementos).

Results: Logs e relatórios HTML detalhados gerados automaticamente.

🚀 Como Executar o Projeto
Pré-requisitos
Python 3.10+

Ambiente virtual configurado (venv)

Instalação
Bash
pip install -r requirements.txt
playwright install
Executando Testes Playwright
Bash
pytest --headed
Executando Testes Robot Framework
Bash
robot -d ./results Tests/
📋 Cenários Automatizados (Exemplos)
Login & Autenticação: Fluxos de sucesso, usuário bloqueado e validação de mensagens de erro ("Your email or password is incorrect!").

E-commerce: Adição de produtos ao carrinho e fluxo de checkout.

Gerenciamento de Usuários: Cadastro de novos usuários (Signup) com validação de campos obrigatórios.

Dicas extras para o seu GitHub:
Corrigi o termo "Dramaturgo": O tradutor do navegador às vezes traduz Playwright para Dramaturgo, o que fica estranho em currículos. Mantenha sempre o nome original da ferramenta.

Destaque os Relatórios do Robot: No Robot, você ganha o log.html e o report.html. Se puder, tire um print de um relatório verde (passando) e coloque na pasta assets do seu Git para exibir no README. Recrutadores amam ver relatórios visuais.

Requirements.txt: Não esqueça de atualizar seu arquivo requirements.txt incluindo robotframework e robotframework-seleniumlibrary.
