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
chrome_options.add_experimental_option("detach", True)
chrome_options.add_extension('8.0.4.0_0.crx')
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
wait = WebDriverWait(driver, 3)
presence = EC.presence_of_element_located
visible = EC.visibility_of_element_located
#driver.get("chrome-extension://omghfjlpggmjjaagoclmmobgdodcjboh/popup/popup.html")
driver.get("chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html")
"""
driver.current_url
driver.implicitly_wait(0.5)
driver.execute_script('window.open("https://www.youtube.com/watch?v=XmsQ3LjSNF8/");')
driver.switch_to(driver.window_handles[0])

WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.LINK_TEXT, "LOGIN"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "userName"))).send_keys("mnouman.hanif66@gmail.com")
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "userPass"))).send_keys("492167aa")
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "btnLogin"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "btnAction"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.LINK_TEXT, "Select Country"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.ID, "srchCountryField"))).send_keys("United States")
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='countriesList']/li[28]/a"))).click()
"""
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/1.png']"))).click()
time.sleep(0.5)
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/2.png']"))).click()
time.sleep(0.5)
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/3.png']"))).click()
time.sleep(0.5)
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/4.png']"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.LINK_TEXT, "Best Location"))).click()
WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[text()=' Germany  ']"))).click()