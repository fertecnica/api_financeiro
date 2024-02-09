from playwright.sync_api import sync_playwright

class BankScrapper:

    def __init__(self) -> None:
        pass

    def scrapping_process(self):
        with sync_playwright() as p:
            self.browser = p.chromium.launch(headless=True)
            self.context = self.browser.new_context(
                viewport={ 'width': 680, 'height': 680 },
                device_scale_factor=2,
                user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
                base_url='https://app.expenseon.com/admin/login?ReturnURL=/admin/financeiro/relatorio'
            )
            self.page = self.context.new_page()

            # Acessa a página de login
            self.page.goto('https://app.expenseon.com/admin/login?ReturnURL=/admin/financeiro/relatorio')

            # Aguarda e clica no botão de aceitação de cookies
            self.page.click('xpath=//button[contains(text(), "Li e aceito")]')

            # Preenche o campo de email
            self.page.fill('#usuarioEmail', 'hassan.primo@fertecnica.net')

            # Clica no botão "PRÓXIMO"
            self.page.click('xpath=//*[@id="lookup"]/button')

            # Preenche o campo de senha
            self.page.fill('#usuarioSenha', '3823D1C79418@')  # Substitua pela sua senha real

            # Clica no botão de login
            self.page.click('name=login')

            # Aguarda até que a página de relatórios seja carregada
            self.page.wait_for_selector('#badgeFinanceiroRelatorio')

            # Navega diretamente para a página de relatórios
            self.page.goto('https://app.expenseon.com/admin/financeiro/relatorio')

            # Preenche o campo de data
            self.page.fill('name=dt_inicio', '01/07/2023')

            # Clica no botão OK para iniciar o download do arquivo
            response = self.page.click('xpath=//button[contains(text(), "OK")]')
            print(f'Resposta -> {response}')