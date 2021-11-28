import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:53758")
#Change chrome driver path accordingly
chrome_driver = "chromedriver.exe"
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
driver.implicitly_wait(0.5)
print(driver.command_executor._url)
print(driver.session_id)
time.sleep(100)
driver.get("chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html")
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.LINK_TEXT, "Best Location"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[text()=' Germany  ']"))).click()
#chrome.exe --remote-debugging-port=9222 --user-data-dir=C:\Users\Nouman\Downloads\Compressed\chromedriver_win32\ChromeData