import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from constants import Constants
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()






