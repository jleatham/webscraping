import requests, bs4,sys
print "\nWebscrape program - This will search for any element on any website that you request"
print "\nPress enter at prompts for an example scrape"
website = raw_input('Enter the URL to scrape: ')
if len(website) > 0:
	print "\n"
else:
	website = 'http://weather.gov/77459'
	print "Website = http://weather.gov/77459"
	print "\n"

print "You can find the web element you need by using your web browser's developer tools.  It is usually F12 on your keyboard to pull it.  You can then navigate the HTML code until the element is highlighted.  Google BeautifulSoup 4 for more info on the elements.\n"

element = raw_input('Enter the element: ')
if len(element) > 0:
	print "\n"
else:
	element = '.myforecast-current-lrg'
	print "Element = .myforecast-current-lrg"
	print "\n"

weatherSite = requests.get(website)
try:
        weatherSite.raise_for_status()
except Exception as exc:
        print('There was a problem: %s' % (exc))
weatherSoup = bs4.BeautifulSoup(weatherSite.text, "html.parser")
elems = weatherSoup.select(element)

if len(elems) > 0:
	print elems[0].getText()
else:
	print "Could not find HTML element"


