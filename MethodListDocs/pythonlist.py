import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

def getPythonFunc(text):
	module_url = "https://docs.python.org/3/library/%s.html" % text

	try:
		class_link = str(urlopen(module_url).read())
	except: return

	try:
		class_link = class_link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&trade;", "(TM)").replace("&#8212;", "--").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\n", " ").replace("\t", "").replace("\r", "").replace("&#8217;", "'")

		value = (re.findall(r'[\w\_]+\.</code><code class="descname">(.*?)<a class=' , class_link))


		pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
		# description = pattern.sub(" ", "".join(result))
		for x in value:
			y = pattern.sub("", x).replace(")", ")#").split("#")[0]
			value[value.index(x)] = y

		# print(value)
		main = []; others = [];

		for x in value:
			if x[0].islower() and x.endswith(")"):
				main.append(x)
			else:
				others.append(x)

		meth_main = "; ".join(sorted(set(main)))
		other_main = "; ".join(sorted(set(others)))

		return meth_main, other_main, module_url
	except : return