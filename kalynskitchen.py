#!/bin/python3
from bs4 import BeautifulSoup
import urllib.request
import re

url = input("recipe url? ")
print()

#Request URL using a fake user-agent, as the python3 user agent appears to get blocked a lot
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

#Read requested URL
page = urllib.request.urlopen(request).read()

#soup it
ksoup = BeautifulSoup(page, 'html.parser')

#For Kalyn's unstrucured website, it makes more sense to grab the "printable" recipe
#and parse that rather than trying to fight the tag irregularities on the main site.
links = ksoup.find_all(href=re.compile("printable"))
for l in links: 
    printable = (l.get("href"))


request = urllib.request.Request(printable, headers={'User-Agent': 'Mozilla/5.0'})
ppage = urllib.request.urlopen(request).read()
soup = BeautifulSoup(ppage, 'html.parser')

print(soup.h3.string)

body = (soup.find_all(itemprop='description articleBody'))

for i in body: 
   for s in i.stripped_strings:
       print(s)
