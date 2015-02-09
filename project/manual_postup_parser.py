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



# for loop, for each line in the list, if it contains pstoingsup or postup (to avoid empty lines), 
#strip the line of cumbersome white space and then parse using the lxml.html parse method  

## parsing section has ended ##

page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000164/postsup_20150209-095501-0.htm')
#uses get method to retreieve webpage and data for filing from February 9, 2015

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000151/postsup_20150206-055501-0.htm')
#uses get method to retreieve webpage and data for filing from February 6, 2015


tree = html.fromstring(page.text)
## data scraping section begins ##

class Loan: 
#define a class "Loan" which grabs the relevant data from the loan table in the filing
#grabs data as lists (the brackets for the heading (e.g. self.key_heading) makes it a list format)
#The class also includes the variable headings as hard-coded, single element lists (e.g. key, Service Charge, Initial maturity, etc.)
#These paths are defined as a class so the elements (e.g. key, amount) are accesible as methods (e.g. loan.amount)

	def __init__(self):
		self.key = tree.xpath('//tr[2]/td[1]/p/b/font/text()')
		self.key_heading = ["Series of Member Payment Dependent Notes"]
		self.amount = tree.xpath('//tr[2]/td[2]/p/font/text()')
		self.amount_heading = ["Maximum aggregate principal amount offered"]
		self.interest_rate = tree.xpath('//tr[2]/td[3]/p/font/text()')
		self.interest_rate_heading = ["Stated interest rate"]
		self.service_charge = tree.xpath('//tr[2]/td[4]/p/font/text()')
		self.service_charge_heading = ["Service Charge"] 
		self.initial_maturity = tree.xpath('//tr[2]/td[5]/p/font/text()')
		self.initial_maturity_heading = ["Initial maturity"]
		self.final_maturity = tree.xpath('//tr[2]/td[6]/p/font/text()')
		self.final_maturity_heading = ["Final maturity"]


loan = Loan()
#instantiates the Loan class with a single instance, "loan"

class Borrower: 
#defines a class "Borower" which grabs the relevant data about the borrower
#There is not a unique sequence of html tags for the borrower elements. For example //tr[1]/td[2]/font/text would be a path
#to both the Home ownership status and the Credit Score Range (a credit element)
#therefore it is necessary to use an xml function, contains(), to select the right row of a table, before determining the rest of the path
#The Borrower.job path exists in the new filing, Borrower.past_employers and Borrower.current_employers exists in the old filing, 
# and Borrower.hometown and Borrower.education exists in both (but in diff locations) 

	def __init__(self): 
		self.mortgage = tree.xpath('//tr[./td[contains(., "Home\nownership")]]/td[2]/font/text()')
		self.mortgage_heading = ["Home ownership"]
		self.income = tree.xpath('//tr[./td[contains(., "Home\nownership")]]/td[4]/font/text()')
		self.income_heading = ["Gross income"]
		self.debt = tree.xpath('//tr[./td[contains(., "Debt-to-income\nratio:")]]/td[4]/font/text()')
		self.debt_heading = ["Debt-to-income ratio"]
		self.tenure = tree.xpath('//tr[./td[contains(., "Length of\nemployment:")]]/td[2]/font/text()')
		self.tenure_heading = ["Length of employment"]
		self.location = tree.xpath('//tr[./td[contains(., "Length of\nemployment:")]]/td[4]/font/text()')
		self.location_heading = ["Location"]
		self.hometown = tree.xpath('//tr[./td[contains(., "Home\ntown:")]]/td[2]/font/text()')
		self.hometown_heading = ["Home town"]
		self.pastemployers = tree.xpath('//tr[./td[contains(., "Current & past\nemployers:")]]/td[2]/font/text()')
		self.pastemployers_heading = ["Current & past employers"]
		self.currentemployers = tree.xpath('//tr[./td[contains(., "Current & past\nemployers:")]]/td[2]/font/text()')
		self.currentemployers_heading = ["Current employer"]
		self.job = tree.xpath('//tr[./td[contains(., "Job title:")]]/td[2]/font/text()')
		self.job_heading = ["Job title"]
		self.education = tree.xpath('//tr[./td[contains(., "Education:")]]/td[2]/font/text()')
		self.education_heading = ["Education"]

borrower = Borrower()
#instantiates the Borrower class with a single instance, "borrower"

