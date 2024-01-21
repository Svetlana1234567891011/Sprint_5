from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import Constants


class Test:
    def test_enter_main(self, driver):
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
        driver.find_element(*Locators.SUBMIT_BUTTON1).click()
        wait = WebDriverWait(driver, 20)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_from_private(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
        driver.find_element(*Locators.SUBMIT_BUTTON1).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_registration(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
        driver.find_element(*Locators.SUBMIT_BUTTON1).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))

    def test_enter_from_forget_pass(self, driver):
        driver.find_element(*Locators.PRIVATE_AREA).click()
        driver.find_element(*Locators.FORGOT_PASSWORD).click()
        driver.find_element(*Locators.ENTER).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.EMAIL_FIELD))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(Constants.email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(Constants.password)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located(Locators.SUBMIT_BUTTON1))
        driver.find_element(*Locators.SUBMIT_BUTTON1).click()
        wait = WebDriverWait(driver, 10)
        assert wait.until(EC.visibility_of_element_located(Locators.ORDER_BUTTON))
