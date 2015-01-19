from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)

import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability

import csv
#imports csv module

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000029/postsup_20150107-135502-0.htm')
#uses get method to retreieve webpage and data for small filing from January 7, 2015

page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997008000004/postingsup_20081014.htm')
#uses get method to retreieve webpage and data for first filing (October 14, 2008)

tree = html.fromstring(page.text)
#parse webpage into tree structure

test = tree.xpath('//p/font/text()')

raw_date2_word_list = tree.xpath('//p[./font[contains(., "Notes will be issued upon closing and funding of member")]]/font/text()')

#/html/body/document/type/sequence/filename/text/div/p[11]/font/text()

#test = tree.xpath('//table[./td[contains(., "Home\nownership")]]//tr[./td[contains(., "Home\ntown")]]/td/font/text()')

#location = tree.xpath('//tr[./td[contains(., "Home\ntown:")]]/td[2]/font/text()')
#past_employers = tree.xpath('//tr[./td[contains(., "Current & past\nemployers:")]]/td[2]/font/text()')
#current_employers = tree.xpath('//tr[./td[contains(., "Current & past\nemployers:")]]/td[2]/font/text()')
#job_title = tree.xpath('//tr[./td[contains(., "Job title:")]]/td[2]/font/text()')
#education = tree.xpath('//tr[./td[contains(., "Education:")]]/td[2]/font/text()')

#csrange = tree.xpath('//tr[./td[contains(., "Total Credit\nLines:")]]/td[2]/font/text()')
#csrange = tree.xpath('//tr[./td[contains(., "Open Credit\nLines:")]]/td[4]/font/text()')

#lastrecord = tree.xpath('//tr[./td[contains(., "Months Since Last\nRecord:")]]/td[4]/font/text()')
#lastderog = tree.xpath('//tr[./td[contains(., "Months Since Last Major Derogatory")]]/td[4]/font/text()')
#lastrecord = tree.xpath('//tr[./td[contains(., "Revolving Line\nUtilization:")]]/td[4]/font/text()')
#tenure = tree.xpath('//tr[./td[contains(., "Length of\nemployerment:")]]/td[2]/font/text()')

#loankey = tree.xpath('//tr[2]/td[1]/p/b/font/text()')

#mortgage = tree.xpath('//tr[./td[contains(., "Home\nownership")]]/td[2]/font/text()')

#income = tree.xpath('//tr[./td[contains(., "Home\nownership")]]/td[4]/font/text()')

#debt = tree.xpath('//tr[./td[contains(., "Debt-to-income\nratio:")]]/td[4]/font/text()')
		
#tenure = tree.xpath('//tr[./td[contains(., "Length of\nemployment:")]]/td[2]/font/text()')

#location = tree.xpath('//tr[./td[contains(., "Length of\nemployment:")]]/td[4]/font/text()')

#hometown = tree.xpath('//tr[./td[contains(., "Home\ntown:")]]/td[2]/font/text()')
		
#pastemployers = tree.xpath('//tr[./td[contains(., "Current & past\nemployers:")]]/td[2]/font/text()')

#currentemployers = tree.xpath('//tr[./td[contains(., "Current & past\nemployers:")]]/td[2]/font/text()')

#job = tree.xpath('//tr[./td[contains(., "Job title:")]]/td[2]/font/text()')

#education = tree.xpath('//tr[./td[contains(., "Education:")]]/td[2]/font/text()')


#if not currentemployers:
	#for i in loankey:
		#currentemployers.append("N/a")
		#print "done1"

#if not pastemployers:
	#for i in loankey:
		#pastemployers.append("N/a")
		#print "done 2"

#if not job:
	#for i in loankey:
		#job.append("N/a")
		#print "done 3"


#print currentemployers
#print pastemployers
#print job

#print mortgage
#print income
#print debt
#print tenure
#print location
#print hometown
#print pastemployers
#print currentemployers
#print job
#print education

#print test

#print date2[0]

date_heading_2 = ["Date 2"]
#creates the date_heading


raw_date2_word = str(raw_date2_word_list)
#raw_date_word turns the single element in raw_date_list into a string

raw_date2 = raw_date2_word.splitlines()
#raw date turns the string, which has two lines, into a list with two elements

#date = [raw_date[1]]
#date grabs the date, which is the second element in raw_date, as a list (the brackets turn it into a list)

print raw_date2[0]
#print tenure
#print lastderog 
#print csrange
#print current_employers
#print job_title
#print education
