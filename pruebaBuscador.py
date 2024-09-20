from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
import webbrowser

def buscar(buscar):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('http://www.google.com')


    search_bar = driver.find_element(By.NAME, 'q')
    search_bar.send_keys(buscar)
    search_bar.send_keys(Keys.RETURN)


    time.sleep(2)


    first_result = driver.find_element(By.CSS_SELECTOR, 'div.g')
    first_link = first_result.find_element(By.TAG_NAME, 'a')
    first_link.click()
    time.sleep(2)

    # Recoge el enlace de la página actual
    webbrowser.open(driver.current_url)

