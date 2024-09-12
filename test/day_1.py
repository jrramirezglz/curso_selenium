from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest

#driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
"""
def test_prueba():
    driver.get('https://www.freerangetesters.com/')
    titulo=driver.title
    assert titulo == 'Free Range Testers'
"""

@pytest.fixture(params=["playwrighty","Selenium","cypress"])
def termino_de_busqueda(request):
    return request.param

@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://www.google.com/')
    yield driver
    driver.quit()

def test_google_busqueda(browser,termino_de_busqueda):
    search_box = browser.find_element("name","q")
    search_box.send_keys(termino_de_busqueda+Keys.RETURN)
    result =browser.find_element("id","search")
    assert (len(result.find_elements("xpath",'.//div'))>0
            ),'Hay resultado de busqueda'

