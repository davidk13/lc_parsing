import os, sys

import urllib

from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)

import lxml.html as lh

import urllib2

import requests



#import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability
import csv
#imports csv module

from lxml import etree 

## section for parsing webpage in xml (in tree structure) begins ##

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000029/postsup_20150107-135502-0.htm')
#uses get method to retreieve webpage and data for filing from January 7, 2015

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997008000004/postingsup_20081014.htm')
#(commented out) uses get method to retrieve webpage and data for first filing (October 14, 2008)

path = "/Users/davidkastelman/Desktop/wget_test/bullseye"
dirs = os.listdir( path )

for files in dirs:
	dest = os.path.join(path,files)
	ops = urllib.urlopen(dest)
	url = ops.geturl()

print url 
