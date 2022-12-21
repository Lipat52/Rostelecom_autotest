Этот репозиторий содержит пример использования паттерна PageObject с Selenium и Python (PyTest + Selenium).

[Тест кейсы для автотестов](https://docs.google.com/spreadsheets/d/1H9-_ujeKtLYYuUJ8yHZVBjI2XReZsS20A4NB-N5Zwdw/edit#gid=0)

<b>Файлы</b>

[conftest.py](https://github.com/Lipat52/Rostelecom_autotest/blob/master/conftest.py) содержит весь необходимый код для отлова неудачных тестовых случаев и создания скриншота страницы в случае, если какой-либо тестовый пример не сработает.

[pages/base.py](https://github.com/Lipat52/Rostelecom_autotest/blob/master/pages/base.py) содержит реализацию шаблона PageObject для Python.

[pages/elements.py](https://github.com/Lipat52/Rostelecom_autotest/blob/master/pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/test_registation.py](https://github.com/Lipat52/Rostelecom_autotest/blob/master/pages/rt.py) содержит тестs Web UI для ростелекома ( https://b2c.passport.rt.ru )

<b>Как запустить тесты</b>

1. Установить все требования:

pip3 install -r requirements

2. Загрузите Selenium WebDriver с https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим)

3. Запустить тесты:

pytest --driver Chrome  --alluredir results
