from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pandas as pd

df = pd.read_excel("dados_selenium.xlsx")

navegador = webdriver.Chrome()

navegador.get("https://www.rpachallenge.com/")
navegador.maximize_window()
time.sleep(5)

for index, row in df.iterrows():
    primeiro_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelCompanyName')]").send_keys(row["Company Name"])
    segundo_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelPhone')]").send_keys(row["Phone Number"])
    terceiro_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelEmail')]").send_keys(row["Email"])
    quarto_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelFirstName')]").send_keys(row["First Name"])
    quinto_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelLastName')]").send_keys(row["Last Name "])
    sexto_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelAddress')]").send_keys(row["Address"])
    setimo_campo = navegador.find_element(By.XPATH, "//input[contains(@ng-reflect-name, 'labelRole')]").send_keys(row["Role in Company"])
    time.sleep(3)
    botão_submit = navegador.find_element(By.XPATH, "//input[contains(@class, 'btn') and @type='submit']")
    navegador.execute_script("arguments[0].scrollIntoView()", botão_submit)
    botão_submit.click()
    time.sleep(3)    
