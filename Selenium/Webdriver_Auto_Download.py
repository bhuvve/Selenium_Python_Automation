from selenium.webdriver import Chrome, Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
"""
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(EdgeChromiumDriverManager().install())
"""

url="https://www.google.com/"
driver_path = Chrome(ChromeDriverManager().install())
print("Installed")
driver_path.get(url)
driver_path.maximize_window()

element_obj = driver_path.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
element_obj.send_keys("Bhuvanachandra")
element_obj.send_keys(Keys.ENTER)

while(True):
    pass
