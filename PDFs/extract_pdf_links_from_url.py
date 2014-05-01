from bs4 import BeautifulSoup
import os
import urllib2


url = 'https://class.coursera.org/startup-001/wiki/view?page=syllabus'

conn = urllib2.urlopen(url)
html_doc = conn.read()

with open('se.html','rb') as fin:
  html_doc = fin.read()

soup = BeautifulSoup(html_doc)
links = soup.find_all('a') # Finds all hrefs from the html doc.

for tag in links:
    link = tag.get('href',None)
    if link != None and link[-3:] == 'pdf':
        print link
	os.system('wget ' + link)
