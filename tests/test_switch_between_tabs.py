from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ..locators import Locators


class TestTab:
    def test_click_tab2(self, driver):
        driver.find_element(*Locators.SECTION_BUTTON2).click()
        wait = WebDriverWait(driver, 10)
        name_section = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON_CLICKED)).text
        assert name_section == driver.find_element(*Locators.SECTION_BUTTON2).text

    def test_click_tab1(self, driver):
        driver.find_element(*Locators.SECTION_BUTTON2).click()
        driver.find_element(*Locators.SECTION_BUTTON1).click()
        wait = WebDriverWait(driver, 10)
        name_section = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON_CLICKED)).text
        assert name_section == driver.find_element(*Locators.SECTION_BUTTON1).text

    def test_click_tab3(self, driver):
        driver.find_element(*Locators.SECTION_BUTTON3).click()
        wait = WebDriverWait(driver, 10)
        name_section = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON_CLICKED)).text
        assert name_section == driver.find_element(*Locators.SECTION_BUTTON3).text
