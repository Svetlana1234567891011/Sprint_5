from selenium.webdriver.common.by import By


class Locators:
    PRIVATE_AREA = (By.XPATH, "//a[@href='/account']")  # Кнопка (ссылка) перехода на страницу входа Личный кабинет
    REG_BUTTON = (By.XPATH, "//a[@href = '/register']")  # Ссылка на страницу регистрации
    NAME = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@name='name']")  # поле ввода имени
    EMAIL_FIELD = (By.XPATH, "//label[text()='Email']/following-sibling::input[@name='name']")  # поле ввода почты
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")  # поле пароля
    SUBMIT_BUTTON = (By.CSS_SELECTOR,
                     ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    # Кнопка Зарегистрироваться для отправки данных для регистрации на странице
    SUBMIT_BUTTON1 = (By.CSS_SELECTOR,
                      ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    # кнопка Войти, отправляющая данные пользователя для залогинивания
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']") # кнопка Оформить заказ
    STATUS_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')]")  # Некорректный пароль (сообщение об ошибке)
    LOGIN_BUTTON_MAIN = (By.XPATH,
                         "//button[contains(@class, 'button_button__33qZ0 button_button_type_primary__1O7Bx')]")
    ENTER = (By.XPATH, "//a[@href='/login']")
    # вход через кнопку в форме восстановления пароля
    FORGOT_PASSWORD = (By.XPATH, "//a[@href='/forgot-password']")
    # раздел восстановления пароля
    MAIN_PAGE = (By.XPATH, "//a[contains(@class, 'AppHeader_header__link__3D_hX') and @href='/']")
    # кнопка (ссылка) на главную страницу
    CONSTRUCTOR = (By.XPATH, ".//section[@class='BurgerIngredients_ingredients__1N8v2']")
    # кнопка (ссылка) конструктора
    EXIT_BUTTON = (
        By.XPATH, "//button[contains(@class, 'Account_button__14Yp3 text text_type_main-medium text_color_inactive')]")
    # кнопка выхода из аккаунта (разлогинивания)
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo__2D0X2')]") # логотип
    SECTION_BUTTON_CLICKED = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect')]")  #
    # кнопка (активный таб), по которой кликнули
    SECTION_BUTTON2 = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG:nth-child(2)')  # таб раздела конструктора
    SECTION_BUTTON1 = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG:nth-child(1)')  # таб раздела конструктора
    SECTION_BUTTON3 = (By.CSS_SELECTOR, 'div.tab_tab__1SPyG:nth-child(3)')  # таб раздела конструктора
