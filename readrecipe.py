
#---------#
import code 

#find length of HTML on a page
from mathematicians import simple_get

#READING A RECIPE BLOG FOR INGREDIENTS
from bs4 import BeautifulSoup
raw_html2 = simple_get('https://www.kingarthurflour.com/recipes/chocolate-mousse-cake-with-raspberries-recipe')
html2 = BeautifulSoup(raw_html2, 'html.parser')
for l in html2.select('li'):
	if l.has_attr('data-serverid'):
		#code.interact(local = locals())
		if l['data-serverid'] == 'IngredientLine': #notice this is a str and not a list! no []
			print(l.text)
			# looks like the recipe is repeated multiple times, but it's actually that the recipe is given in different measurements (oz, grams, cups)
			
""" If you wanted to figure out where there are duplicates...
			recipe = {}
			if l.text not in recipe:
				recipe = l.text
			print recipe
"""