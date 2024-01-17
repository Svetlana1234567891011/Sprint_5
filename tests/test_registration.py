from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Locators

faker = Faker()


class Test:
    def test_registration(self, driver):
        name = 'Masha'
        email = faker.email()
        password = 'sota310311'
        driver.find_element(*Locators.PRIVATE_AREA).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        wait = WebDriverWait(driver, 50)
        wait.until(
            EC.visibility_of_element_located(Locators.REG_BUTTON))  # ждем, чтобы прогрузилась вся страница целиком
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON1).click()
        wait = WebDriverWait(driver, 20)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
