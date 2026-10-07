from selenium.webdriver.common.by import By

from utils.helpers import esperar_visible


def intentar_login(driver, usuario, password):
    """Intenta hacer login con los datos indicados y devuelve el mensaje de error."""
    driver.get("https://www.saucedemo.com/")
    esperar_visible(driver, (By.ID, "user-name")).send_keys(usuario)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    return esperar_visible(driver, (By.CSS_SELECTOR, "[data-test='error']")).text


def test_login_password_incorrecta(driver):
    mensaje = intentar_login(driver, "standard_user", "clave_incorrecta")
    assert "do not match any user" in mensaje, f"Mensaje inesperado: {mensaje}"
    assert "/inventory.html" not in driver.current_url, "No debería haber entrado al inventario"


def test_login_usuario_bloqueado(driver):
    mensaje = intentar_login(driver, "locked_out_user", "secret_sauce")
    assert "locked out" in mensaje, f"Mensaje inesperado: {mensaje}"
    assert "/inventory.html" not in driver.current_url, "No debería haber entrado al inventario"


def test_login_campos_vacios(driver):
    mensaje = intentar_login(driver, "", "")
    assert "Username is required" in mensaje, f"Mensaje inesperado: {mensaje}"
