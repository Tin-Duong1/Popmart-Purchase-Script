import time
import random
import selenium
from selenium_stealth import stealth
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_profile_path = r"/Users/tinduong/Library/Application Support/Google/Chrome" 
profile_directory = "Profile 3"  

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(f"--user-data-dir={chrome_profile_path}")
chrome_options.add_argument(f"--profile-directory={profile_directory}")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize the WebDriver with the Chrome options and executable path
driver = webdriver.Chrome(options=chrome_options)

totalClock = 0
requestTime = 3600


stealth(driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True)

driver.get("https://www.popmart.com/us/largeShoppingCart")

# Explicit wait
wait = WebDriverWait(driver, 20)

checked = False
while True:
    try:
        checkBox = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "index_checkbox__w_166")))
        checkBox.click()
        time.sleep(0.5)  # Wait for the click action to take effect
        if "index_checkboxActive__LAaYV" in checkBox.get_attribute("class"):
            checked = True
        else:
            continue
    except selenium.common.exceptions.TimeoutException:
        break
    except selenium.common.exceptions.StaleElementReferenceException:
        break
    except selenium.common.exceptions.NoSuchElementException:
        break


try:
    #button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div[3]/button')))
    button = driver.find_element(By.XPATH, '//*[@id="rc-tabs-0-panel-1"]/div/div[2]/div/div[3]/button')
    button.click()
    print("Element clicked successfully.")
except selenium.common.exceptions.TimeoutException:
    print("Element not found or not clickable.")
except selenium.common.exceptions.NoSuchElementException:
    print("Element not found.")
except selenium.common.exceptions.ElementClickInterceptedException:
    print("Element not clickable due to being obscured by another element.")
except Exception as e:
    print(f"An error occurred: {e}")

billingClick = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div[1]/div/div[6]/div[2]/span')))
billingClick.click()

addressClick = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'addressItem_tel__kIwwB')))    
addressClick.click()

time.sleep(0.3)

creditCardClick = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[1]/div[1]/div/div[8]/div[2]/div[1]')))

creditCardClick.click()



time.sleep(6000)


