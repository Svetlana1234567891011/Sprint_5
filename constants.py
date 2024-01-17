from selenium.webdriver.chrome import webdriver
import time

from selenium.webdriver.common.by import By


from selenium.webdriver.support.wait import WebDriverWait
# driver = webdriver.Chrome()
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .locators import Locators


class Constants:
    URL = 'https://stellarburgers.nomoreparties.site/'
    email = 'svetlana.smirnova22023@formatkoda.ru'
    password = 'sota310311'


def login(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
    driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
    driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
    wait = WebDriverWait(driver, 20)
    wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
    driver.find_element(*Locators.SUBMIT_BUTTON1).click()
    return driver
