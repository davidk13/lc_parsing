import os, sys

from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)

import requests 

#import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability
import csv

path = "/Users/davidkastelman/Desktop/wget_test/boom"
dirs = os.listdir( path )

for files in dirs: 
	page = os.path.join(path,files)
	with open (page,"w") as myfile:
		myfile.write("append text")
		myfile.close()
	print page


#for files in dirs: 
#	page = os.path.join (path, files)
#	tree = html.parse(page)
#	key = tree.xpath('//tr[2]/td[1]/p/b/font/text()')
#	print key
	
