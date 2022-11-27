from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def getscurl(url):
    chrome_options=Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")

    driver=webdriver.Chrome("D:\pythonProject1\venv\chromedriver.exe",options=chrome_options)
    driver.get(url)
    time.sleep(2)

    email_element = driver.find_element('id', 'userid')
    user_id='09345096'
    user_pass='Whyy!1122'
    email_element.send_keys(user_id)  # Give keyboard input

    password_element = driver.find_element('id', 'password')
    password_element.send_keys(user_pass)  # Give password as input too

    login_button = driver.find_element('id', 'submit')
    login_button.click()  # Send mouse click


    time.sleep(10)
    #element=driver.find_element("xpath","/html/body")
    element = driver.find_element("xpath", "/html/frameset")
    width=1928
    height=element.size["height"]+1000
    driver.set_window_size(width,height)
    time.sleep(5)
    driver.save_screenshot("B.png")
    driver.quit()


getscurl("https://pepsicodocumentmanagement.pepsico.com/")

