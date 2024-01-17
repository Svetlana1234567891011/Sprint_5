import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from .locators import Locators
from .constants import Constants
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(Constants.URL)
    yield driver
    driver.quit()


@pytest.fixture
def login(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
    # WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_MAIN))
    # driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
    driver.find_element(*Locators.SUBMIT_BUTTON1).click()
    return driver



