import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

def getMatlabFuncDoc(text):
	func_url = "http://uk.mathworks.com/help/matlab/ref/%s.html" % text.lower()

	try:
		class_link = str(urlopen(func_url).read())
	except: return

	try:
		class_link = class_link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("\\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&trade;", "(TM)").replace("&#8212;", "--").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\n", " ").replace("\t", "").replace("\r", "").replace("&#8217;", "'").replace("&#x00AE;", "(R)")


		value = (re.findall(r'">Description</h2>(.*?)</p></div>' , class_link))
		result = "".join((value[0:3]))

		pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
		description = pattern.sub(" ", result)

		pattern = re.compile(r'\s{2,10}')
		description = pattern.sub(" ", description).strip()

		return func_url, description[:720]
	except ValueError: return