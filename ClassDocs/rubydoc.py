import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

def getRubyDoc(text):
	text = text.replace("::", "/")
	url = "http://ruby-doc.org/core-2.3.0/%s.html" % text

	try:
		class_link = str(urlopen(url).read())
	except: return

	class_link = class_link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\xe2\x80\x94", " -- ").replace("\\xe2\\x80\\x94", " -- ").replace("&#8217;", "'")

	class_data = re.findall(r'class="description">(.*)<!-- description -->', class_link)

	pattern = re.compile(r'<.*?>')
	result = pattern.sub(u" ", "".join(class_data))

	pattern = re.compile(r'\s{2,10}')
	result = pattern.sub(u" ", result.strip())

	return result[:700], url