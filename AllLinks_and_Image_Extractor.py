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

Documentation : https://pypi.org/project/beautifulsoup4/

'''
import requests as r 
from bs4 import BeautifulSoup as bs 

url=input("Enter link : ")

responseAsWeb=r.get(url)
HtmlContent=responseAsWeb.content
soup=bs(HtmlContent,'html.parser')

print("All Links are :>")
links=soup.find_all('a')
for index,l in enumerate(links):
    text=l.get('href')
    print(index+1,text)

print("All Image Links are :>")
links=soup.find_all('img')
for index,l in enumerate(links):
    text=l.get('src')
    print(index+1,text)