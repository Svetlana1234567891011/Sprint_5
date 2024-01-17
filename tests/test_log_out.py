from ..constants import login
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Locators


class TestExit:
    def test_exit_by_exit_button(self, driver):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        login(driver)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.PRIVATE_AREA))
        driver.find_element(*Locators.PRIVATE_AREA).click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        wait = WebDriverWait(driver, 20)
        assert wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON))
