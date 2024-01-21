from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants


class TestExit:
    def test_exit_by_exit_button(self, driver):
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.LOGIN_BUTTON_MAIN))
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
        driver.find_element(*Locators.SUBMIT_BUTTON1).click()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.PRIVATE_AREA))
        driver.find_element(*Locators.PRIVATE_AREA).click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        wait = WebDriverWait(driver, 20)
        assert wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1)) # если появляется кнопка Войти
        # значит нам удалось разлогиниться
