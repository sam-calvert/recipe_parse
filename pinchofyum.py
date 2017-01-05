#!/bin/python3
from bs4 import BeautifulSoup
import urllib.request

url = input("recipe url? ")
print()
#Request URL using a fake user-agent, as the python3 user agent appears to get blocked a lot
request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
#Read requested URL
page = urllib.request.urlopen(request).read()

#soup it
soup = BeautifulSoup(page, 'html.parser')


print((soup.find("div", class_="ERSName")).get_text())
#ingredients = (soup.find_all("div", class_="ingredient"))
ingredients = (soup.find_all(attrs={"class": "ingredient"}))
#print(dir(ingredients))
#print(ingredients)

instructions = (soup.find_all(attrs={"class": "instruction"}))

print()

print("Ingredients: ")
for i in ingredients:
    print((i.get_text()))

print()
print()
print("Instructions: ")
for i in instructions:
    print((i.get_text()))

print()
print()


