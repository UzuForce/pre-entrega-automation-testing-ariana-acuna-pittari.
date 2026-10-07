"""Fixture del driver y captura de pantalla cuando un test falla."""
import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver

logger = logging.getLogger(__name__)
CARPETA_REPORTES = os.path.join(os.path.dirname(__file__), "..", "reports")


@pytest.fixture
def driver(request):
    """Abre un Chrome nuevo para cada test (HEADLESS=1 para correr sin ventana)."""
    opciones = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS") == "1":
        opciones.add_argument("--headless=new")
    drv = webdriver.Chrome(options=opciones)
    drv.maximize_window()
    request.node.driver = drv
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si el test falla, guarda una captura en reports/ y la deja en el log."""
    reporte = (yield).get_result()
    drv = getattr(item, "driver", None)
    if reporte.when == "call" and reporte.failed and drv:
        os.makedirs(CARPETA_REPORTES, exist_ok=True)
        marca = datetime.now().strftime("%Y%m%d_%H%M%S")
        ruta = os.path.join(CARPETA_REPORTES, f"fallo_{item.name}_{marca}.png")
        drv.save_screenshot(ruta)
        logger.error("Test fallido: %s. Captura: %s", item.name, ruta)
