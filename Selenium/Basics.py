from selenium.webdriver import Chrome, Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = 'https://www.google.com/'
driver_path = "D:\Selenium\venv\msedgedriver.exe"


browser = Edge(executable_path="driver_path")
browser.get(url)

input_search='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'
search_obj = browser.find_element(By.XPATH, input_search)
search_obj.clear()
search_obj.send_keys('Manchala Bhuvanachandra')
search_obj.send_keys(Keys.ENTER)


# Window Navigation

"""
    Refresh, Go Back, Go Forward
"""
browser.refresh()
browser.back()
browser.forward()
"""
Minimize Window, Maximize Window, Restore Window
"""
w, h = browser.get_window_size().values()
browser.maximize_window()
browser.minimize_window()
browser.set_window_size(w, h)

"""
ActionChains class

ActionChains class to simulate different mouse and keyboard commands.

"""
from selenium.webdriver import ActionChains
action_chains = ActionChains(browser)
#action_chains.key_down(Keys.CONTROL).send_keys('V').key_up( Keys.CONTROL).perform()  # ctrl v chesi perform() chesthunnam if we not do perform It will not performed any action

x_path_string= '//*[@id="rso"]/div[1]/div/div/div[1]/div/a/h3'
element = browser.find_element(By.XPATH, x_path_string)
action_chains.move_to_element(element).click().perform()  # mouse tho Bhuvanachandra nu clickng


while(True):
       pass
