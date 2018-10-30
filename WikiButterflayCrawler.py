# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 06:19:06 2018

@author: PCLee
Crawl images of butterfly found in Taiwan from Wiki. 
"""

from bs4 import BeautifulSoup
import urllib
import requests as rq
 

response = rq.get('https://zh.wikipedia.org/wiki/%E8%87%BA%E7%81%A3%E8%9D%B4%E8%9D%B6%E5%88%97%E8%A1%A8')
html_doc = response.text
soup = BeautifulSoup(html_doc, 'lxml')

soup.find_all('a', class_='image')
L = soup.find_all('a', class_='image')
str_L = [  str(x) for x in L ] 

prefix = 'https://zh.wikipedia.org/'
href_L = []
for i in range(1, len(str_L) ):
    start = str_L[i].find('/wiki/')
    end = str_L[i].find('.jpg')
    href_L.append( prefix + str_L[i][start: end + 4] )   

for link in href_L:
    html_doc = rq.get( link ).text
    soup = BeautifulSoup(html_doc, 'lxml')
    result = soup.find_all('a', class_='internal')
    if len(result) > 0 :
        result = str(result[0])
        start = result.find('//')
        end = result.find('.jpg')
        url = 'https:' + result[start:end+4]
        name = url[ url.rfind('/') + 1:]
        print(url)
        urllib.request.urlretrieve( url, filename='d:/wiki_butterfly/'+name)