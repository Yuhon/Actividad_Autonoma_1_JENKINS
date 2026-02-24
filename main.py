from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def esperar(driver, locator, condicion, tiempo=10):
    wait = WebDriverWait(driver, tiempo)
    return wait.until(condicion(locator))

driver = webdriver.Chrome()
driver.maximize_window()

inicio = time.perf_counter()

driver.get("https://webdriveruniversity.com/Ajax-Loader/index.html")

esperar(driver, (By.ID, "loader"), EC.invisibility_of_element_located)

fin = time.perf_counter()
print("Tiempo hasta que desaparece el loader:", round(fin - inicio, 2), "segundos")

boton = esperar(driver, (By.ID, "button1"), EC.element_to_be_clickable)
boton.click()

modal = esperar(driver, (By.CLASS_NAME, "modal-content"), EC.visibility_of_element_located)

if modal.is_displayed():
    print("El modal se mostró correctamente")
else:
    print("El modal NO se mostró")

driver.quit()