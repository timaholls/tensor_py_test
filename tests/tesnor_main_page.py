from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.conts import *

class Tensor_main_page:
    def __init__(self, driver):
        self.driver = driver

    def switch_page(self):
        """Код для переключения на вторую вкладку
        (Я использую Google Chrome и так как он открывает ссылки в новой вкладке, требуется переход)"""
        # получаем все вкладки
        current_handle = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        found_new_page = False
        for handle in all_handles:
            if handle != current_handle:
                self.driver.switch_to.window(handle)
                found_new_page = True
                break
        return found_new_page

    def check_vlog_title(self):
        """Проверка названия"""
        # прокрутка до места, где блог
        element = WAIT.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.tensor_ru-Index__block4')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        vlog_title_element = WAIT.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                               "div.tensor_ru-Index__block4-content.tensor_ru-Index__card > p.tensor_ru-Index__card-title.tensor_ru-pb-16")))
        return vlog_title_element

    def more_detailed(self):
        """ Клик по кнопке 'подробнее' в блоге 'сила в людях' """
        # нажимаем на кнопку 'подробнее'
        detailed_element = WAIT.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content.tensor_ru-Index__card "
                              "> p.tensor_ru-Index__card-text > a.tensor_ru-link.tensor_ru-Index__link")))
        return detailed_element

        # # проверяем название кнопки на правильность
        # css_path_bt = "div.tensor_ru-Index__block4-content.tensor_ru-Index__card > p.tensor_ru-Index__card-text > a.tensor_ru-link.tensor_ru-Index__link"
        # detailed_element = WAIT.until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_path_bt)))
        # assert detailed_element.text.lower() == 'подробнее', "кнопка называется по другому"
