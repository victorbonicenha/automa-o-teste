from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from datetime import datetime
from selenium.webdriver.support.ui import Select

year_value = datetime.today().strftime('%Y')
month_value = datetime.today().strftime('%m')
day = datetime.today().strftime('%d')
data_atual = datetime.today().strftime('%Y-%m-%d')
month_antarior = int(month_value)-1


#MODEL 
class UserModel:
    USERNAME = "evsilva@paranoa.com.br"
    PASSWORD = "Paranoa.123"

# CONTROLLER 
class WebController:
    def __init__(self):
        self.site = webdriver.Chrome()

    def open_url(self, link="https://suppliercollaboration.marelli.com/login"):
        self.site.get(link)
        self.site.maximize_window()
        time.sleep(5)

    def login(self):
        self.site.find_element(By.XPATH, '//*[@placeholder="Username"]').send_keys(UserModel.USERNAME)
        time.sleep(1)
        
        self.site.find_element(By.XPATH, '//*[@placeholder="Password"]').send_keys(UserModel.PASSWORD)
        time.sleep(2)

        self.site.find_element(By.XPATH, "/html/body/app-root/app-loginform/div/div[2]/div[2]/form/div[2]/button").click()
        time.sleep(10)

    def navigate(self):
        button = self.site.find_element(By.XPATH, "/html/body/app-root/app-nav/div/div/div/div[2]/app-home/div/div[2]/div[1]/div[2]/div[4]/div/div")
        button.click()
        self.site.execute_script("arguments[0].scrollIntoView()", button)
        time.sleep(5)

        button_SQP = self.site.find_element(By.XPATH, "/html/body/app-root/app-nav/div/div/div/div[2]/app-home/div/div[2]/div[2]/div[5]/container-element/div/div/div/div/button")
        button_SQP.click()
        self.site.execute_script("arguments[0].scrollIntoView()", button_SQP)
        time.sleep(10)

    def buttons(self):
        all_windows = self.site.window_handles
        self.site.switch_to.window(all_windows[1])
        time.sleep(5)
        button_report = self.site.find_element(By.ID, "Report_a")
        button_report.click()
        time.sleep(3)
        button_Quality = self.site.find_element(By.ID, "Quality Score Card_c")
        action = ActionChains(self.site)
        action.move_to_element(button_Quality).perform() 
        time.sleep(3)
        button_Quality_score = self.site.find_element(By.XPATH, "//*[@href='/sqp/main/pages/report/6']")
        action = ActionChains(self.site)
        action.move_to_element(button_Quality_score).perform()
        button_Quality_score.click()
        time.sleep(10)

    def data(self):
        year = self.site.find_element(By.XPATH, '//*[@id="co_Filters"]/div/div[1]/div/div[1]/app-drop-down/div[2]/select')
        select_year = Select(year)
        select_year.select_by_value(year_value)
        time.sleep(4)

        month = self.site.find_element(By.XPATH, '//*[@id="co_Filters"]/div/div[1]/div/div[2]/app-drop-down/div[2]/select')
        select_month = Select(month)
        select_month.select_by_value(str(month_antarior))
        time.sleep(5)
    
    def download(self):
        butotn_download = self.site.find_element(By.XPATH, '//*[@id="co_Filters"]/div/div[2]/div/div[3]')
        butotn_download.click()
        time.sleep(10)

# EXECUÇÃO 
if __name__ == "__main__":
    controller = WebController()
    controller.open_url()
    controller.login()
    controller.navigate()
    controller.buttons()
    controller.data()
    controller.download()