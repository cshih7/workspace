#find length of HTML on a page

from mathematicians import simple_get
raw_html = simple_get('https://www.quokkachallenge.com/')
print len(raw_html)

#once you have the html file, read through it to find specific ID's and associated Text

from bs4 import BeautifulSoup
raw_html = open('contrived.html').read()
html = BeautifulSoup(raw_html, 'html.parser')
for p in html.select('p'):
	if p['id'] == 'walrus':
		print(p.text)

#or to enumerate and test your way through an html file

raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')):
	print(i, li.text)