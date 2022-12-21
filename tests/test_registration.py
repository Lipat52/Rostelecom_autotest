# How to run:
#  1) Download driver for Chrome here:
#     https://chromedriver.chromium.org/downloads
#  2) Install all requirements:
#     pip install -r requirements.txt
#  3) Run tests:
#     pytest --driver Chrome  --alluredir results
import allure
import pytest

from pages.rt import MainPage
from setting import email
from setting import generate_random_name, generate_random_password
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести все предложенные данные корректно')
@pytest.mark.parametrize(
    'first_names, last_names, password',
    [('Алексей', 'Липатов', 'QwerT1234'),
     ('Иван-Иван', 'Иванов-Иванов', 'QwerT1234'),
     pytest.param('Т-т', 'М-м', 'Q123werT4', marks=pytest.mark.xfail(reason='Bug')),
     pytest.param('Дмитрий', 'Сидоров', 'Qwer1234', marks=pytest.mark.xfail(reason='Bug'))]
)
def test_keys_1(web_browser, first_names, last_names, password):
    """ Выполнить регистрацию, введя корректные данные. """

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name = first_names
    page.last_Name = last_names
    page.address = email
    page.password = password
    page.password_confirm = password
    page.register.click()
    sleep(1)

    with allure.step('Перенаправление на страницу получения кода'):
        assert page.confirm.get_text() == 'Подтверждение email'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Заполнить все данные и обновить страницу')
def test_keys_2(web_browser):
    """ Заполнить все данные для регистрации и обновить страницу. """

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    page.address.send_keys(email)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.refresh()
    sleep(1)

    with allure.step('Очистка введённой информации'):
        assert page.first_name.get_attribute('value') and page.address.get_attribute('value') == ''


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Не заполнять данные и выполнить регистрацию')
def test_keys_3(web_browser):
    """При регистрации оставить все поля пустыми и попытаться зарегистрироваться"""

    page = MainPage(web_browser)

    page.registration.click()

    page.register.click()
    sleep(1)

    with allure.step('Неудачная регистрация'):
        assert page.confirm.is_visible() is False


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести максимально допустимые значения в поля ввода')
def test_keys_4(web_browser):
    """Выполнить регистрацию введя в поля Имя, Фамилия 30 символов, пароль 20 символов"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys(generate_random_name(30))
    page.last_Name.send_keys(generate_random_name(30))
    page.address.send_keys(email)
    page.password.send_keys(generate_random_password(20))
    p = page.password.get_attribute('value')
    page.password_confirm.send_keys(p)
    page.register.click()
    sleep(1)

    with allure.step('Перенаправление на страницу получения кода'):
        assert page.confirm.get_text() == 'Подтверждение email'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести минимально допустимые значения в поля ввода')
def test_keys_5(web_browser):
    """Выполнить регистрацию введя в поля Имя, Фамилия 2 символа, пароль 8 символов"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys(generate_random_name(2))
    page.last_Name.send_keys(generate_random_name(2))
    page.address.send_keys(email)
    page.password.send_keys(generate_random_password(8))
    p = page.password.get_attribute('value')
    page.password_confirm.send_keys(p)
    page.register.click()
    sleep(1)

    with allure.step('Перенаправление на страницу получения кода'):
        assert page.confirm.get_text() == 'Подтверждение email'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('В поля «Имя» и «Фамилия» ввести только одни пробелы')
def test_keys_6(web_browser):
    """Выполнить регистрацию введя в поля Имя, Фамилия только пробелы"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('  ')
    page.last_Name.send_keys('  ')
    page.address.send_keys(email)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    sleep(1)

    with allure.step('Неудачная регистрация'):
        assert page.error_first_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        assert page.error_last_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести значения больше максимально допустимых в поля ввода')
def test_keys_7(web_browser):
    """Выполнить регистрацию введя в поля Имя, Фамилия больше 30 символов, пароль больше 20 символов"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys(generate_random_name(31))
    page.last_Name.send_keys(generate_random_name(40))
    page.address.send_keys(email)
    page.password.send_keys(generate_random_password(21))
    p = page.password.get_attribute('value')
    page.password_confirm.send_keys(p)
    page.register.click()
    sleep(1)

    with allure.step('Неудачная регистрация'):
        assert page.error_first_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        assert page.error_last_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        assert page.error_password.get_attribute(
            'textContent') == 'Длина пароля должна быть не более 20 символов'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести значения меньше минимально допустимых в поля ввода')
def test_keys_8(web_browser):
    """Выполнить регистрацию введя в поля Имя, Фамилия меньше 2 символов, пароль меньше 8 символов"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys(generate_random_name(1))
    page.last_Name.send_keys(generate_random_name(1))
    page.address.send_keys(email)
    page.password.send_keys(generate_random_password(7))
    p = page.password.get_attribute('value')
    page.password_confirm.send_keys(p)
    page.register.click()
    sleep(1)

    with allure.step('Неудачная регистрация'):
        assert page.error_first_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        assert page.error_last_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        assert page.error_password.get_attribute(
            'textContent') == 'Длина пароля должна быть не менее 8 символов'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести некорректные данные в поля Имя, Фамилия')
def test_keys_9(web_browser):
    """Выполнить регистрацию введя в поля Имя, Фамилия слова на кириллице, цифры, спецсимволы"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('\'~@#$%^&*()_+|-={}[]:”;’<>?\'')
    page.last_Name.send_keys('Asdf1234')
    page.register.click()
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_first_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
        assert page.error_last_name.get_attribute(
            'textContent') == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести другой Новый пароль')
