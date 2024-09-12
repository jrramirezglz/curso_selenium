from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService, Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest

driver =webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
@pytest.mark.navegacion
def test_navegacion():
    driver.get('https://www.freerangetesters.com')
    driver.find_element(By.XPATH, "//a[normalize-space()='cursos' and @href]").click()
