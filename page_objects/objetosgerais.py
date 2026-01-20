import unittest
from playwright.sync_api import sync_playwright

class ObjetosGerais:

    def __init__(self, page):
        self.page = page
        self.botao_submit = page.locator('#submit')
