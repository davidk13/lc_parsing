from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)

import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability

import csv
#imports csv module

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000029/postsup_20150107-135502-0.htm')
#uses get method to retreieve webpage and data for first filing (October 14, 2008)

page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997008000004/postingsup_20081014.htm')
#uses get method to retreieve webpage and data for small filing from January 7, 2015

tree = html.fromstring(page.text)
#parse webpage into tree structure

#borrower = tree.xpath('//table/tr[1]/td[@width = "160" ]/font/text()')

#borrower = tree.xpath('//table/tr/td[@style= "PADDING-RIGHT: 5.4pt; PADDING-LEFT: 5.4pt; PADDING-BOTTOM: 0in; WIDTH: 100pt; PADDING-TOP: 0in"]#/font/text()')

#borrower = tree.xpath('//table[./tr[contains(., "Home\nownership:")]]/tr[2]/td[2]/font/text()')

#borrower = tree.xpath('//table[./td[contains(., "Home\nownership")]]/tr[2]/td[2]/font/text()')

loan = tree.xpath('//tr[2]/td[3]/p/font/text()')

borrower = tree.xpath('//font[contains(., "Posting Supplement No.")]/text()')
#/html/body/document/type/sequence/filename/description/text/div/p[11]/font/text()

print loan 

sliced = str(borrower[0])

orange=sliced.splitlines()

apple = [orange[1]]

print apple

print len (loan)

final_borrower = [apple + [i] for i in loan]

print final_borrower


#count(td[@style = "PADDING-RIGHT: 5.4pt; PADDING-LEFT: 5.4pt; PADDING-BOTTOM: 0in; WIDTH: 120pt; PADDING-TOP: 0in"]) > 1]