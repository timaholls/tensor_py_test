from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.conts import *


class Sbis_contact_page:

    def __init__(self, driver):
        self.driver = driver

    def checking_url_contact_page(self):
        """Проверка url, что мы перешли в раздел контакты"""
        current_url = self.driver.current_url
        return current_url

    def find_tensor_banner(self):
        """Поиск баннера tensor"""
        tensor_banner = WAIT.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor.mb-12')))
        return tensor_banner

    def checking_the_region(self, region):
        """Проверка региона"""
        # ищем поле с регионом
        regoin_field = WAIT.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text.sbis_ru-link')))
        # проверка соответствия названия региона
        if regoin_field.text.lower() == region:
            return True
        else:
            return regoin_field

    def checking_city_before_the_list(self, city):
        """Проверка города перед списком партнеров"""
        # ищем название город перед списком партнеров
        regoin_field = WAIT.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '#city-id-2')))

        # проверка соответствия города Уфа в нашем случаи
        regoin_field_title = regoin_field.text.lower()
        if regoin_field_title == city.lower():
            return True
        else:
            return regoin_field_title

    def checking_list_of_partners(self):
        """Поиск списка партнеров"""
        # ищем список партнеров
        list_of_partners = WAIT.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.sbisru-Contacts-List__address.sbisru-Contacts-List--ellipsis.sbisru-text-small.sbisru-Contacts__relative > div.sbisru-Contacts-List--ellipsis')))
        return list_of_partners

    def find_the_region_field(self):
        # нажатие на регион для всплытия списка со всеми регионами
        regoin_field = WAIT.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '.sbis_ru-Region-Chooser__text.sbis_ru-link')))
        return regoin_field

    def find_the_kamchat_field(self):
        # нажатие на кнопку в списке регионов
        kamchat_field = WAIT.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]')))
        return kamchat_field