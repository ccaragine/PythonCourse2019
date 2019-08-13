############## Homework 2 ##############
## Crystal Caragine
## 8/13/2019
## Hw2_Caragine


from bs4 import BeautifulSoup
import urllib.request
import re
import csv
import unicodedata

with open('homework2.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("Title", "Date", "Issues", "Signatures"))
  w.writeheader() 
  web_address= 'https://petitions.whitehouse.gov/petitions'
  web_page = urllib.request.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()

all_petitions = soup.find_all('h3') 
for i in all_petitions:
    pet = {}
    extension = i.attrs['href']   ### What
    
    pet["Title"] = i.article.find('h3').get_text()
    pet["Signatures"] = i.article.find('span', {'class' : "signatures-number"}).get_text()
    pet["Issues"] = i.article.find('div', {'class' : "field-items"}).get_text()
    
    pet_page = urllib.request.urlopen('https://petitions.whitehouse.gov/petition/%s' % extension)
    prof_html = BeautifulSoup(pet_page.read())	 
    
    pet["Date"] = pet_html.find('h4', {'class' : "pettition-attribution"}).get_text() 


#--------------------------------
soup.find_all('h3')
petition = soup.find_all('h3') 
title = [i.text for i in petition]

signatures = soup.find_all('span', {'class' : "signatures-number"})
number = [i.text for i in signatures]

issues = soup.find_all('div', {'class' : "field-items"})
issue_type = [i.text for i in issues]

date_field = soup.find_all('h4', {'class' : "pettition-attribution"})
date = [i.text for i in date_field] 
