#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

url = "http://jecvay.com"
#url = "http://ffce.ffan.com"
#response = requests.get(url)

html_doc = """  
<html><head><title>The Dormouse's story</title></head>  
<body>  
<p class="title"><b>The Dormouse's story</b></p>  
  
<p class="story">Once upon a time there were three little sisters; and their names were  
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,  
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;  
and they lived at the bottom of a well.</p>  
  
<p class="story">...</p>  
"""  
soup = BeautifulSoup(html_doc, "html.parser")
 
print("soup.title.text")
print(soup.title.text)

print("soup.body.text")
print(soup.body.text)

for x in soup.findAll("a"):
	print(x)
	print(x['href'])
