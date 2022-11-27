from ast import Pass
from selenium.webdriver import Chrome, Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url="https://jenniferdewalt.com/click_challenge.html"
 # How many times can you click in 30 Seconds?
driver_path = "D:\Selenium\venv\msedgedriver.exe"


browser = Edge(executable_path="driver_path")
browser.get(url)
from selenium.webdriver import ActionChains
action_chains = ActionChains(browser)
browser.find_element(By.ID, "start").click()
for i in range(1000):
    action_chains.double_click().perform()

while(True):
    Pass
