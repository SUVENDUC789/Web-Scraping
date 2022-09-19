'''
If you want to scrape a website:
	1. Use the Api
	2. Html Web Scraping using some tool like bs4

Requirment Tools :
	1. pip install requests
	2. pip install bs4
	3. pip install html5lib

HTML:
	Step 1 : Get the HTML
	Step 2 : Parse the HTML
	Step 3 : HTML Tree traversal

Commonly used types of objects:
	1.Tag
	2.NavigableString
	3.BeautifulSoup
	4.Comment

'''
import requests 
from bs4 import BeautifulSoup
# https://is-weather-fine.herokuapp.com/weather
# https://is-weather-fine.herokuapp.com/
url='https://is-weather-fine.herokuapp.com/weather'
# url = 'https://suvenduc789.herokuapp.com/student/'

# Step 1 : Get the HTML
r=requests.get(url)
htmlContent=r.content
# print(htmlContent)

# Step 2 : Parse the HTML
soup=BeautifulSoup(htmlContent,'html.parser')
# print(soup.prettify)

# Step 3 : HTML Tree traversal
# title=soup.img
# print(type(title))

# Get all the Paragraph from the page
# paras=soup.find_all('p')
# print(paras)

# Get all the Anchors from the page
# atag=soup.find_all('div')
# atag=soup.find('a')['class']
# atag=soup.find('table').get_text()
# print(atag)

# get all link in your web page 
Links=soup.find_all('a')
for l in Links:
	text=l.get('href')
	print(text)