import re

imp = open("finished_links.txt", "r")
output = open("salesup_links.txt", "w")

for line in imp:
	if re.match("(.*)(salessup)(.*)", line):
		print >> output, line 
