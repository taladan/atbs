#! bin/python

# searchpypi.py

# search URL: https://pypi.org/search/?q=<search_term>

import requests, sys, webbrowser, bs4, logging
# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)

logging.debug('Program start')
print('Searching...')               # Display text while downloading the search result page

# get the page contents
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
logging.debug(f'Request sent: {res=}')

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug(f'Soup obj created: {soup=}')
linkElems = soup.select('.package-snippet')
logging.debug(f'LinkElements selected: {linkElems=}')
numOpen = min(5, len(linkElems))

# Open a browser tab for each result.
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    logging.debug(f'Opening pages: {i} : {urlToOpen}')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)