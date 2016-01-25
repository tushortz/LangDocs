import re
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen


def getJavaPackDoc(text):
	main_url = "https://docs.oracle.com/javase/8/docs/api/%s"
	url = main_url % "overview-summary.html"

	try:
		link = str(urlopen(url).read())
	except: return "\nConnection could not be established ..."

	link = link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("\n", " ").replace("\t", "").replace("\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("  ", " ").replace("&trade;", "(TM)")

	description = re.findall(r'"><a href="([\w\d\\\/\-\_\.]+)">%s</a>(.*?)</div> </td>' % text.strip(), link)

	if len(description) > 0:
		pattern = re.compile(r'<.*?>')
		doc = pattern.sub("", "".join(description[0][1]))

		pattern = re.compile(r'\s{2,10}')
		doc = pattern.sub("", doc)

		url = description[0][0]

		return doc, main_url % url
	else:
		return "Documentation not found.", "%s" % url