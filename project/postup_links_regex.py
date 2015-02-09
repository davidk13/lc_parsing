import re

imp = open("finished_links.txt", "r")
output = open("postup_links.txt", "w")

for line in imp:
	if re.match("(.*)(postingsup|postsup)(.*)", line):
		print >> output, line 
