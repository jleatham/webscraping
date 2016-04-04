import requests, bs4,sys
website = raw_input('Enter the URL to scrape: ')
if len(website) > 0:
	print "\n"
else:
	website = 'http://www.pythonforbeginners.com'
	print "\n"


element = '.a'
webRequest = requests.get(website)
try:
        webRequest.raise_for_status()
except Exception as exc:
        print('There was a problem: %s' % (exc))
webSoup = bs4.BeautifulSoup(webRequest.text, "html.parser")
elems = webSoup.select(element)

if len(elems) > 0:
	print elems[0].getText()
else:
	print "Could not find HTML element"

title = webSoup.find_all("title")
print "Title: ",title
ptitle = webSoup.find_all("p","title")
print "p,title: ",ptitle
#a = webSoup.find_all("a")
#print "a: ",a

#print webSoup.prettify()
print webSoup.get_text()