def test_keys_10(web_browser):
    """Выполнить регистрацию введя в поле Подтверждение пароля пароль, отличный от введенного в поле Новый пароль"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    page.address.send_keys(email)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('1234QwerT')
    page.register.click()
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_password_confirm.get_attribute(
            'textContent') == 'Пароли не совпадают'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести уже зарегистрированный email/телефон')
@pytest.mark.skip(reason='Необходим доступ к базе данных')
def test_keys_11(web_browser):
    """Выполнить регистрацию введя уже зарегистрированный email/телефон"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    page.address.send_keys(email)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    sleep(1)

    with allure.step('Отображается оповещающая форма для email/телефона'):
        assert page.existing_account.is_visible()


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести в поле email данные в некорректном формате')
@pytest.mark.parametrize('email_phone', ['email', '@gmail.ru', '+19999999999', '+799999999999'])
def test_keys_12(web_browser, email_phone):
    """Выполнить регистрацию введя в поле email/телефон в формате отличным от формата email/телефон"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    page.address.send_keys(email_phone)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_address.get_text() == \
               'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести полученный код из смс')
@pytest.mark.skip(reason='Не приходит код')
def test_keys_13(web_browser):
    """Ввести полученный код из смс"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    web_browser.execute_script("window.open('https://online-sms.org/ru')")
    web_browser.switch_to.window(web_browser.window_handles[1])
    all_numbers = page.phone.get_attribute('outerText')

    rus_number = []
    for p in all_numbers:
        if p.startswith('+7'):
            rus_number = p
            web_browser.find_element(By.XPATH, '//a[contains(text(),"{0}")]'.format(rus_number)).click()
            break

    web_browser.switch_to.window(web_browser.window_handles[0])
    page.address.send_keys(rus_number)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.refresh()
    sleep(1)


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести некорректный код')
def test_keys_15(web_browser):
    """Ввести код отличающийся от того который пришел в смс"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    web_browser.execute_script("window.open('https://online-sms.org/ru')")
    web_browser.switch_to.window(web_browser.window_handles[1])
    all_numbers = page.phone.get_attribute('outerText')

    rus_number = []
    for p in all_numbers:
        if p.startswith('+7'):
            rus_number = p
            web_browser.find_element(By.XPATH, '//a[contains(text(),"{0}")]'.format(rus_number)).click()
            break

    web_browser.switch_to.window(web_browser.window_handles[0])
    page.address.send_keys(rus_number)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    page.time_code_1.send_keys('111111')
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_time_code.get_text() == 'Неверный код. Повторите попытку'


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести полученный код из email')
def test_keys_17(web_browser):
    """Ввести полученный код из email"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    web_browser.execute_script("window.open('https://www.1secmail.com/')")
    web_browser.switch_to.window(web_browser.window_handles[1])
    page.copy_email.click()
    web_browser.switch_to.window(web_browser.window_handles[0])
    page.address.send_keys(Keys.CONTROL + 'v')
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    web_browser.switch_to.window(web_browser.window_handles[1])
    sleep(5)
    page.check_email.click()
    page.mail.click()
    p = page.email_code.get_text().split()[3]
    web_browser.switch_to.window(web_browser.window_handles[0])
    page.time_code_1.send_keys(p)
    sleep(1)

    with allure.step('Перенаправление в кабинет'):
        assert page.lk.is_visible()


@allure.feature('Тест-кейсы для регистрации')
@allure.story('Ввести некорректный код')
def test_keys_19(web_browser):
    """Ввести код отличающийся от того который пришел в email"""

    page = MainPage(web_browser)

    page.registration.click()

    page.first_name.send_keys('Алексей')
    page.last_Name.send_keys('Липатов')
    page.address.send_keys(email)
    page.password.send_keys('QwerT1234')
    page.password_confirm.send_keys('QwerT1234')
    page.register.click()
    sleep(5)
    page.time_code_1.send_keys('111111')
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_time_code.get_text() == 'Неверный код. Повторите попытку'


@allure.feature('Тест-кейсы для авторизации')
@allure.story('Авторизация по некорректному номеру телефона')
def test_keys_24(web_browser):
    """Выполнить авторизацию, введя не зарегистрированный номер телефона"""

    page = MainPage(web_browser)

    page.section_phone.click()
    page.user_name.send_keys('9999999999')
    page.user_password.send_keys('QwerT1234')
    page.login.click()
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_login.get_text() == 'Неверный логин или пароль'


@allure.feature('Тест-кейсы для авторизации')
@allure.story('Авторизация по email')
def test_keys_26(web_browser):
    """Выполнить авторизацию, введя зарегистрированный email и пароль"""

    page = MainPage(web_browser)

    page.section_mail.click()
    page.user_name.send_keys('bpn72qik05@dcctb.com')
    page.user_password.send_keys('QwerT1234')
    page.login.click()
    sleep(1)

    with allure.step('Перенаправление в кабинет'):
        assert page.lk.is_visible()


@allure.feature('Тест-кейсы для авторизации')
@allure.story('Авторизация по email с не корректным паролем')
def test_keys_28(web_browser):
    """Выполнить авторизацию, введя зарегистрированный email и некорректный пароль"""

    page = MainPage(web_browser)

    page.section_mail.click()
    page.user_name.send_keys('bpn72qik05@dcctb.com')
    page.user_password.send_keys('QwerT12345')
    page.login.click()
    sleep(1)

    with allure.step('Сообщение об ошибке'):
        assert page.error_login.get_text() == 'Неверный логин или пароль'


