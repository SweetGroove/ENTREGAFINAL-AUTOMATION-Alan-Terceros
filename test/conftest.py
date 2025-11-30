import pytest
import datetime
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utils.helpers import get_driver

@pytest.fixture
def driver():
    #configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Ejecuta todos los demás hooks de reporteo primero
    outcome = yield
    report = outcome.get_result()

    # Verifica si el test falló (report.when == 'call' y report.failed)
    if report.when == 'call' and report.failed:
        print("\n*** TEST FALLIDO, GENERANDO CAPTURA DE PANTALLA ***")
        
        # Accede al fixture 'driver' a través del request del item
        try:
            driver = item.funcargs['driver'] 
        except KeyError:
            # Si el test que falló no usaba el fixture 'driver', ignora la captura
            return

        # 1. Definir Directorio de Capturas
        SCREENSHOTS_DIR = "capturas_fallos"
        os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
        
        # 2. Obtener Nombre del Test y Sanitizar
        # El nombre completo del test, incluyendo el módulo: 
        # ejemplo: tests/test_login.py::test_login_fallido
        test_node_id = item.nodeid 
        # Sanitizar para el nombre de archivo: reemplazar :: y / por _
        test_name_sanitized = test_node_id.replace("::", "_").replace("/", "_")
        
        # 3. Generar Timestamp (YYYYMMDD_HHmmss)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # 4. Crear Nombre de Archivo Completo
        filename = f"{test_name_sanitized}_{timestamp}.png"
        file_path = os.path.join(SCREENSHOTS_DIR, filename)

        # 5. Tomar y Guardar la Captura
        try:
            driver.get_screenshot_as_file(file_path)
            print(f"Captura guardada exitosamente en: {file_path}")
        except Exception as e:
            print(f"Error al intentar guardar la captura: {e}")