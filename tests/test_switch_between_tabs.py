from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators


class TestTab:
    def test_click_tab2(self, driver):
        driver.find_element(*Locators.SECTION_BUTTON2).click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON_CLICKED))
        class_attribute = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON1)).get_attribute(
            "class")
        assert "tab_tab_type_current__2BEPc" in class_attribute  # Проверяем наличие класса кликнутой кнопки
        # в строке атрибута

    def test_click_tab1(self, driver):
        driver.find_element(*Locators.SECTION_BUTTON2).click()
        driver.find_element(*Locators.SECTION_BUTTON1).click()
        wait = WebDriverWait(driver, 10)
        class_attribute = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON1)).get_attribute(
            "class")
        assert "tab_tab_type_current__2BEPc" in class_attribute  # Проверяем наличие класса кликнутой кнопки
        # в строке атрибута

    def test_click_tab3(self, driver):
        driver.find_element(*Locators.SECTION_BUTTON3).click()
        wait = WebDriverWait(driver, 10)
        # name_section = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON_CLICKED)).text
        # assert name_section == driver.find_element(*Locators.SECTION_BUTTON3).text
        # Мы кликаем по кнопке. Потом мы смотрим кнопку с локатором с current, запоминаем ее текст - это кликнутая кнопка
        # и сравниваем с текстом кнопки по которой только что кликнули (ее локатор отличается порядковым номером nth-child(2)/(1)/(3))
        # assert name_section == driver.find_element(*Locators.SECTION_BUTTON3).text
        class_attribute = wait.until(EC.visibility_of_element_located(Locators.SECTION_BUTTON3)).get_attribute(
            "class")
        assert "tab_tab_type_current__2BEPc" in class_attribute  # Проверяем наличие класса в строке атрибута
