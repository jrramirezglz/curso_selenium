import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#def test_navegacion_free_range_tester():
#    driver.get('https://www.freerangetesters.com/')
#    driver.find_element(By.XPATH,"//a[normalize-space()='Cursos' and @href]"
#                        ).click()
    #//*[@id='page_header']/div/section/div/header/nav/ul/li[1]/a"
    # /html/body/div/div[1]/div/section/div/header/nav/ul/li[1]/a

#encadenar locators
@pytest.fixture
def browser():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://thefreerangetester.github.io/sandbox-automation-testing/')
    yield driver
    driver.quit()

def test_navegacion_hamburguesa(browser):
    contenedor_checkbox = browser.find_element(By.CLASS_NAME,'mt-3')
    #dentro del contenedor buscar el checkbox hamburguesa
    checkbox_hamburguesa =contenedor_checkbox.find_element(By.ID,'checkbox-1')
    #interaccion con el checkbox le hace click
    if not checkbox_hamburguesa.is_selected():
        checkbox_hamburguesa.click()
    assert checkbox_hamburguesa.is_selected()