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

#to extract a single list of names rather than duplicates included when there are multiple names separated by newline characters

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = simple_get(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))

#NEXT: To get page views of this mathematicians page at https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/Henri_Poincar%C3%A9,
#notice that the text appears inside an <a> element, and that the href attribute of that element always contains the string 'latest-60' as a substring
#...use that to find the text

def get_hits_on_name(name):
    """
    Accepts a `name` of a mathematician and returns the number
    of hits that mathematician's wikipedia page received in the 
    last 60 days, as an `int`
    """
    # url_root is a template string that used to buld a URL.
    url_root = 'https://xtools.wmflabs.org/articleinfo/en.wikipedia.org/{}'
    response = simple_get(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')

        hit_link = [a for a in html.select('a')
                    if a['href'].find('latest-60') > -1]

        if len(hit_link) > 0:
            # Strip commas:
            link_text = hit_link[0].text.replace(',', '')
            try:
                # Convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))

    log_error('No pageviews found for {}'.format(name))
    return None


 #what about errors?

 