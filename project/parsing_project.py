from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)
import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000029/postsup_20150107-135502-0.htm')
#uses get method to retreieve webpage and data for first filing (October 14, 2008)

page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997008000004/postingsup_20081014.htm')
#uses get method to retreieve webpage and data for small filing from January 7, 2015

tree = html.fromstring(page.text)
#parse webpage into tree structure

#headings = tree.xpath('//td[@width="72"]/p/b/font/text()')
#unnecessary grab of headings (since constant, do not need to grab for each table)--needed to use combination of tags and style, since tags weren't unique

#oldloantable = tree.xpath('//td[@style = "BORDER-RIGHT: windowtext 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: medium none; PADDING-LEFT: 5.4pt; PADDING-BOTTOM: 0in; BORDER-LEFT: medium none; WIDTH: 72pt; PADDING-TOP: 0in; BORDER-BOTTOM: windowtext 1pt solid"]/p/font/text()')
#(commented out) inelegant first solution which dependend on style instead of pathway for primary loan table

loantable = tree.xpath('//tr[2]//p/font/text()')
#grabs numeric values of loan detail table, minus key--more elegant second solution which depends on html tags (path)

loankey = tree.xpath('//tr[2]/td[1]/p/b/font/text()')
#grabs unique loan transaction number (key), for use in any relational databases

borrowerinfo1 = tree.xpath('//tr/td[2]/font/text()')
#grabs just the values (not headings) of left half of borower characteristic tables below 

borrowerinfo2 = tree.xpath('//tr/td[4]/font/text()')
#grabs just the values (not heaadings) of the right half of borrower characteristic tables

print 'loantable: ', loantable[:6]
#print function to make sure command scrapes right data, commented out 

print 'borrowerinfo1: ', borrowerinfo1[:20]
#print function to make sure command scrapes right data, commented out 

print 'borrowerinfo2: ', borrowerinfo2[:20]
#print function to make sure command scrapes right data, commented out 

print 'loankey: ', loankey[:20]
#print function to make sure command scrapes right data, commented out 

#print 'length: ', len(loankey)
#seeing how many loans are in a file 
