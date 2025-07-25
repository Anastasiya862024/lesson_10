from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CalcPage:

    def __init__(self, driver):
        """
        Конструктор класса calc_page.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.result_locator = (By.ID, "result")

    @allure.step("Установка задержки 45 секунд")
    def enter_delay(self):
        """
        Устанавливает задержку для выполнения операций на калькуляторе.
        """
        input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        input.clear()
        input.send_keys("45")

    @allure.step("Нажатие на кнопки '7' '+' '8' '=' на калькуляторе")
    def click_button(self):
        """
        Нажимает на кнопку калькулятора.
        """
        button = self.driver.find_element(By.XPATH, '//span[text()="7"]')
        button.click()
        button = self.driver.find_element(By.XPATH, '//span[text()="+"]')
        button.click()
        button = self.driver.find_element(By.XPATH, '//span[text()="8"]')
        button.click()
        button = self.driver.find_element(By.XPATH, '//span[text()="="]')
        button.click()

    @allure.step("Ожидание и получение результата с экрана калькулятора")
    def get_result(self):
        """
        Ожидает появления ожидаемого результата на экране калькулятора.
        """
        WebDriverWait(self.driver, 60).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".screen"))
        )
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".screen"), "15")
        )

        """
        Возвращает текущий результат с экрана калькулятора.

        :res: str — текст результата на экране калькулятора.
        """
        res = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return res
