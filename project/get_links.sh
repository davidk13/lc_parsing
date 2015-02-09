#!/bin/bash

# Where the search links will go
INTERMEDIATE_FILE="search_links.txt"
# Where the final links (for analysis) will go
OUTPUT_FILE="final_links.txt"
# Stop after 8000 results. 

curl "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001409970&type=&dateb=[20091015-20151015:10000]&owner=exclude&start=[0-2000:100]&count=100&output=atom" 2>/dev/null | grep "link href" | grep -v "cgi-bin" | egrep -o 'http[^"]+' >> $INTERMEDIATE_FILE 2>/dev/null

# Didn't bother to look up better way to do this
echo "Search Links Done"

awk '!a[$0]++' search_links.txt

# For each search result, find the relevant link
while read link
do
  curl $link 2>/dev/null | egrep "(postsup|postingsup|salessup)" | egrep -o '/Archives[^"]+' | sed -e "s/^/http\:\/\/www.sec.gov/g" >> $OUTPUT_FILE
done < $INTERMEDIATE_FILE

awk '!a[$0]++' final_links.txt > finished_links.txt

echo "Finished"
# Uncomment to delete search links file
#rm $INTERMEDIATE_FILE