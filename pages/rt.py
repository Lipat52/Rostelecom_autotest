from pages.base import WebPage
from pages.elements import WebElement, ManyWebElements
from setting import main_url


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = main_url

        super().__init__(web_driver, url)

    '''Страница регистрации'''
    # Локатор ссылки зарегистрироваться
    registration = WebElement(id='kc-register')
    # Локатор для имени
    first_name = WebElement(name='firstName')
    # Локатор для ошибок после ввода имени
    error_first_name = WebElement(xpath='//*[@class="rt-input-container rt-input-container--error"][1]/span')
    # Локатор для фамилии
    last_Name = WebElement(name='lastName')
    # Локатор для ошибок после ввода фамилии
    error_last_name = WebElement(xpath='//*[@class="rt-input-container rt-input-container--error"][2]/span')
    # Локатор для email/телефон
    address = WebElement(id='address')
    # Локатор для ошибок после ввода email/телефона
    error_address = WebElement(
        xpath='//*[@class="rt-input-container rt-input-container--error email-or-phone register-form__address"]/span')
    # Локатор для пароля
    password = WebElement(name='password')
    # Локатор для ошибок после ввода пароля
    error_password = WebElement(
        xpath='//*[@class="rt-input-container rt-input-container--error new-password-container__password"]/span')
    # Локатор для подтверждения пароля
    password_confirm = WebElement(name='password-confirm')
    # Локатор для ошибок после ввода подтверждения пароля
    error_password_confirm = WebElement(
        xpath='//*[@class="rt-input-container rt-input-container--error new-password-container__confirmed-password"]/span')
    # Локатор для кнопки зарегистрироваться
    register = WebElement(name='register')
    # Локатор body
    body = WebElement(xpath='//body')
    # Локатор существующей учетной записи
    existing_account = WebElement(xpath='//h2[contains(text(),"Учётная запись уже существует")]')

    '''Страница подтверждения email'''
    # Локатор текста Подтверждение email
    confirm = WebElement(xpath='//h1[contains(text(),"Подтверждение email")]')
    # Локатор временного кода
    time_code_1 = WebElement(id='rt-code-0')
    # Локатор ошибки кода
    error_time_code = WebElement('//span[@id="form-error-message""]')
    # Локатор для смены email
    change_email = WebElement(name='otp_back_phone')

    '''Страница с номерами телефонов'''
    # Локатор номеров телефонов
    phone = ManyWebElements(xpath='//*[@class="npn nol"]')

    '''Страница с  генерацией email'''
    # Локатор копирования email
    copy_email = WebElement(xpath='//div[@id="topmenu"]/a[1]')
    # Локатор проверки email
    check_email = WebElement(xpath='//button[contains(text(),"Check mail")]')
    # Локатора email
    mail = WebElement(xpath='//a[contains(text(),"Регистрация в Ростелеком ID")]')
    # Локатор кода в email
    email_code = WebElement(xpath='//div[@id="messageBody"]/div/p')

    '''Страница авторизации'''
    # Локатор для ошибок
    error_login = WebElement(id='form-error-message')
    # Локатор раздела телефон
    section_phone = WebElement(id='t-btn-tab-phone')
    # Локатор для мобильного телефона
    user_name = WebElement(id='username')
    # Локатор для мобильного телефона
    user_password = WebElement(id='password')
    # Локатор раздела почта
    section_mail = WebElement(id='t-btn-tab-mail')
    # Локатор раздела логин
    section_login = WebElement(id='t-btn-tab-login')
    # Локатор раздела лицевой счет
    section_ls = WebElement(id='t-btn-tab-ls')
    # Локатор для кнопки войти
    login = WebElement(id='kc-login')

    '''Страница кабинета'''
    # Локатор кабинета
    lk = WebElement(id='lk-btn')
