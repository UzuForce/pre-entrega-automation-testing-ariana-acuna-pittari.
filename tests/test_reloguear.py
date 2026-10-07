from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import esperar_visible, hacer_login


def test_logout(driver):
    hacer_login(driver)

    # Abrir el menú y cerrar sesión
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    # Debe volver a la pantalla de login
    assert esperar_visible(driver, (By.ID, "login-button")).is_displayed(), "No volvió al login"


def test_acceso_sin_login(driver):
    # Entrar directo al inventario sin iniciar sesión
    driver.get("https://www.saucedemo.com/inventory.html")

    mensaje = esperar_visible(driver, (By.CSS_SELECTOR, "[data-test='error']")).text
    assert "only access '/inventory.html' when you are logged in" in mensaje