class Credit: 
#defines a class "Credit" which grabs the relevant data about the borrower's credit report
# The new and old filings are actually almost identical, but the new filing has an 
#additional "Months since last major derogatory" (Credit.lastderog) element

	def __init__(self):
		self.csrange = tree.xpath('//tr[./td[contains(., "Credit Score\nRange:")]]/td[2]/font/text()')
		self.csrange_heading = ["Credit Score Range"]
		self.accountsdelinq = tree.xpath('//tr[./td[contains(., "Credit Score\nRange:")]]/td[4]/font/text()')
		self.accountsdelinq_heading = ["Accounts Now Delinquent"]
		self.earliest = tree.xpath('//tr[./td[contains(., "Earliest Credit\nLine:")]]/td[2]/font/text()')
		self.easliest_heading = ["Earliest Credit Line"]
		self.amountdelinq = tree.xpath('//tr[./td[contains(., "Earliest Credit\nLine:")]]/td[4]/font/text()')
		self.amountdelinq_heading = ["Delinquent Amount"]
		self.openlines = tree.xpath('//tr[./td[contains(., "Open Credit\nLines:")]]/td[2]/font/text()')
		self.openlines_heading = ["Open Credit Lines"]
		self.countdelinq = tree.xpath('//tr[./td[contains(., "Open Credit\nLines:")]]/td[4]/font/text()')
		self.countdelinq_heading = ["Delinquencies (Last 2 years)"]
		self.totalines = tree.xpath('//tr[./td[contains(., "Total Credit\nLines:")]]/td[2]/font/text()')
		self.totalines_heading = ["Total Credit Lines"]
		self.delinqfree = tree.xpath('//tr[./td[contains(., "Total Credit\nLines:")]]/td[4]/font/text()')
		self.delinqfree_heading = ["Months Since Last Delinquency"]
		self.balance = tree.xpath('//tr[./td[contains(., "Revolving Credit\nBalance:")]]/td[2]/font/text()')
		self.balance_heading = ["Revolving Credit Balance"]
		self.publicrecords = tree.xpath('//tr[./td[contains(., "Revolving Credit\nBalance:")]]/td[4]/font/text()')
		self.publicrecords_heading = ["Public Records on File"]
		self.utilization = tree.xpath('//tr[./td[contains(., "Revolving Line\nUtilization:")]]/td[2]/font/text()')
		self.utilization_heading = ["Revolving Line Utilization"]
		self.lastrecord = tree.xpath('//tr[./td[contains(., "Revolving Line\nUtilization:")]]/td[4]/font/text()')
		self.lastrecord_heading = ["Months Since Last Record"]
		self.inquiries = tree.xpath('//tr[./td[contains(., "Inquiries in the\nLast 6 Months:")]]/td[2]/font/text()')
		self.inquiries_heading = ["Inquiries in the Last 6 Months"]
		self.lastderog = tree.xpath('//tr[./td[contains(., "Months Since Last Major Derogatory")]]/td[4]/font/text()')
		self.lastderog_heading = ["Months Since Last Major Derogatory"]


credit = Credit()
#instantiate the Credit class with a single instance, "credit"

## data scrapping section has ended ##


## next section is for grabbing the date of the filing ##

date_heading = ["Date"]
#creates the date_heading

raw_date_word_list = tree.xpath('//font[contains(., "Posting Supplement No.")]/text()')
#raw_date_word_list grabs the line of text that lists the filing date  

raw_date_word = str(raw_date_word_list[0])
#raw_date_word turns the single element in raw_date_list into a string

raw_date = raw_date_word.splitlines()
#raw date turns the string, which has two lines, into a list with two elements

date = [raw_date[1]]
#date grabs the date, which is the second element in raw_date, as a list (the brackets turn it into a list)

for i in loan.key:
	date.append(raw_date[1])
#the for loop ensures that there are enough elements in the date list--one for each loan--so that it can be zipped with the other lists later on 

## date section has ended##

## adjusting for differences between the old and new format section ##

if not borrower.currentemployers:
	for i in loan.key:
		borrower.currentemployers.append("N/a")
#if not borrower.currentemployers is a pythonic way of checking if a list is empty
#if a list is empty, the for loop appends it with N/A so that it has the same number of elements as the other lists
#and can be zipped together (below)

if not borrower.pastemployers:
	for i in loan.key:
		borrower.pastemployers.append("N/a")
#see note starting on line 151

if not borrower.job:
	for i in loan.key:
		borrower.job.append("N/a")
#see note starting on line 151

if not credit.lastderog:
	for i in loan.key:
		credit.lastderog.append("N/a")
#see note starting on line 151

if not borrower.education:
	for i in loan.key:
		borrower.education.append("N/a")
