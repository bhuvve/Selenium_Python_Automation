# Type a paragraph in google docs
from ast import Pass
from selenium.webdriver import Chrome, Edge
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

Keys.SPACE # to remove extra space in below string

str="""These types of actions are mainly common in complex scenarios like drag and drop and hovering over an element on the page. The methods of the Action Chains class are utilized by advanced scripts. We can manipulate DOM with the help of Action Chains in Selenium.

The action chain object implements the ActionChains in the form of a queue and then executes the perform() method. On calling the method perform(), all the actions on action chains will be performed.

The method of creating an Action Chain object is listed below −

First we need to import the Action Chain class and then the driver will be passed as an argument to it.

Now all the operations of action chains can be done with the help of this object."""


url="https://docs.google.com/document/d/1TAtDLPTy-i5aBGFMcqvjIhQRSqwdnJC871CMI7ErQ1E/editl"
 # How many times can you click in 30 Seconds?
driver_path = "D:\Selenium\venv\chromedriver.exe"


browser = Chrome(executable_path="driver_path")
browser.get(url)
from selenium.webdriver import ActionChains
action_chains = ActionChains(browser)
action_chains.send_keys(str).perform()
while(True):
    pass
