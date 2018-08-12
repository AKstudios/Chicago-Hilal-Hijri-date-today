from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

# specify the url here
url = 'http://chicagohilal.org/'

# specify browser user agent to bypass mod_security blocking bot user agents like urllib
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# query the website and return the HTML
web_page = urlopen(req)

# parse the HTML using BeautifulSoup
soup = BeautifulSoup(web_page, 'html.parser')

# Locate today's hijri date from HTML
date = soup.find('span', attrs={'class':'simcal-event-title'})

# print only the actual text string (remove tags)
print (date.text)
