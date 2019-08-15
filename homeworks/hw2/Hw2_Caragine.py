############## Homework 2 ##############
## Crystal Caragine
## 8/13/2019
## Hw2_Caragine

## Importing packages
from bs4 import BeautifulSoup
import urllib.request
import csv

## Opening file
with open('homework2.csv', 'w') as f:
  w = csv.DictWriter(f, fieldnames = ("Title", "Date", "Issues", "Signatures"))
  w.writeheader() 
  pet = {}
  web_address= 'https://petitions.whitehouse.gov/petitions'
  web_page = urllib.request.urlopen(web_address)
  soup = BeautifulSoup(web_page.read())
  soup.prettify()



## subsetting on the individual websites, finding Title and Date 
  all_h3 = soup.find_all('h3') 
  all_h3 = all_h3[3::]
  for i in all_h3:
        extension = i.a.attrs['href']  
        pet["Title"] = i.get_text()
        pet_page = urllib.request.urlopen('https://petitions.whitehouse.gov%s' % extension)
        pet_html = BeautifulSoup(pet_page.read())	    
        pet["Date"] = pet_html.find('h4', {'class' : "petition-attribution"}).get_text() 
        w.writerow(pet)
        
        
## Finding Signatures        
  all_span = soup.find_all('span', {'class' : "signatures-number"})    
  for j in all_span:  
        pet["Signatures"] = j.get_text()
        w.writerow(pet)
  
## finding Issues      
  all_div = soup.find_all('div', {'class' : "field-items"})  
  for k in all_div:
       pet["Issues"] = k.get_text()
       w.writerow(pet)




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
