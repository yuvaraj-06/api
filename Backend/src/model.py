from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def mine_data(email,password):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path="chromedriver.exe", chrome_options=options)
    email =email
    password =password
    driver.get('https://www.linkedin.com/login')
    time.sleep(3)
    driver.find_element_by_id('username').send_keys(email)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('password').send_keys(Keys.RETURN)
    driver.get("https://www.linkedin.com/my-items/saved-jobs/")
    time.sleep(3)
    x=driver.find_elements(by=By.CLASS_NAME,value="entity-result__item")
    #x = driver.find_elements_by_class_name()
    d=dict()
    c=1
    for each in x:
        d[c]=each.text.split("\n")
        c=c+1
    print(d)
    return d 