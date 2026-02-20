🧪 QA Automation Portfolio – Python + Playwright

Projeto de automação de testes End-to-End (E2E) desenvolvido com Python, Playwright e Pytest, aplicando boas práticas de qualidade de software e arquitetura escalável baseada em Page Object Model (POM).

Este repositório simula um ambiente real de times de QA, incluindo organização modular, reutilização de componentes, e preparação para integração contínua (CI/CD).

🎯 Objetivo

Automatizar fluxos críticos de aplicações web

Garantir cobertura funcional com cenários positivos e negativos

Aplicar boas práticas de arquitetura de testes

Simular estrutura profissional utilizada em empresas

🧰 Stack Utilizada

Python

Playwright

Pytest

Page Object Model (POM)

Git / GitHub

Jenkins (Pipeline CI/CD)

Execução headless e headed

Configuração via pytest.ini

Fixtures globais com conftest.py

🌐 Sistemas Automatizados

Aplicações públicas utilizadas para estudo, testes executados nas paginas:

Obs: todos testes funcionam, alguns sites podem estar fora do ar

https://demoqa.com

https://www.saucedemo.com

https://demo.nopcommerce.com/

🧪 Estratégia de Testes

O projeto contempla:

✔ Testes Funcionais

✔ Testes End-to-End (E2E)

✔ Testes de Regressão

✔ Testes Smoke

✔ Cenários Positivos e Negativos

✔ Validação de mensagens de erro

✔ Validação de regras de negócio

✔ Manipulação de DOM e validações dinâmicas

📋 Exemplos de Cenários Automatizados

CRUD completo (Create, Read, Update, Delete)

Fluxo de login válido e inválido

Adição de produto ao carrinho

Validação de dados exibidos em tabela

Filtros e busca de registros

Validação de mensagens de erro

🏗 Arquitetura do Projeto

O projeto segue o padrão Page Object Model (POM) para garantir:

Separação entre lógica de teste e mapeamento de elementos

Reutilização de componentes

Facilidade de manutenção

Escalabilidade

Estrutura:

Python_Playwright/
│
├── pages/
│   ├── sites mapeados

├── tests/
│
├── conftest.py
├── pytest.ini
└── README.md


🚀 Execução dos Testes

Instalar dependências:

pip install -r requirements.txt
playwright install

Executar testes:

pytest

Executar em modo headed:

pytest --headed