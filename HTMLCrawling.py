# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/known_by_Jagoda.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
# print(soup)

times = 4
position = 3 


# Retrieve all of the anchor tags

for i in range(0,6):
    print(i)
    html = urllib.request.urlopen(tags[17].get('href', None), context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
print(tags[17].contents[0])
# for tag in tags:
#     # if (position == 0):
#     #     position=3 
#     #     html = urllib.request.urlopen(tag.get('href', None), context=ctx).read()
#     #     soup = BeautifulSoup(html, 'html.parser')
        
#     print(tag.get('href', None))
    # print(tag.contents)
    
