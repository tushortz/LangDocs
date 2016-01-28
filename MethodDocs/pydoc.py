import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

def pyFunc(text):
	built_in_url = "https://docs.python.org/3/library/functions.html"
	text = text.replace("(", "").replace(")", "")

	funcs = ["dict", "frozenset", "list", "memoryview", "range", "set", "str", "tuple"]
	for func in funcs:
		if text == func:
			text = "func-" + text

	try:
		class_link = str(urlopen(built_in_url).read())
	except: pass

	try:
		class_link = class_link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("  ", " ").replace("&trade;", "(TM)").replace("&#8212;", "--").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("&#8217;", "'")

		value = (re.findall(r'id="%s">(.*?)</dd>' % text, class_link))
		result = "".join(value)

		if len(value) > 0:
			pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
			description = pattern.sub(u" ", result)

			pattern = re.compile(r'\s{2,10}')
			description = pattern.sub(u" ", description)

			return built_in_url + "#" + text, description[:700]

	except: pass
