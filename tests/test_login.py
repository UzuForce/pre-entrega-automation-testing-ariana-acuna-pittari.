import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.helpers import esperar_visible


def test_login_exitoso():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.saucedemo.com/")

        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        # Ingresar credenciales válidas y hacer login
        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")
        boton_login.click()

        # Validar que se redirigio al inventario
        titulo = esperar_visible(driver, (By.CLASS_NAME, "title"))
        assert "/inventory.html" in driver.current_url, "No se redirigió a /inventory.html"

        # Validacion texto
        logo = driver.find_element(By.CLASS_NAME, "app_logo")
        assert logo.text == "Swag Labs"
        assert titulo.text == "Products"
        assert driver.title == "Swag Labs"

        titulo = driver.find_element(By.CSS_SELECTOR, "[data-test='title']")
        assert titulo.text == "Products"

        # Cierra el navegador - Fin del Try
    finally:
        driver.quit()
