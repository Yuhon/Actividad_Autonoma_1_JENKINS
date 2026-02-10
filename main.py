from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

service = Service(executable_path="msedgedriver.exe")
driver = webdriver.Edge(service=service)

driver.get("https://www.saucedemo.com")
# time.sleep(2)

# Este es un contador dinamico en vez del time.sleep 
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
)

##Este enlace lo copiamos desde el inspeccionar de la pagna web, el elemento que queramos, click derecho, copy, copy full XPath o
##una forma correcta es en el inspector de navegador ponemos ctrl+f Y se habre el buscador par apoder ir hacienod los inputs 
username_input = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
username_input.send_keys("standard_user")


password_input = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input")
password_input.send_keys("secret_sauce")


boton_login = driver.find_element(By.XPATH, '//input[contains(@value, "Login")]')
boton_login.click()

#time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//div[contains(text(),"T-Shirt")]/../../..//button[contains(text(),"Add")]'))
)

#Esto es para que se agregen los productos 
boton_agregar = driver.find_element(By.XPATH, '//div[contains(text(),"T-Shirt")]/../../..//button[contains(text(),"Add")]')
boton_agregar.click()

boton_agregar = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[1]/div[2]/div[2]/button')
boton_agregar.click()

boton_agregar = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[4]/div[2]/div[2]/button')
boton_agregar.click()

boton_agregar = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div/div/div/div[2]/div[2]/div[2]/button')
boton_agregar.click()

time.sleep(10)