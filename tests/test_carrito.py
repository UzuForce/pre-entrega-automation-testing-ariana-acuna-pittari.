from selenium.webdriver.common.by import By

from utils.helpers import esperar_visible, hacer_login


def test_carrito(driver):
    hacer_login(driver)

    # 1) Agregar al carrito el primer producto
    primer_item = driver.find_element(By.CLASS_NAME, "inventory_item")
    nombre = primer_item.find_element(By.CLASS_NAME, "inventory_item_name").text
    primer_item.find_element(By.TAG_NAME, "button").click()

    # 2) Verificar que el contador del carrito sea 1
    contador = esperar_visible(driver, (By.CLASS_NAME, "shopping_cart_badge")).text
    assert contador == "1"

    # 3) Ir al carrito y confirmar el producto
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    nombre_carrito = esperar_visible(driver, (By.CSS_SELECTOR, ".cart_item .inventory_item_name")).text
    assert nombre_carrito == nombre, "El producto del carrito no coincide"


def test_agregar_dos_productos(driver):
    hacer_login(driver)

    # Agregar los dos primeros productos y verificar que el contador sea 2
    botones = driver.find_elements(By.CSS_SELECTOR, "button.btn_inventory")
    botones[0].click()
    botones[1].click()
    contador = esperar_visible(driver, (By.CLASS_NAME, "shopping_cart_badge")).text
    assert contador == "2"


def test_quitar_producto(driver):
    hacer_login(driver)

    # Agregar el primer producto y luego quitarlo
    driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()
    esperar_visible(driver, (By.CLASS_NAME, "shopping_cart_badge"))
    driver.find_element(By.CSS_SELECTOR, "button.btn_inventory").click()

    # El contador del carrito ya no debe aparecer
    assert len(driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")) == 0, "El contador sigue visible"
