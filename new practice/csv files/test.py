from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)
import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability
import csv
#imports csv module

## section for parsing webpage in xml (in tree structure) begins ##

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000029/postsup_20150107-135502-0.htm')
#uses get method to retreieve webpage and data for filing from January 7, 2015

ops = open ("salesup_links.txt", "r")

for lines in ops: 
	print lines