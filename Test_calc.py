import pytest
from selenium import webdriver
from Calc_page import calc_page
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@allure.title("Тестирование калькулятора:  7 + 8 = 15")
@allure.description("Тест проверяет корректность работу калькулятора")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_calculator(driver):
    """
    Тест проверяет работу калькулятора
    """
    with allure.step("Открытие страницы калькулятора"):
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        calculator = calc_page(driver)
    with allure.step("Установка задержки 45 секунд"):
        calculator.enter_delay()
    with allure.step("Нажатие кнопок: '7' '+' '8' '='"):
        calculator.click_button()
    with allure.step("Ожидание результата"):
        result = calculator.get_result()
    with allure.step("Проверка результата"):
        assert result == "15"
