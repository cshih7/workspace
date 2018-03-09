

#What about JavaScript enabled sites? http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Scraping_a_Webpage_Rendered_by_Javascript_Using_Python.php

#2/5/18
# #-----SAFEWAY PORTION----#
# import code 

# #find length of HTML on a page
# from mathematicians import simple_get
# raw_html = simple_get('http://plan.safeway.com/Circular/Menlo-Park-525-El-Camino-Real/CCBC74236/Other/5')
# # print len(raw_html) 
# # the last number at the end of this above Safeway link refers to the # week of the month it is (i.e., 3=3rd flyer of the month)

# raw_html = simple_get('http://plan.safeway.com/Circular/Menlo-Park-525-El-Camino-Real/CCBC74236/Other/3')
# # (following is optional code if i want to download into a file on my computer)
# with open('safeway5.html', "w") as html_file:
# 	html_file.write(raw_html)
# html_file.close()

# #READING SAFEWAY'S FRIDAY $5 FLYER

# from bs4 import BeautifulSoup
# raw_html = open('safeway5.html').read()
# html = BeautifulSoup(raw_html, 'html.parser')
# with open('safewaydeals.txt', 'w') as outfile:
# 	outfile.write('Safeway Friday $5 Deals' + '\n' + '\n')
# 	for p in html.select('p'):
# 		if p.has_attr('class'):
# 			if p['class'] == ['itemPrice']:
# 				outfile.write(p.text + '\n')
# 			if p['class'] == ['itemTitle']:
# 				outfile.write((p.text + '\n' + '\n').encode('utf8'))
# outfile.close()

#-----SPROUTS PORTION-----#

# 2/7/18
#Let's use Selenium to scrape from JavaScript-rendered page: 

import time
from utils.driver import get_driver
driver = get_driver()

driver.get('https://shop.sprouts.com/shop/flyer')

def get_button_by_id(id):
	try:
		button = driver.find_element_by_id(id) 
	except:
		button = None

	if not button:
		time.sleep(2)
		return get_button_by_id(id)

	return button

searchbutton = get_button_by_id('shopping-selector-search-cities')
searchbutton.send_keys('94040')

submitbutton = get_button_by_id('shopping-selector-update-home-store-157-instore')
submitbutton.click()

innerHTML = driver.execute_script("return document.body.innerHTML") #returns the innerHTML as a string
# print len(innerHTML)


with open('sproutsflyer.html', "w") as html_file:
  html_file.write(innerHTML.encode('utf8'))
  html_file.close()

#html_file = file('sproutsflyer', 'r')
#print html_file.read().decode('utf8')

from bs4 import BeautifulSoup
sproutshtml = open('sproutsflyer.html').read()
html = BeautifulSoup(sproutshtml, 'html.parser')
with open('sproutsdeals.txt', 'w') as outfile:
	outfile.write('Sprouts Front Page Deals' + '\n' + '\n')
	for span in html.select('span'):
		if span.has_attr('class'):
			if span['class'] == ['cell-title-text']: #<-- Watch out for "list" vs. str with [] or without []
				outfile.write('\n' + (span.text).encode('utf8') + '\n')		
			if span['class'] == ['amount']:
				if 'sale' in span.parent.parent['class']:
					#code.interact(local = locals())
					outfile.write((span.text).encode('utf8'))
			if span['class'] == ['unit']:
				if 'sale' in span.parent.parent['class']:	
					outfile.write((span.text + '\n').encode('utf8'))
outfile.close()

# # -----WHOLE FOODS PORTION-----#
# from mathematicians import simple_get

# raw_html = simple_get('https://www.wholefoodsmarket.com/sales-flyer/losaltos')
# # (following is optional code if i want to download into a file on my computer)
# with open('wholefoods.html', "w") as html_file:
# 	html_file.write(raw_html)
# html_file.close()

# from bs4 import BeautifulSoup
# raw_html = open('wholefoods.html').read()
# html = BeautifulSoup(raw_html, 'html.parser')
# with open('wholefoodsdeals.txt', 'w') as outfile:
# 	outfile.write('Whole Foods Deals of the Week' + '\n' + '\n')
# 	for div in html.select('div'):
# 		if div.has_attr('class'):
# 			if 'views-field-field-flyer-brand-name' in div['class']: 
# 				outfile.write((div.text).encode('utf8') + ' ')
# 			if 'views-field-field-flyer-product-name' in div['class']:
# 				outfile.write(div.text + '\n')
# 			if div['class'] == ['sale_line']:
# 				outfile.write(div.text + '\n')		
# 			if div['class'] == ['reg_line']:
# 				outfile.write(div.text + '\n')
# outfile.close()

# # ----END ---- #

#now, read through the html and find the tag to spit out the sale items
#then maybe compile safeway + sprouts in excels
#create a list of dictionaries (item name, slug, price) 

