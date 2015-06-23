import mechanize
import cookielib
import time
import getpass


URL = "https://cms.iyte.edu.tr/login/index.php"
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
openPage = br.open(URL)

print "Welcome to IZTECH CMS News Checker:"

mail = raw_input('Please enter your e-mail prefix: (without @std.iyte.edu.tr)')
password = getpass.getpass('Please enter your password: ')
#password = raw_input('Please enter your password:')

br.select_form(nr=0)
br.form['usernamef'] = mail
br.form['password'] = password
br.submit()
print "Submitting your information please wait..."

time.sleep(2)

#print br.geturl()
print br.title()

html_source = br.response().read()

if "There are new forum posts" in html_source:
	print "News On Cms!"
else:
	print "Nothing new."

