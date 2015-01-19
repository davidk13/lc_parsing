from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)
import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability
import csv
#imports csv module

## section for parsing webpage in xml (in tree structure) begins ##

#page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997015000029/postsup_20150107-135502-0.htm')
#uses get method to retreieve webpage and data for filing from January 7, 2015

page = requests.get('http://www.sec.gov/Archives/edgar/data/1409970/000140997008000004/postingsup_20081014.htm')
#(commented out) uses get method to retrieve webpage and data for first filing (October 14, 2008)

tree = html.fromstring(page.text)
#parse webpage into tree structure

## parsing section has ended ##


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

## section for exporting to csv begins ##

#csv_out = open('new_format.csv', 'wb')
#open a file for writing called new_format.csv, 'wb' puts it in writing mode

csv_out = open('old_format.csv', 'wb')
#open a file for writing called old_format.csv, 'wb' puts it in writing mode

mywriter = csv.writer(csv_out)
#instantiate a csv writer object 

if not borrower.currentemployers:
	for i in loan.key:
		borrower.currentemployers.append("N/a")
#if not borrower.currentemployers is a pythonic way of checking if a list is empty
#if a list is empty, the for loop appends it with N/A (or __) so that it has the same number of elements as the other lists
#and can be zipped together (below)

if not borrower.pastemployers:
	for i in loan.key:
		borrower.pastemployers.append("N/a")
#see note starting on line 157

if not borrower.job:
	for i in loan.key:
		borrower.job.append("N/a")
#see note starting on line 157

if not credit.lastderog:
	for i in loan.key:
		credit.lastderog.append("N/a")
#see note starting on line 157

if not borrower.hometown:
	for i in loan.key:
		borrower.hometown.append("__")
#see note starting on line 157

if not borrower.education:
	for i in loan.key:
		borrower.education.append("__")
#see note starting on line 157

rows_headings = zip(date_heading, loan.key_heading, loan.amount_heading, loan.interest_rate_heading, 
	loan.service_charge_heading, loan.initial_maturity_heading, loan.final_maturity_heading, borrower.mortgage_heading,
	 borrower.income_heading, borrower.debt_heading, borrower.tenure_heading, borrower.location_heading, borrower.hometown_heading, 
	 borrower.pastemployers_heading, borrower.currentemployers_heading, borrower.job_heading, borrower.education_heading, 
	 credit.csrange_heading, credit.accountsdelinq_heading, credit.easliest_heading, credit.amountdelinq_heading, 
	 credit.openlines_heading, credit.countdelinq_heading, credit.totalines_heading, credit.delinqfree_heading, 
	 credit.balance_heading, credit.publicrecords_heading, credit.utilization_heading, credit.lastrecord_heading, credit.inquiries_heading, 
	 credit.lastderog_heading)
#zips the variable hadings together into a single list 


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

print "done"
#prints done in command line so it is easy to see when operation is finished


## appendix (old colde) is listed, commented out, below ##
#print date

#print rows_headings
#print rows_values[0:3]
#print rows[0:10]
#print rows
#borrower_home_ownership = tree.xpath('//tr[1]/td[2]/font/text()')
#grabs borrower's home ownership status 

#borrower

#borrower_current_employer = tree.xpath('//tr[1]/td[3]/font/text()')
#grabs borrower's current employer

#borrower_length_of_employment = tree.xpath('//tr[1]/td[4]/font/text()')
#grabs duration, in years, of employerment 

#loantable = tree.xpath('//tr[2]//p/font/text()')
#grabs numeric values of loan detail table, minus key--more elegant second solution which depends on html tags (path)

#borrowerinfo1 = tree.xpath('//tr/td[2]/font/text()')
#grabs just the values (not headings) of left half of borower characteristic tables below 

#borrowerinfo2 = tree.xpath('//tr/td[4]/font/text()')
#grabs just the values (not heaadings) of the right half of borrower characteristic tables

#print 'loantable: ', loantable[:6]
#print function to make sure command scrapes right data, commented out 

#print 'borrowerinfo1: ', borrowerinfo1[:20]
#print function to make sure command scrapes right data, commented out 

#print 'borrowerinfo2: ', borrowerinfo2[:20]
#print function to make sure command scrapes right data, commented out 

#print 'loankey: ', loankey[:20]
#print function to make sure command scrapes right data, commented out 

#print 'length: ', len(loankey)
#seeing how many loans are in a file 


#print "loankey heading: ", loan.key_heading

#print "loankey: ", loan.key[0:3]


#print "loan_amount_heading: ", loan.amount_heading

#print "loan_amount: ", loan.amount[0:3]


#print "loan_interest_rate_heading: ", loan.interest_rate_heading

#print "loan_interest_rate: ", loan.interest_rate [0:3]


#print "loan_service_charge_heading: ", loan.service_charge_heading

#print "loan_service_charge: ", loan.service_charge[0:3]


#print "loan_initial_maturity_heading: ", loan.initial_maturity_heading

#print "loan_initial_maturity: ", loan.initial_maturity[0:3]


#print "loan_final_maturity_heading: ", loan.final_maturity_heading

#print "loan_final_maturity: ", loan.final_maturity[0:3]


#APPENDIX: OLD CODE USED

#headings = tree.xpath('//td[@width="72"]/p/b/font/text()')
#unnecessary grab of headings (since constant, do not need to grab for each table)--needed to use combination of tags and style, since tags weren't unique

#oldloantable = tree.xpath('//td[@style = "BORDER-RIGHT: windowtext 1pt solid; PADDING-RIGHT: 5.4pt; BORDER-TOP: medium none; PADDING-LEFT: 5.4pt; PADDING-BOTTOM: 0in; BORDER-LEFT: medium none; WIDTH: 72pt; PADDING-TOP: 0in; BORDER-BOTTOM: windowtext 1pt solid"]/p/font/text()')
#(commented out) inelegant first solution which dependend on style instead of pathway for primary loan table

#loankey_heading = tree.xpath('//table[2]/tr[1]/td[1]/p/b/font/text()')
##test of grabbing heading for loankey, NOTE: IF YOU COPY AND PASTE CHROME XPATH, IT'LL INCLUDE <TBODY> WHICH HAS TO BE REMOVED	

#loankey = tree.xpath('//tr[2]/td[1]/p/b/font/text()')
##grabs unique loan transaction number (key), for use in any relational databases

#loankey_heading = "Series of Member Payment Dependent Notes"
##the correct heading for loan key

#loan_amount = tree.xpath('//tr[2]/td[2]/p/font/text()')
##grabs the amount of the loan offered

#loan_amount_heading = "Maximum aggregate principal amount offered"
##heading for loan amount

#loan_interest_rate = tree.xpath('//tr[2]/td[3]/p/font/text()')
##grabs the interest rate of the loan

#loan_interest_rate_heading = "Stated interest rate"
##heading for loan interest rate

#loan_service_charge = tree.xpath('//tr[2]/td[4]/p/font/text()')
##grabs the service charge, as a percentage, associated with the loan 

#loan_service_charge_heading = "Service Charge" 
##heading for loan interest rate

#loan_initial_maturity = tree.xpath('//tr[2]/td[5]/p/font/text()')
##grabs the initial maturity date associated with the loan 

#loan_initial_maturity_heading = "Initial maturity"
##heading for initial maturity 

#loan_final_maturity = tree.xpath('//tr[2]/td[6]/p/font/text()')
##grabs the final maturity date associated with the loan 

#loan_final_maturity_heading = "Final maturity"
##heading for final maturity 