#see note starting on line 151

if not borrower.hometown:
	for i in loan.key:
		borrower.hometown.append("N/a")
#see note starting on line 151

## old and new format adjustment section ends ##


##adjusting for empty entries (some borrower charcteristics were optional) in the old format ##

if len(borrower.mortgage) != len(loan.key):
	borrower.education = []
	for i in loan.key:
		borrower.education.append("__")
#in the old format, it appears that at least some of the borrower characteristics were optional
#in order to make sure lists have the same number of elements so that they can be zipped together
#it is necessary to first empty the list, and then append it with "__"

if len(borrower.income) != len(loan.key):
	borrower.income = []
	for i in loan.key: 
		borrower.income.append("__")
#see note starting on line 189

if len(borrower.debt) != len(loan.key):
	borrower.debt = []
	for i in loan.key: 
		borrower.debt.append("__")
#see note starting on line 189

if len(borrower.tenure) != len(loan.key):
	borrower.tenure = []
	for i in loan.key: 
		borrower.tenure.append("__")
#see note starting on line 189

if len(borrower.location) != len(loan.key):
	borrower.location = []
	for i in loan.key: 
		borrower.location.append("__")
#see note starting on line 189

if len(borrower.hometown) != len(loan.key):
	borrower.hometown = []
	for i in loan.key: 
		borrower.hometown.append("__")
#see note starting on line 189

if len(borrower.pastemployers) != len(loan.key):
	borrower.pastemployers = []
	for i in loan.key: 
		borrower.pastemployers.append("__")
#see note starting on line 189

if len(borrower.currentemployers) != len(loan.key):
	borrower.currentemployers = []
	for i in loan.key: 
		borrower.currentemployers.append("__")
#see note starting on line 190

if len(borrower.job) != len(loan.key):
	borrower.job = []
	for i in loan.key: 
		borrower.job.append("__")
#see note starting on line 189

if len(borrower.education) != len(loan.key):
	borrower.education = []
	for i in loan.key: 
		borrower.education.append("__")
#see note starting on line 189

##end section adjusting for optional borrower entries##

## section for exporting to csv begins ##

csv_out = open('postup_newer_manual2_.csv', 'wb')
#open a file for writing called posting_old_format.csv, 'wb' puts it in writing mode

#csv_out = open('posting_new_format.csv', 'wb')
#open a file for writing called posting_new_format.csv, 'wb' puts it in writing mode

mywriter = csv.writer(csv_out)
#instantiate a csv writer object 


rows_headings = zip(date_heading, loan.key_heading, loan.amount_heading, loan.interest_rate_heading, 
loan.service_charge_heading, loan.initial_maturity_heading, loan.final_maturity_heading, 
borrower.mortgage_heading, borrower.income_heading, borrower.debt_heading, borrower.tenure_heading, 
borrower.location_heading, borrower.hometown_heading, borrower.pastemployers_heading,  
borrower.currentemployers_heading, borrower.job_heading, borrower.education_heading, 
credit.csrange_heading, credit.accountsdelinq_heading, credit.easliest_heading, credit.amountdelinq_heading,
credit.openlines_heading, credit.countdelinq_heading, credit.totalines_heading, credit.delinqfree_heading,
 credit.balance_heading, credit.publicrecords_heading, credit.utilization_heading, credit.lastrecord_heading, credit.inquiries_heading,
 credit.lastderog_heading)
#zips the variable headings together into a single list 


rows_values = zip(date, loan.key, loan.amount, loan.interest_rate, loan.service_charge, loan.initial_maturity, loan.final_maturity, 
borrower.mortgage, borrower.income, borrower.debt, borrower.tenure, borrower.location, borrower.hometown, borrower.pastemployers, 
borrower.currentemployers, borrower.job, borrower.education, credit.csrange, credit.accountsdelinq, credit.earliest, 
credit.amountdelinq, credit.openlines, credit.countdelinq, credit.totalines, credit.delinqfree, credit.balance, 
credit.publicrecords, credit.utilization, credit.lastrecord, credit.inquiries, credit.lastderog)
#zips the date and all of the loan variables into a series of lists, one list per loan 


rows = rows_headings + rows_values
#combines the headings list (as the first row) with the row_values lists 

mywriter.writerows(rows)
#writes the rows (remember rows = rows_headings + rows_values) to the csv file 


csv_out.close()
#closes the csv file

##end export to csv section##

print str(len(rows)) 
#prints count and length of rows in each csv file, in part so you can track progress
