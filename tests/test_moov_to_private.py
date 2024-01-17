from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Locators


class Test:
    def test_registration(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        wait = WebDriverWait(driver, 20)
        assert wait.until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
