from lxml import html
#uses lxml library for parsing html (lxml can also be used for xml)
import requests
#uses requests module, rather than built in urlib2, because of improved speed and readability

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
#uses get method to retreieve webpage and data
tree = html.fromstring(page.text)
#parse webpage into tree structure

info = tree.xpath('//div/text()')

print info
