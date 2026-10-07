# Pre-entrega Automation Testing

## Propósito
Automatizar con Selenium WebDriver y Pytest los flujos básicos de [saucedemo.com](https://www.saucedemo.com):
1. **Login** (`test_login.py`): login válido con espera explícita, validando `/inventory.html`, "Products" y "Swag Labs".
2. **Login negativo** (`test_login_negativo.py`): contraseña incorrecta, usuario bloqueado y campos vacíos.
3. **Inventario** (`test_inventario.py`): título, presencia de productos, nombre y precio del primero, y menú, filtro y carrito.
4. **Catálogo** (`test_catalogo.py`): ordenar por precio y detalle de producto.
5. **Carrito** (`test_carrito.py`): agregar el primer producto, verificar contador e ítem; agregar dos productos y quitar uno.
6. **Sesión** (`test_sesion.py`): logout y acceso al inventario sin login.

Los tests son independientes: cada uno abre su propio navegador e inicia sesión con `standard_user` / `secret_sauce`.

## Tecnologías
Python 3, Pytest, Selenium WebDriver, pytest-html, Git/GitHub.

## Estructura
```
tests/       archivos test_*.py y conftest.py (driver y capturas ante fallos)
utils/       helpers.py (login y espera explícita)
datos/       datos externos (si aplica)
reports/     reporte HTML y log de ejecución
pytest.ini   configuración de pytest (reporte y log)
```

## Instalación
```bash
pip install -r requirements.txt
```
Requiere Chrome instalado; Selenium descarga el driver automáticamente.

## Ejecución
```bash
pytest
```

## Evidencias
- Reporte HTML: `reports/reporte.html`
- Log de ejecución: `reports/ejecucion.log`
- Capturas automáticas de los tests que fallan: `reports/fallo_*.png`
# pre-entrega-automation-testing-ariana-acuna-pittari.
