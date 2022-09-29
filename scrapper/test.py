import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

def executeTest():
    global driver
    driver.get('http://www.sciencedirect.com/science/article/pii/S2211926417300024')
    time.sleep(7)
    element = driver.find_element(By.CSS_SELECTOR, "#preview-section-snippets-item a")
    print(element)
    element.click()
    time.sleep(3)

def startWebDriver():
    global driver
    options = Options()
    options.add_argument("--disable-infobars")
    driver = webdriver.Chrome('/Users/juandavidgomez/chromedriver/chromedriver', chrome_options=options)

if __name__ == "__main__":
    startWebDriver()
    executeTest()
    driver.quit()