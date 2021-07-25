#Creating a Web Scraper to collect and mine data from a website

from bs4 import BeautifulSoup

import requests

#Receives the entire content of the http request from the site
site = requests.get("https://www.globo.com").content

#downloading all html from the site and storing it in variable
soup = BeautifulSoup(site, 'html.parser')

#transforms html structure into string and displays on screen
# print(soup.prettify())

temp = soup.find("span", class_="_block _margin-b-5 -gray")

print(soup.title)

print(soup.p.string)

print(soup.find('admin'))


