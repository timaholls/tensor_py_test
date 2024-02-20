from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from driver import driver_brow

HANDLES = driver_brow.window_handles
ENTER = Keys.ENTER
WAIT = WebDriverWait(driver_brow, 15)
