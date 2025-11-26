from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL= "https://www.saucedemo.com/"
USERNAME= "standard_user"
PASSWORD= "secret_sauce"

def get_driver():
    
    #options = Options
    #option.add_argument("--star-maximized")

    #instalacion driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    #time.sleep(5)
    driver.implicitly_wait(5)

    return driver

def login_saucedemo(driver):

    driver.get(URL)

    #INGRESAR CREDENCIALES

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "user-name"))        
    ).send_keys(USERNAME)

    #driver.find_element(By.ID,"user-name").send_keys(USERNAME)    
    driver.find_element(By.ID,"password").send_keys(PASSWORD)
    driver.find_element(By.ID,"login-button").click()

   #time.sleep(7)

    