import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

from utils.helpers import get_driver

@pytest.fixture
def driver():
    #configuracion para consultar a selenium web driver
    driver = get_driver()
    yield driver
    driver.quit()