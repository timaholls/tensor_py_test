import time
import pytest
from driver import driver_brow
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
from tests.sbis_download_page import Sbis_download_page
from tests.sbis_main_page import Sbis_main_page
from tests.sbis_contact_page import Sbis_contact_page
from tests.tesnor_main_page import Tensor_main_page
from tests.tensor_about_page import Tensor_about_page
import allure


# Инициализация драйвера
@pytest.fixture(scope="session")
def browser(request):
    driver = driver_brow
    yield driver
    if hasattr(request.node, 'result') and request.node.result:
        if request.node.result.failed:
            driver.save_screenshot(request.node.name + ".png")


# Фикстура для инициализации страниц
@pytest.fixture(scope="session")
def initialized_pages(browser):
    sbis_main_page = Sbis_main_page(browser)
    sbis_contact_page = Sbis_contact_page(browser)
    tensor_main_page = Tensor_main_page(browser)
    tensor_about_page = Tensor_about_page(browser)

    return sbis_main_page, sbis_contact_page, tensor_main_page, tensor_about_page


# Тест первого сценария
@allure.step("Запуск первого сценария")
def test_tensor_search_1(browser, initialized_pages):
    script_1, script_2, script_3, script_4 = initialized_pages
    with allure.step("Шаг 1: переход на https://sbis.ru/"):
        # открытие страницы, возвращается url
        url_sbis_main_page = script_1.open_sbis_main_page()
        assert url_sbis_main_page == 'https://sbis.ru/', f'url не соответствует, получено {url_sbis_main_page}'

    with allure.step("Шаг 2: Поиск кнопки и переход в раздел Контакты"):
        # открытие страницы, возвращается кнопка
        contacts_button = script_1.find_contacts_botton()
        assert contacts_button, "Ошибка: кнопка Контакты не найдена"
        bt_contacts_title = contacts_button.text.lower()
        assert bt_contacts_title == 'контакты'.lower(), f"Ошибка: кнопка существует, но название не соответствует, получено: {bt_contacts_title}"
        # кликаем на кнопку для перехода в раздел Контакты
        contacts_button.click()

    with allure.step("Шаг 3: Поиск баннера в разделе контакты и клик по нему"):
        # проверка url раздела контакты
        expected_url = "https://sbis.ru/contacts"
        current_url = script_2.checking_url_contact_page()
        assert current_url == expected_url or current_url == 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients', \
            f'Ошибка: URL вкладки ({current_url}) не совпадает ни с одним из ожидаемых URL'

        # открытие раздела контакты, возвращается найденный баннер
        tensor_banner = script_2.find_tensor_banner()
        assert tensor_banner, "Ошибка: баннер Тензор не найден"
        # кликаем на баннер
        tensor_banner.click()

    with allure.step("Шаг 4: Проверить, что есть блок 'Сила в людях' "):
        # Получаем список всех вкладок после открытия новой ссылки
        all_handles = browser.window_handles
        # Переключаемся на последнюю вкладку в списке (которая должна быть новой вкладкой)
        browser.switch_to.window(all_handles[-1])
        # Проверка названия блока
        blog_title = script_3.check_vlog_title()
        assert blog_title.text.lower() == 'сила в людях', f"Ошибка: Название блога не совпадает или блог не найден, получено: {blog_title}"

    with allure.step("Шаг 5: Перейти в этом блоке в 'Подробнее' и убедитесь, что открывается 'https://tensor.ru/about'"):
        more_details_button = script_3.more_detailed()
        assert more_details_button, "Ошибка: кнопка 'Подробнее' не найдена"
        more_details_button.click()
        WebDriverWait(browser, 10).until(EC.url_contains("https://tensor.ru/about"))
        assert browser.current_url == 'https://tensor.ru/about', f"Ошибка: URL не соответствует ожидаемому, получено {browser.current_url}"

    with allure.step("Шаг 6: Находим раздел 'Работаем' и проверяем, что у всех фотографий хронологии одинаковые height и width"):
        # Проверяем название блока
        title_vlog = script_4.check_vlog_working_title()
        assert title_vlog == "работаем", f"Ошибка: Название блока не совпадает или блог не найде, получено: {title_vlog}"

        # Получаем список с фотографиями
        photos = script_4.working()
        assert photos, "Ошибка: Фотографии не найдены!"

        # Проверяем, что у всех фотографий одинаковые размеры
        if len(photos) > 1:
            first_photo = photos[0]
            expected_width = first_photo.size['width']
            expected_height = first_photo.size['height']

            for i, photo in enumerate(photos[1:], start=2):
                assert photo.size[
                           'width'] == expected_width, f"Ошибка: Ширина фотографии {i} не соответствует ожидаемой ({expected_width})"
                assert photo.size[
                           'height'] == expected_height, f"Ошибка: Высота фотографии {i} не соответствует ожидаемой ({expected_height})"


