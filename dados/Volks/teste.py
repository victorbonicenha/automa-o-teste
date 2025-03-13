import time 
from selenium import webdriver
import time
from selenium.webdriver.common.by import By


key = 'GOVJKEZXVTVFZ7RJTR2HTILDXTUWFO2K'
navegador = webdriver.Chrome()
navegador.get("https://www.vwgroupsupply.com/one-kbp-pub/en/kbp_public/homepage/homepage.html")
navegador.maximize_window()
time.sleep(5)

def login(url, username, password):
    def caminho_login():
        login = navegador.find_element(By.XPATH, '//a[contains(@href, "login")]')
        login.click()
        time.sleep(8)
    def username():
        preenchimento_login = navegador.find_element(By.ID, "contentForm:profileIdInput")
        preenchimento_login.send_keys("D423549")
        time.sleep(1)
    def password():
        preenchimento_senha = navegador.find_element(By.ID, "contentForm:passwordInput")
        preenchimento_senha.send_keys("Paranoa@2024")
        time.sleep(2)

    def conditions_submit():
        checkbox = navegador.find_element(By.XPATH, '//*[contains(@class, "ui-chkbox-icon")]')
        if "ui-icon-check" in checkbox.get_attribute("class"):
            checkbox.click()

        if "ui-icon-remove" not in checkbox.get_attribute("class"):
            botão_login = navegador.find_element(By.XPATH, '//*[@id="contentForm:passwordLoginAction"]/span')
            botão_login.click()
            time.sleep(15)



def navigate():
    def aplication ():
        aba_aplicação = navegador.find_element(By.CLASS_NAME, "system-dropdown-trigger")
        aba_aplicação.click()
        time.sleep(5)
    def icon():
        foguetinho = navegador.find_element(By.XPATH, '//*[@id="system-dropdown"]/div[2]/ul[1]/li[8]/a/i')
        foguetinho.click()
        time.sleep(5)


