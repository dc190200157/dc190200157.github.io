import random
import time
import sys
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
def check_exists_by_css(css):
    try:
        driver.find_element_by_css_selector(css)
    except NoSuchElementException:
        return False
    return True
countries=["//*[text()=' Germany  ']","//*[text()=' Romania  ']","//*[text()=' Singapore  ']","//*[text()=' United States  ']"]
current_space = '::'
data=open('Links.txt','r').read()
d_lines = data.splitlines()
counts=0
with open("Stamps.txt", "w") as text_file:
  text_file.write(str(counts))
for x in range(1,4):
  for line in d_lines:
   if current_space not in line:
        if line.strip():
            coun=random.choice(countries)
            print(coun)
            print(line)
            chrome_options = Options() 
            chrome_options.add_experimental_option("detach", True)
            chrome_options.add_extension('8.0.4.0_0.crx')
            chrome_options.add_extension('4.1.2_0.crx')
            driver = webdriver.Chrome(options=chrome_options)
            driver.maximize_window()
            wait = WebDriverWait(driver, 3)
            presence = EC.presence_of_element_located
            visible = EC.visibility_of_element_located
            actions = webdriver.ActionChains(driver)
            print(driver.command_executor._url)
            print(driver.session_id)
            time.sleep(1)
            driver.get("https://account.zenmate.com/en_US/login?redirectTo=/en_US/devices") 
            driver.minimize_window()  
            driver.maximize_window()  
            driver.minimize_window()  
            driver.maximize_window()  
            time.sleep(1)
            curr=driver.current_window_handle
            for handle in driver.window_handles:
              driver.switch_to.window(handle)
              if handle != curr:
                driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
            if check_exists_by_css("#username"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']"))).send_keys("mnoumanhanif.66@gmail.com")
            time.sleep(2)
            if check_exists_by_css("#password"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))).send_keys("Nouman@786AA")
              time.sleep(3)
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//label[normalize-space()='Keep me logged in']"))).click()
              time.sleep(3)
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='login-btn']/button"))).click()
            time.sleep(100)
            driver.get("chrome-extension://fdcgdnkidjaadafnichfpabhfomcebme/index.html") 
            time.sleep(1)
            WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/1.png']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/2.png']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/3.png']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//img[@src='assets/imgs/onboarding/en/4.png']"))).click()
            time.sleep(1)
            WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.LINK_TEXT, "Best Location"))).click()
            time.sleep(1)
            WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, coun))).click()
            driver.implicitly_wait(3)
            driver.get(line)
            time.sleep(1)
            if check_exists_by_css("#button[aria-label='Agree to the use of cookies and other data for the purposes described']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//yt-formatted-string[normalize-space()='I Agree']"))).click()
            driver.implicitly_wait(7)
            if check_exists_by_css(".ytp-ad-preview-container.countdown-next-to-thumbnail"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ytp-ad-skip-button ytp-button']"))).click()
            time.sleep(1)
            if check_exists_by_css("ytd-button-renderer[id='dismiss-button'] yt-formatted-string[id='text']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//ytd-button-renderer[@id='dismiss-button']//yt-formatted-string[@id='text']"))).click()
            time.sleep(1)
            actions.send_keys("m")
            actions.perform()
            time.sleep(1)
            if check_exists_by_css("div[class='ytp-left-controls'] button[aria-label='Play (k)']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ytp-left-controls']//button[@aria-label='Play (k)']"))).click()
            #if check_exists_by_css(".ytp-autonav-toggle-button"):
              #WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ytp-autonav-toggle-button-container']"))).click()
            if check_exists_by_css("#button[aria-label='Loop playlist']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Loop playlist']"))).click()
            if check_exists_by_css("#button[aria-label='Shuffle playlist']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[@aria-label='Shuffle playlist']"))).click()
            time.sleep(5)
            time.sleep(1)
            actions.send_keys("m")
            actions.perform()
            if check_exists_by_css("button[title='Settings']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Settings']"))).click()
            if check_exists_by_css("div[role='menu'] div:nth-child(1) div:nth-child(2)"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Playback speed']"))).click()
              time.sleep(1)
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//*[text()='1.25']"))).click()
            actions.send_keys("m"*2)
            actions.perform()
            if check_exists_by_css("button[title='Settings']"):
              WebDriverWait(driver, 70).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Settings']"))).click()
            counts+=1
            with open("Stamps.txt", "w") as text_file:
              text_file.write(str(counts))
            with open('Stamps.txt', 'r') as file:
              countes=file.read()
              if int(countes)==2:
                sys.exit(0)
            if counts==2:
              sys.exit(0)
            """
            driver.switch_to.window(driver.window_handles[0])
            driver.switch_to.window(driver.window_handles[0])
            driver.close()

            browser.execute_script("window.open('about:blank', 'tab2');")
            driver.switch_to.default_content()
            #actions.key_down(Keys.CONTROL).send_keys("w").key_up().perform()
            #actions.key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.switch_to.window(driver.current_window_handle)
            """