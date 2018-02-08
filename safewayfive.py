

#What about JavaScript enabled sites? http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php

#2/5/18
#---------#
import code 

#find length of HTML on a page
from mathematicians import simple_get
#raw_html = simple_get('http://plan.safeway.com/Circular/Menlo-Park-525-El-Camino-Real/CCBC74236/Other/5')
#print len(raw_html)

"""
raw_html = simple_get('http://plan.safeway.com/Circular/Menlo-Park-525-El-Camino-Real/CCBC74236/Other/5')
#(following is optional code if i want to download into a file on my computer)
# with open('safeway5.html', "w") as html_file:
# 	html_file.write(raw_html)
# html_file.close()

#READING SAFEWAY'S FRIDAY $5 FLYER

from bs4 import BeautifulSoup
# raw_html = open('safeway5.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
	# code.interact(local = locals())
	if p.has_attr('class'):
		if p['class'] == ['itemPrice']: <-- Watch out for "list" vs. str with [] or without []
			print(p.text)
		if p['class'] == ['itemTitle']:
			#code.interact(local = locals())
			print(p.text + '\n')
"""

#2/7/18
#Let's use Selenium to scrape from JavaScript-rendered page: 
#should pip install selenium first, may need to install a chrome web driver?

from selenium import webdriver

browser = webdriver.Chrome() #replace with .Firefox(), or with the browser of your choice
url = "https://shop.sprouts.com/shop/flyer"
browser.get(url) #navigate to the page
innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string
