import re 
#imports module for regex string matching
from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)
import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability
import csv
#imports csv module
from lxml import etree
#imports etree from lxml module (not actually sure if this is necssary--just covering bases)
import lxml.html as lh
#import the lxml.html module as lh

## section for parsing webpage in xml (in tree structure) begins ##


ops = open ('salesup_links.txt', 'r')
#open list of html links to salesup filings in read mode 


c = 0
#sets count c, which will be used for naming csv files, to 0 to start 

for lines in ops: 
	if re.match("(.*)(salessup)(.*)", lines):
		a = lines.strip() 
		print a 