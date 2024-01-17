from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Locators

faker = Faker()


class TestIncorrectPassword:
    def test_incorrect_password(self, driver):
        name = 'Masha'
        email = faker.email()
        password = 'sota'
        driver.find_element(*Locators.PRIVATE_AREA).click()
        driver.find_element(*Locators.REG_BUTTON).click()
        driver.find_element(*Locators.NAME).send_keys(name)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.SUBMIT_BUTTON).click()
        reg_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.STATUS_MESSAGE)).text
        assert reg_text == "Некорректный пароль"
