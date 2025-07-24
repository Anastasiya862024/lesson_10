import pytest
from selenium import webdriver
from Shop_page import shop_page
import allure


@pytest.fixture
def browser():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    browser = webdriver.Edge()
    browser.maximize_window()
    yield browser
    browser.quit()


@allure.title("Тестирование интернет магазина")
@allure.description("Тест проверяет корректность работу интернет магазина")
@allure.feature("Интернет магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop(browser):
    """
    Тест проверяет работу интернет магазина.
    """
    with allure.step("Открытие страницы интернет магазина"):
        browser.get("https://www.saucedemo.com/")
        shop = shop_page(browser)
    with allure.step("Авторизация на сайте"):
        shop.authorization()
    with allure.step("Добавление товаров в корзину"):
        shop.home_page()
    with allure.step("Переход в корзину товаров"):
        shop.cart_product()
    with allure.step("Заполнение данных"):
        shop.registration()
    with allure.step("Получение итоговой суммы покупки"):
        result = shop.get_result()
    with allure.step("Проверка результата"):
        assert result == 58.29, f"Итоговая сумма \
            должна быть 58.29, но получена {result}"
