# If you want to scrap a website:
# 1. Use the API
# 2. HTML web Scrapping using some tool like bs4


# Step 0: Install all the requirements
# pip install requests
# pip install bs4
# pip install html5lib

#
import requests
from bs4 import BeautifulSoup
url = "http://bhuvan.rf.gd/?i=1"
# step 1: Get the HTML
r = requests.get(url)		# r variable has all the HTML code
htmlContent = r.content	 # r returns response so if we want the code we write r.content
# print(htmlContent)		# printing the code
# Instead of “content” we can also use “text”:
htmlTexr = r.text
print(htmlTexr)
# step 2: Parse the HTML

# Step 3: HTML Tree traversal
#print(htmlcontent)
