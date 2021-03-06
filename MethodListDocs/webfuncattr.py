import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen


def getWebFunc(text, web_type):
	if web_type == "css":
		url = "https://developer.mozilla.org/en-US/docs/Web/CSS/%s" % text
		reference_link = "https://developer.mozilla.org/en-US/docs/Web/CSS/Reference"

	elif web_type == "html":
		text = text.replace("<", "").replace("/", "").replace(">", "")
		url = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element/%s" % text
		reference_link = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element"

	elif web_type == "javascript":
		# For javascript
		text = text.replace("(", "").replace(")", "").replace("SIMD.", "")
		url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/%s" % text
		reference_link = "https://developer.mozilla.org/en-US/docs/Web/HTML/Element"

	try:
		property_link = str(urlopen(url).read())
	except:
		if web_type == "javascript":
			try:
				if text == "if": text = "if...else"
				if text == "do": text = "do...while"
				url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/%s" % text
				property_link = str(urlopen(url).read())
			except:
				url = "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/%s" % text
				property_link = str(urlopen(url).read())

		else:
			return reference_link, ""


	property_link = property_link.replace("\\n", "").replace("\\r", "").replace("\\t", "").replace("\n", "").replace("\r", "").replace("\t", "").replace("&nbsp;", " ").replace("&#34;", "\"").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("  ", " ").replace("&#39;", "'").replace("\\xe2\\x80\\x94", "--").replace("\xe2\x80\x94", "--").replace("\\xc2\\xa0", " ").replace("\xc2\xa0", " ").replace("&#8217;", "'")

	if web_type == "html":
		# Starting global attributes
		global_attr = ["accesskey", "class", "contenteditable", "contextmenu", "data-*", "dir", "draggable",
						"dropzone", "hidden", "id", "itemid", "itemprop", "itemref", "itemscope",
						"itemtype", "lang", "spellcheck", "style", "tabindex", "title", "translate"
					]

		description = re.findall(r'<dt><strong id="attr-[\w\s\d\-\_\.\:\;\*\@]+"><code>([\w\s\d\-\_\.\:\;\*\@]+)</code>', property_link)

		description = global_attr + description

	elif web_type == "css":
		result = re.findall(r'<dt><code>(.*?)</code>', property_link)

		description = []

		for x in result:
			x = x.replace("<" ,"").replace(">" ,"").replace("'", "")
			if len(x) > 0:
				description.append(x)

		description = sorted(set(description))

	elif web_type == "javascript":
		description = re.findall(r'<dt><.*?><code>(.*?)</code>', property_link)

	description = ", ".join(sorted(description)).replace(text + ".", "")

	if len(description) > 0:
		return url, description

	else:
		return