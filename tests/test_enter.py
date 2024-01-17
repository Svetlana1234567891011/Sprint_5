from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..constants import login
from ..locators import Locators


class Test:
    def test_enter_main(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        login(driver)
        wait = WebDriverWait(driver, 20)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_from_private(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        login(driver)
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_registration(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        login(driver)
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_from_forget_pass(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.ENTER).click()
        login(driver)
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
