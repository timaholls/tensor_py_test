from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.conts import *

class Tensor_about_page:
    def __init__(self, driver):
        self.driver = driver
        

    def check_vlog_working_title(self):
        """ Проверка названия блога Работаем"""
        # прокрутка до места, где блог
        element = WAIT.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, 'div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3')))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # находим блог Работаем
        vlog_title_element = WAIT.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.tensor_ru-container.tensor_ru-section.tensor_ru-About__block3 > div.tensor_ru-About__block-title-block > h2.tensor_ru-header-h2.tensor_ru-About__block-title")))
        return vlog_title_element.text.lower()

    def working(self):
        """ Проверка блога 'работаем' """
        # находим в блоге все фотографии по селектору и проверяем ширину и высоту
        photos = WAIT.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.tensor_ru-About__block3-image.new_lazy.loaded')))
        return photos

