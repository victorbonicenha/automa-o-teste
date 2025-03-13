from playwright.sync_api import sync_playwright
import time
import pandas as pd 

df = pd.read_excel("dados_Playwright.xlsx")

with sync_playwright() as p:
    navegador = p.chromium.launch(args=['--start-maximized'], headless=False)
    pagina = navegador.new_page(no_viewport=True)
    pagina.goto("https://www.rpachallenge.com/")
    time.sleep(3)
    
    for index, row in df.iterrows():
        pagina.locator("[ng-reflect-name='labelPhone']").fill(str(row["Phone Number"]))
        pagina.locator("[ng-reflect-name='labelEmail']").fill(row["Email"])
        pagina.locator("[ng-reflect-name='labelAddress']").fill(row["Address"])
        pagina.locator("[ng-reflect-name='labelLastName']").fill(row["Last Name "])
        pagina.locator("[ng-reflect-name='labelFirstName']").fill(row["First Name"])
        pagina.locator("[ng-reflect-name='labelCompanyName']").fill(row["Company Name"])
        pagina.locator("[ng-reflect-name='labelRole']").fill(row["Role in Company"])
        time.sleep(3)
        scroll_submit = pagina.locator("input[value='Submit']").scroll_into_view_if_needed()
        botao_submit = pagina.locator("input[value='Submit']").click()
        time.sleep(4)
