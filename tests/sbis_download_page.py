import os
import shutil
import time


class Sbis_download_page:

    def __init__(self, driver):
        self.driver = driver

    def plugin_button(self):
        """Переход по кнопке в раздел 'Скачать плагин' скачивания плагина """
        # ищем нужную кнопку
        bt_go_download_chapter = self.driver.execute_script("return document.querySelector('[data-id=\"plugin\"]');")
        assert bt_go_download_chapter, f"Ошибка: раздел 'Скачать плагин' не найдена "
        return bt_go_download_chapter

    def download_plugin(self):
        """Скачиваем плагин"""
        # ищем нужную кнопку
        # path = 'div.sbis_ru-DownloadNew-loadLink__link.js-link'

        bt_download = self.driver.execute_script(
            "return document.querySelector('a[href=\"https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe\"]');")
        return bt_download

    def check_file_to_download_and_move(self):
        # Ожидание завершения загрузки файла
        source_path = os.path.join(r"C:\Users\HP\Downloads\sbisplugin-setup-web.exe")
        timeout = 60  # таймаут ожидания в секундах
        start_time = time.time()
        while not os.path.exists(source_path) or os.path.getsize(source_path) == 0:
            if time.time() - start_time > timeout:
                return False
            time.sleep(1)
        # перемещение плагина в папку с проектом
        destination_folder = r"C:\Users\HP\PycharmProjects\tensor_py_test"
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # Перемещение файла
        shutil.move(source_path, destination_folder)
        return True

    def checking_the_size(self, file_size):
        """Проверка размера скаченного плагина"""
        time.sleep(5)
        expected_filename = "sbisplugin-setup-web.exe"
        expected_path = r"C:\Users\HP\PycharmProjects\tensor_py_test\sbisplugin-setup-web.exe"

        full_path = os.path.join(expected_path)

        if os.path.exists(full_path):
            # Получаем размер файла в мегабайтах
            file_size_mb = round(float(os.path.getsize(full_path) / (1024 * 1024)), 2)
            if file_size_mb == float(file_size):
                return True
            else:
                return False
        else:
            assert f"Ошибка: Файл '{expected_filename}' не найден по пути '{expected_path}'."
