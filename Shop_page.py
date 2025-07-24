from selenium.webdriver.common.by import By
import allure


class shop_page:

    def __init__(self, browser):
        """
        Конструктор класса shop_page

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.browser = browser

    @allure.step("Авторизация на сайте")
    def authorization(self):
        """
        Авторизуется на сайте с указанными именем пользователя и паролем.
        """
        username_input = self.browser.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        password_input = self.browser.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        login_button = self.browser.find_element(By.ID, "login-button")
        login_button.click()

    @allure.step("Добавление товара в корзину")
    def home_page(self):
        """
        Добавляет указанные товары в корзину.
        """
        backpack_button = self.browser.find_element(
            By.XPATH, "//div[@class='inventory_item' and \
                .//div[contains(text(), 'Sauce Labs Backpack')]]//button")
        backpack_button.click()
        tshirt_button = self.browser.find_element(
            By.XPATH, "//div[@class='inventory_item' and \
                .//div[contains(text(), 'Sauce Labs Bolt T-Shirt')]]//button")
        tshirt_button.click()
        onesie_button = self.browser.find_element(
            By.XPATH, "//div[@class='inventory_item' and \
                .//div[contains(text(), 'Sauce Labs Onesie')]]//button")
        onesie_button.click()
        cart_link = self.browser.find_element(
            By.CLASS_NAME, "shopping_cart_link")
        cart_link.click()

    @allure.step("Переход в корзину товаров")
    def cart_product(self):
        """
        Нажинамает на кнопку перехода в корзину.
        """
        checkout_button = self.browser.find_element(By.ID, "checkout")
        checkout_button.click()

    @allure.step("Заполнение данных")
    def registration(self):
        """
        Заполняет данные для оформления покупки.
        """
        first_name_input = self.browser.find_element(By.ID, "first-name")
        first_name_input.send_keys("Анастасия")
        last_name_input = self.browser.find_element(By.ID, "last-name")
        last_name_input.send_keys("Иванова")
        postal_code_input = self.browser.find_element(By.ID, "postal-code")
        postal_code_input.send_keys("987654")
        continue_button = self.browser.find_element(By.ID, "continue")
        continue_button.click()

    @allure.step("Полечение итоговой суммы покупки")
    def get_result(self):
        """
        Получает и возвращает итоговую сумму покупки.
        """
        total_cost = self.browser.find_element(
            By.CLASS_NAME, "summary_total_label").text
        total_cost_value = float(total_cost.split("$")[1])
        return total_cost_value
