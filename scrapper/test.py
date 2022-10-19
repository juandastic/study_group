import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def executeTest():
    global driver
    open_url(driver)
    close_statguide_modal(driver)
    # open_invesment_type_filter(driver)
    # select_invesment_type_option(driver)
    # select_price_range_min(driver)
    time.sleep(3)
    find_and_click_cta(driver)
    # apply_filters(driver)
    # print(element)
    # element.click()
    # element.send_keys("MDE", Keys.ENTER)
    time.sleep(3)

def open_url(driver):
    driver.get('http://lahausdev.com:3000/invertir-bienes-raices?investment_type=short_term&price=200:400')

def close_statguide_modal(driver):
    element = driver.find_element(By.CSS_SELECTOR, ".start_guide_modal #close")
    element.click()

def open_invesment_type_filter(driver):
    element = driver.find_element(By.CSS_SELECTOR, "#inversion_type")
    element.click()

def select_invesment_type_option(driver):
    element = driver.find_element(By.CSS_SELECTOR, "label[for='short_term']")
    element.click()

def select_price_range_min(driver):
    element = driver.find_element(By.CSS_SELECTOR, "#PriceFilter .roomie-dropdown")
    element.click()

def apply_filters(driver):
    element = driver.find_element(By.CSS_SELECTOR, "#aplly_filter")
    element.click()

def find_and_click_cta(driver):
    element = driver.find_element(By.CSS_SELECTOR, "p[title='TORRECHIARA']")
    card_element = element.find_element(By.XPATH, "../../../../../..")
    cta = card_element.find_element(By.CSS_SELECTOR, "#advisory")
    cta.click()


def startWebDriver():
    global driver
    options = Options()
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome('/Users/juandavidgomez/chromedriver/chromedriver', chrome_options=options)

if __name__ == "__main__":
    startWebDriver()
    executeTest()
    driver.quit()