# Тест второго сценария
@allure.step("Запуск второго сценария")
def test_tensor_search_2(browser, initialized_pages):
    script_1, script_2, script_3, script_4 = initialized_pages
    with allure.step("Шаг 1: Перейти на https://sbis.ru/ в раздел 'Контакты' "):
        # открытие страницы, возвращается url
        url_sbis_main_page = script_1.open_sbis_main_page()
        WebDriverWait(browser, 10).until(EC.url_contains("https://sbis.ru/"))
        assert url_sbis_main_page == 'https://sbis.ru/', f'url не соответствует, получено {url_sbis_main_page}'

    with allure.step("Шаг 2: Поиск кнопки и переход в раздел Контакты"):
        # открытие страницы, возвращается кнопка
        contacts_button = script_1.find_contacts_botton()
        assert contacts_button, "Ошибка: кнопка 'Контакты' не найдена"
        bt_contacts_title = contacts_button.text.lower()
        assert bt_contacts_title == 'контакты'.lower(), f"Ошибка: кнопка существует, но название не соответствует, получено: {bt_contacts_title}"
        # кликаем на кнопку для перехода в раздел Контакты
        contacts_button.click()

    with allure.step("Шаг 3: Проверить, что определился ваш регион (в нашем случаи рес. Башкор.) и есть список партнеров"):
        WebDriverWait(browser, 10).until(
            EC.url_contains("https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients"))

        # проверка текущего региона (Республика Башкортостан) в url
        correct__url_reg_bash = script_2.checking_url_contact_page()
        assert correct__url_reg_bash == 'https://sbis.ru/contacts/02-respublika-bashkortostan?tab=clients', f'Ошибка: url не соотвествует текущему региону, получено {correct__url_reg_bash}'

        # проверка текущего региона (Республика Башкортостан)
        region_bash = script_2.checking_the_region('республика башкортостан')
        assert region_bash, f'Ошибка: Регион не соотвествует текущему, получено {region_bash}'

        # проверка город перед списком партнеров (Уфа)
        city_bash = script_2.checking_city_before_the_list('Уфа')
        assert city_bash, f'Ошибка: Город не соотвествует ожидаемому - Уфа'

        # проверка наличия списка партнеров
        partner_bash = script_2.checking_list_of_partners()
        assert partner_bash or len(
            partner_bash) <= 0, f"Ошибка: список партнеров найден или партнеров в этом регионе нет"

    with allure.step("Шаг 4: Изменить регион на Камчатский край"):
        # нахождение кнокпи для смены региона и клик
        region_field = script_2.find_the_region_field()
        assert region_field, f"Ошибка: поле с регионом не найден"
        region_field.click()

        # нахождение камчатки в списке всплывающего окна со всеми регионами
        time.sleep(2)
        kamchat_field = script_2.find_the_kamchat_field()
        assert kamchat_field, f"Ошибка: кнопка с Камчатским краем не найден"
        kamchat_field.click()
        # Явное ожидание конца загрузки страницы
        WebDriverWait(browser, 10).until(EC.url_contains("https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"))

        # проверка текущего региона (Камчатский край) в url
        correct__url_reg_bash = script_2.checking_url_contact_page()
        assert correct__url_reg_bash == 'https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients', f'Ошибка: url не соотвествует текущему региону, получено {correct__url_reg_bash}'

        # проверка город перед списком партнеров (Петропавловск-Камчатский)
        city_bash = script_2.checking_city_before_the_list('Петропавловск-Камчатский')
        assert region_bash, f'Ошибка: Город не соотвествует, получено {city_bash}'

        # проверка наличия списка партнеров
        partner_bash = script_2.checking_list_of_partners()
        assert partner_bash or len(
            partner_bash) <= 0, f"Ошибка: список партнеров найден или партнеров в этом регионе нет"


# Тест третьего сценария
@allure.step("Запуск третьего сценария")
def test_tensor_search_3(browser, initialized_pages):
    file_size = None
    script_1, script_2, script_3, script_4 = initialized_pages
    script_5 = Sbis_download_page(browser)

    with allure.step("Шаг 1: Перейти на https://sbis.ru/"):

        # открытие страницы, возвращается url
        url_sbis_main_page = script_1.open_sbis_main_page()
        WebDriverWait(browser, 10).until(EC.url_contains("https://sbis.ru/"))
        assert url_sbis_main_page == 'https://sbis.ru/', f'url не соответствует, получено {url_sbis_main_page}'

    with allure.step("Шаг 2: В Footer'e найти и перейти 'Скачать СБИС'"):
        # поиск кнопки в Footer'е
        bt_to_download_page = script_1.click_go_to_download_page()
        assert bt_to_download_page, f"Ошибка: кнопка не существует"

        # проверяем название кнопки
        bt_go_download_page_title = bt_to_download_page.text.lower()

        """В задании указано, что кнопка называется 'Скачать СБИС', но в действительности 'скачать локальные версии' """
        assert bt_go_download_page_title == f'скачать локальные версии', f"Ошибка: название кнопки не соответствует, она - {bt_go_download_page_title}"

        # нажимаем для перехода
        bt_to_download_page.click()

    with allure.step("Шаг 3: Скачать СБИС Плагин для вашей для windows, веб-установщик в папку с данным тестом"):
        # ожидание страницы с локальными файлами
        WebDriverWait(browser, 10).until(EC.url_contains("https://sbis.ru/download?tab=ereport&innerTab=ereport25"))

        # поиск кнопки СБИС плагин
        bt_go_download_chapter = script_5.plugin_button()

        # нажатие на нее
        bt_go_download_chapter.click()

        # ожидание перехода в подраздел
        WebDriverWait(browser, 10).until(EC.url_contains("https://sbis.ru/download?tab=plugin&innerTab=default"))

        # поиск кнопки для скачивания и клик по нему
        bt_download = script_5.download_plugin()
        assert bt_download, f"Ошибка: кнопка 'Скачать' не найдена "
        bt_download.click()

        # поиск размера файла
        bt_download_title = bt_download.text.lower()
        size = re.search(r'\d+\.\d+', str(bt_download_title))
        file_size = float(size.group())

    with allure.step("Шаг 4: Убедиться что плагин скачался"):
        file_check = script_5.check_file_to_download_and_move()
        assert file_check, "Ошибка файл не скачен или не переместился в папку проекта"

    with allure.step("Шаг 5: Сравнить размер скачанного файла в мегабайтах. Он должен совпадать с указанным на сайте"):
        size_check = script_5.checking_the_size(file_size=file_size)
        assert size_check, "Ошибка: Размер файла не совпадает с ожидаемым"
