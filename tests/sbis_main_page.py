from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.conts import *


class Sbis_main_page:
    def __init__(self, driver):
        self.driver = driver

    def open_sbis_main_page(self):
        """Переход на сбис"""
        self.driver.get("https://sbis.ru/")
        return self.driver.current_url

    def find_contacts_botton(self):
        """Поиск кнопки 'Контакты' """
        # ищем нужную нам кнопку
        bt_contacts = WAIT.until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]')))
        return bt_contacts

    def click_go_to_download_page(self):
        """Проверка кнопки 'скачать локальные файлы'('Скачать СБИС') и ее нажатие"""
        # прокрутка до footer
        element = WAIT.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.sbisru-Footer.sbisru-Footer__scheme--default')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # ищем нужную кнопку в footer
        bt_go_download_page = WAIT.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]')))
        return bt_go_download_page
