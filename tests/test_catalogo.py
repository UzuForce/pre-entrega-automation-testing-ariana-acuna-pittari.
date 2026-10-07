from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from utils.helpers import esperar_visible, hacer_login


def test_ordenar_por_precio(driver):
    hacer_login(driver)

    # Ordenar de menor a mayor precio
    Select(driver.find_element(By.CLASS_NAME, "product_sort_container")).select_by_value("lohi")

    # Los precios deben quedar en orden ascendente
    textos = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    precios = [float(t.text.replace("$", "")) for t in textos]
    assert precios == sorted(precios)


def test_detalle_de_producto(driver):
    hacer_login(driver)

    # Entrar al detalle del primer producto
    enlace = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    nombre = enlace.text
    enlace.click()

    # Verificar que se abre la página del producto con el mismo nombre
    nombre_detalle = esperar_visible(driver, (By.CLASS_NAME, "inventory_details_name")).text
    assert "/inventory-item.html" in driver.current_url, "No se abrió el detalle del producto"
    assert nombre_detalle == nombre
