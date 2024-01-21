from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestMovingToConstructorFromPrivateArea:
    def test_logo_clickable(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        driver.find_element(*Locators.LOGO_BUTTON).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR))

    def test_button_constructor(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        driver.find_element(*Locators.MAIN_PAGE).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.CONSTRUCTOR))
