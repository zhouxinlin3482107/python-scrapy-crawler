from selenium import webdriver
import time

def sleep(seconds):
    time.sleep(seconds)

def create_chrome_driver():
    options = webdriver.ChromeOptions()
    # 浏览器开着方便调试
    # options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(chrome_options=options)
    driver.maximize_window()
    return driver

def find_element_by_css_selector(driver, selector):
    try:
        return driver.find_element_by_css_selector(selector)
    except:
        return None

def find_elements_by_css_selector(driver, selector):
    try:
        return driver.find_elements_by_css_selector(selector)
    except:
        return []