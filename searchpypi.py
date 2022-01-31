#! bin/python

# searchpypi.py

# search URL: https://pypi.org/search/?q=<search_term>

import requests, sys, webbrowser, bs4, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.CRITICAL)
print('Searching...')               # Display text while downloading the search result page
res = requests.get('https://pypi.org/search/?q=' + ' '.join(sys.argv[1:]))
logging.debug(f'Request sent: {res=}')
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug(f'Soup obj created: {soup=}')
# Open a browser tab for each result.
linkElems = soup.select('.package-snippet')
logging.debug(f'LinkElements selected: {linkElems=}')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
    urlToOpen = 'https://pypi.org' + linkElems[i].get('href')
    logging.debug(f'Opening pages: {i} : {urlToOpen}')
    print('Opening', urlToOpen)
    webbrowser.open(urlToOpen)