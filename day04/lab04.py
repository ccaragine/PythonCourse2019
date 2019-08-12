## Go to https://polisci.wustl.edu/people/88/
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization
## 	-Name *
## 	-Title * 
## 	-E-mail  *
## 	-Web page  *
	
from bs4 import BeautifulSoup
import urllib.request
import csv 

web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)
web_page 

soup = BeautifulSoup(web_page.read())
soup.prettify()

soup.find_all('a')
soup.find_all('div')
soup.find_all('h3')

names = soup.find_all('h3') ## list of html entries
firstlast = [i.text for i in names]

webtitle = soup.find_all('div', {'class' : "dept"})
title = [i.text for i in webtitle]

soup.find_all('div', {'class' : "card"})

all_a_tags = soup.find_all('a', {'class' : "card"})


try:
   for i in all_a_tags:
       current_link = i['href']
       new_url = 'https://polisci.wustl.edu' + current_link
       newsite = urllib.request.urlopen(new_url)
except urllib.error.URLError:
    print("Epstein")


web_aksoy = "https://polisci.wustl.edu/people/deniz-aksoy"
web_pageaksoy = urllib.request.urlopen(web_aksoy)
web_pageaksoy 

soup = BeautifulSoup(web_pageaksoy.read())
soup.prettify()

soup.find_all('a')
soup.find_all('div')
soup.find_all('h3')

contact = soup.find_all('ul', {'class': "detail contact"})
email = contact[0].a["href"]
print(email)

link = soup.find_all('ul', {'class': "links"})
personal_website = link[0].a["href"]
print(personal_website)

specialization = soup.find_all('div', {'class': "post-excerpt"})
first_line = [i.text for i in specialization]
print(first_line)






			
				
				
				
