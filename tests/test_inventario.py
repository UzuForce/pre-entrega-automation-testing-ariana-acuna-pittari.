from selenium.webdriver.common.by import By

from utils.helpers import esperar_visible, hacer_login


def test_inventario(driver):
    hacer_login(driver)

    # 1) Validar título de la página de inventario
    titulo = driver.find_element(By.CLASS_NAME, "title").text
    assert titulo == "Products"

    # 2) Verificar que exista al menos un producto
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No se encontraron productos"

    # 3) Listar nombre y precio del primer producto
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"Primer producto: {nombre} - {precio}")

    # 4) Elementos importantes de la interfaz: menú, filtro y carrito
    assert esperar_visible(driver, (By.ID, "react-burger-menu-btn")).is_displayed(), "Falta el menú"
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed(), "Falta el filtro"
    assert driver.find_element(By.CLASS_NAME, "shopping_cart_link").is_displayed(), "Falta el carrito"
