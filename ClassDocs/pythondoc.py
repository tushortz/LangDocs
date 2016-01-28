import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

def getPythonDoc(text):
	module_url = "https://docs.python.org/3/library/%s.html" % text.strip()

	try:
		class_link = str(urlopen(module_url).read())
	except: return

	try:
		class_link = class_link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\xe2\x80\x94", " -- ").replace("\\xe2\\x80\\x94", " -- ").replace("&#8217;", "'").replace("&para;", "|").replace("&uarr", "↑").replace("\xe2\x80\x98", "'").replace("\\xe2\\x80\\x98", "'").replace("\xe2\x80\x99", "'").replace("\\xe2\\x80\\x99", "'").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x93", "-").replace("\\xe2\\x80\\x93", "-").replace("\\xc2\\xa0", " ").replace("\xc2\xa0", " ").replace("&#8217;", "'").replace("&#8212;", "--")

		value = (re.findall(r'<code class="xref py py-mod docutils literal">(.*?)</p>' , class_link))
		result = "".join((value[0:3]))

		pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
		description = pattern.sub(" ", result)

		pattern = re.compile(r'\s{2,10}')
		description = pattern.sub(" ", description).strip()

		return module_url, description[:700]
	except : return