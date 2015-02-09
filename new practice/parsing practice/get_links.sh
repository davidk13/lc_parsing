#!/bin/bash

# Where the search links will go
INTERMEDIATE_FILE="search_links.txt"
# Where the final links (for analysis) will go
OUTPUT_FILE="final_links.txt"
# Stop after 8000 results. 
# Increase if there are more
STOP=300
C=0
# Get all of the search results
until [ $C -ge $STOP ]; do
  curl "http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001409970&type=&dateb=[20091015:20151015:10000]&owner=exclude&start=[0-2000:100]&count=100&output=atom" 2>/dev/null | grep "link href" | grep -v "cgi-bin" | egrep -o 'http[^"]+' >> $INTERMEDIATE_FILE 2>/dev/null
  # Didn't bother to look up better way to do this
  echo "Search Links `expr ${C} + 1`-`expr ${C} + 100` Done"
  let C+=100
  sequ=$C
done

# For each search result, find the relevant link
while read link
do
  curl $link 2>/dev/null | egrep "(postsup|postingsup|salessup)" | egrep -o '/Archives[^"]+' | sed -e "s/^/http\:\/\/www.sec.gov/g" >> $OUTPUT_FILE
done < $INTERMEDIATE_FILE

print "Finished"
# Uncomment to delete search links file
#rm $INTERMEDIATE_FILE