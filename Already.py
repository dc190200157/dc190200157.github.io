import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
def check_exists_by_xpath(css):
    try:
        driver.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
#Change chrome driver path accordingly
#chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome("chromedriver.exe", chrome_options=chrome_options)
#driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
driver.implicitly_wait(0.5)
driver.get("https://www.youtube.com/")
time.sleep(10)
#WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.LINK_TEXT, "Best Location"))).click()
if check_exists_by_xpath("#button[aria-label='Agree to the use of cookies and other data for the purposes described']"):
    WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[normalize-space()='I Agree']"))).click()
#chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\Users\Nouman\Downloads\Compressed\chromedriver_win32\ChromeData