import re 
#imports module for regex string matching
from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)
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
	if re.match("(.*)(salessup_)(.*)", lines):
		a = lines.strip() 
		tree = lh.parse(a)
		
		class Loan: 
		#define a class "Loan" which grabs the relevant data from the loan table in the filing
		#grabs data as lists (the brackets for the heading (e.g. self.key_heading) makes it a list format)
		#The class also includes the variable headings as hard-coded, single element lists (e.g. key, Service Charge, Initial maturity, etc.)
		#These paths are defined as a class so the elements (e.g. key, amount) are accesible as methods (e.g. loan.amount)

			def __init__(self):
				self.key = tree.xpath('//tr[2]/td[1]/p/b/font/text()')
				self.key_heading = ["Series of Member Payment Dependent Notes"]
				self.offered = tree.xpath('//tr[2]/td[2]/p/font/text()')
				self.offered_heading = ["Maximum aggregate principal amount of Notes offered"]
				self.sold = tree.xpath('//tr[2]/td[3]/p/font/text()')
				self.sold_heading = ["Aggregate principal amount of Notes sold"]
				self.interest_rate = tree.xpath('//tr[2]/td[4]/p/font/text()')
				self.interest_rate_heading = ["Stated interest rate"]
				self.service_charge = tree.xpath('//tr[2]/td[5]/p/font/text()')
				self.service_charge_heading = ["Service Charge"] 
				self.date = tree.xpath('//tr[2]/td[6]/p/font/text()')
				self.date_heading = ["Sale and Original Issue Date"]
				self.initial_maturity = tree.xpath('//tr[2]/td[7]/p/font/text()')
				self.initial_maturity_heading = ["Initial maturity"]
				self.final_maturity = tree.xpath('//tr[2]/td[8]/p/font/text()')
				self.final_maturity_heading = ["Final maturity"]
				self.lc = tree.xpath('//tr[2]/td[9]/p/font/text()')
				self.lc_heading = ["Amount of corresponding loan funded by Lending Club"]


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
				self.mortgage = tree.xpath('//tr[./td[contains(., "Home ownership")]]/td[2]/font/text()')
				self.mortgage_heading = ["Home ownership"]
				self.income = tree.xpath('//tr[./td[contains(., "Home ownership")]]/td[4]/font/text()')
				self.income_heading = ["Gross income"]
				self.debt = tree.xpath('//tr[./td[contains(., "Debt-to-income ratio:")]]/td[4]/font/text()')
				self.debt_heading = ["Debt-to-income ratio"]
				self.tenure = tree.xpath('//tr[./td[contains(., "Length of employment:")]]/td[2]/font/text()')
				self.tenure_heading = ["Length of employment"]
				self.location = tree.xpath('//tr[./td[contains(., "Length of employment:")]]/td[4]/font/text()')
				self.location_heading = ["Location"]
				self.hometown = tree.xpath('//tr[./td[contains(., "Home town:")]]/td[2]/font/text()')
				self.hometown_heading = ["Home town"]
				self.pastemployers = tree.xpath('//tr[./td[contains(., "Current & past employers:")]]/td[2]/font/text()')
				self.pastemployers_heading = ["Current & past employers"]
				self.currentemployers = tree.xpath('//tr[./td[contains(., "Current & past employers:")]]/td[2]/font/text()')
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
				self.csrange = tree.xpath('//tr[./td[contains(., "Credit Score Range:")]]/td[2]/font/text()')
				self.csrange_heading = ["Credit Score Range"]
				self.accountsdelinq = tree.xpath('//tr[./td[contains(., "Credit Score Range:")]]/td[4]/font/text()')
				self.accountsdelinq_heading = ["Accounts Now Delinquent"]
				self.earliest = tree.xpath('//tr[./td[contains(., "Earliest Credit Line:")]]/td[2]/font/text()')
				self.easliest_heading = ["Earliest Credit Line"]
				self.amountdelinq = tree.xpath('//tr[./td[contains(., "Earliest Credit Line:")]]/td[4]/font/text()')
				self.amountdelinq_heading = ["Delinquent Amount"]
				self.openlines = tree.xpath('//tr[./td[contains(., "Open Credit Lines:")]]/td[2]/font/text()')
				self.openlines_heading = ["Open Credit Lines"]
				self.countdelinq = tree.xpath('//tr[./td[contains(., "Open Credit Lines:")]]/td[4]/font/text()')
				self.countdelinq_heading = ["Delinquencies (Last 2 years)"]
				self.totalines = tree.xpath('//tr[./td[contains(., "Total Credit Lines:")]]/td[2]/font/text()')
				self.totalines_heading = ["Total Credit Lines"]
				self.delinqfree = tree.xpath('//tr[./td[contains(., "Total Credit Lines:")]]/td[4]/font/text()')
				self.delinqfree_heading = ["Months Since Last Delinquency"]
				self.balance = tree.xpath('//tr[./td[contains(., "Revolving Credit Balance:")]]/td[2]/font/text()')
				self.balance_heading = ["Revolving Credit Balance"]
				self.publicrecords = tree.xpath('//tr[./td[contains(., "Revolving Credit Balance:")]]/td[4]/font/text()')
				self.publicrecords_heading = ["Public Records on File"]
				self.utilization = tree.xpath('//tr[./td[contains(., "Revolving Line Utilization:")]]/td[2]/font/text()')
				self.utilization_heading = ["Revolving Line Utilization"]
				self.lastrecord = tree.xpath('//tr[./td[contains(., "Revolving Line Utilization:")]]/td[4]/font/text()')
				self.lastrecord_heading = ["Months Since Last Record"]
				self.inquiries = tree.xpath('//tr[./td[contains(., "Inquiries in the Last 6 Months:")]]/td[2]/font/text()')
				self.inquiries_heading = ["Inquiries in the Last 6 Months"]


		credit = Credit()
		#instantiate the Credit class with a single instance, "credit"

		## data scrapping section has ended ##


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
		#see note starting on line 132

		if not borrower.job:
			for i in loan.key:
				borrower.job.append("N/a")
		#see note starting on line 132

		if not borrower.education:
			for i in loan.key:
				borrower.education.append("N/a")
		#see note starting on line 132

		if not borrower.hometown:
			for i in loan.key:
				borrower.hometown.append("N/a")
		#see note starting on line 132

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
		#see note starting on line 164

		if len(borrower.debt) != len(loan.key):
			borrower.debt = []
			for i in loan.key: 
				borrower.debt.append("__")
		#see note starting on line 164

		if len(borrower.tenure) != len(loan.key):
			borrower.tenure = []
			for i in loan.key: 
				borrower.tenure.append("__")
		#see note starting on line 164

		if len(borrower.location) != len(loan.key):
			borrower.location = []
			for i in loan.key: 
				borrower.location.append("__")
		#see note starting on line 164

		if len(borrower.hometown) != len(loan.key):
			borrower.hometown = []
			for i in loan.key: 
				borrower.hometown.append("__")
		#see note starting on line 164

		if len(borrower.pastemployers) != len(loan.key):
			borrower.pastemployers = []
			for i in loan.key: 
				borrower.pastemployers.append("__")
		#see note starting on line 164

		if len(borrower.currentemployers) != len(loan.key):
			borrower.currentemployers = []
			for i in loan.key: 
				borrower.currentemployers.append("__")
		#see note starting on line 164

		if len(borrower.job) != len(loan.key):
			borrower.job = []
			for i in loan.key: 
				borrower.job.append("__")
		#see note starting on line 164

		if len(borrower.education) != len(loan.key):
			borrower.education = []
			for i in loan.key: 
				borrower.education.append("__")
		#see note starting on line 171

		##end section adjusting for optional borrower entries##

		## section for exporting to csv begins ##

		csv_out = open('salesup' + str(c) + '.csv', 'wb')
		#open a file for writing called sales_old_format.csv, 'wb' puts it in writing mode

		#csv_out = open('sales_new_format.csv', 'wb')
		#open a file for writing called sales_new_format.csv, 'wb' puts it in writing mode

		mywriter = csv.writer(csv_out)
		#instantiate a csv writer object 


		rows_headings = zip(loan.key_heading, loan.offered_heading, loan.sold_heading, loan.interest_rate_heading, 
			loan.service_charge_heading, loan.date_heading, loan.initial_maturity_heading, loan.final_maturity_heading, loan.lc_heading, borrower.mortgage_heading,
			 borrower.income_heading, borrower.debt_heading, borrower.tenure_heading, borrower.location_heading, borrower.hometown_heading, 
			 borrower.pastemployers_heading, borrower.currentemployers_heading, borrower.job_heading, borrower.education_heading, 
			 credit.csrange_heading, credit.accountsdelinq_heading, credit.easliest_heading, credit.amountdelinq_heading, 
			 credit.openlines_heading, credit.countdelinq_heading, credit.totalines_heading, credit.delinqfree_heading, 
			 credit.balance_heading, credit.publicrecords_heading, credit.utilization_heading, credit.lastrecord_heading, credit.inquiries_heading)
		#zips the variable headings together into a single list 

		rows_values = zip(loan.key, loan.offered, loan.sold, loan.interest_rate, loan.service_charge, loan.date, loan.initial_maturity, 
			loan.final_maturity, loan.lc, borrower.mortgage, borrower.income, borrower.debt, borrower.tenure, borrower.location, borrower.hometown, borrower.pastemployers, 
			borrower.currentemployers, borrower.job, borrower.education, credit.csrange, credit.accountsdelinq, credit.earliest, 
			credit.amountdelinq, credit.openlines, credit.countdelinq, credit.totalines, credit.delinqfree, credit.balance, 
			credit.publicrecords, credit.utilization, credit.lastrecord, credit.inquiries) 
		#zips the loan and borrower variables into a series of lists, one list per loan 
			

		rows = rows_headings + rows_values
		#combines the headings list (as the first row) with the row_values lists 

		mywriter.writerows(rows)
		#writes the rows (remember rows = rows_headings + rows_values) to the csv file 


		csv_out.close()
		#closes the csv file

		##end export to csv section##

		print str(c) + ': ' + str(len(rows)) + ' rows'
			#prints count and length of rows in each csv file, in part so you can track progress

		c = c + 1 
	#prints done in command line so it is easy to see when operation is finished
