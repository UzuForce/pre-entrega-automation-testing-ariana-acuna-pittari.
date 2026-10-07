"""Funciones auxiliares para los tests de saucedemo.com."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def esperar_visible(driver, locator, segundos=10):
    """Espera explícita: devuelve el elemento cuando es visible."""
    return WebDriverWait(driver, segundos).until(EC.visibility_of_element_located(locator))


def hacer_login(driver):
    """Abre saucedemo.com, ingresa credenciales válidas y espera el inventario."""
    driver.get("https://www.saucedemo.com/")
    esperar_visible(driver, (By.ID, "user-name")).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/inventory.html"))
