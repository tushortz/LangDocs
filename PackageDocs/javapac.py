import re
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

javaseurl = "http://docs.oracle.com/javase/8/docs/api/%s/package-summary.html"
javafxurl = "https://docs.oracle.com/javase/8/javafx/api/%s/package-summary.html"


def replaced(text):

	replace_text = text.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\xe2\x80\x94", " -- ").replace("\\xe2\\x80\\x94", " -- ").replace("&#8217;", "'").replace("&para;", "|").replace("&uarr", "↑").replace("\xe2\x80\x98", "'").replace("\\xe2\\x80\\x98", "'").replace("\xe2\x80\x99", "'").replace("\\xe2\\x80\\x99", "'").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x93", "-").replace("\\xe2\\x80\\x93", "-").replace("\\xc2\\xa0", " ").replace("\xc2\xa0", " ").replace("&#8217;", "'").replace("&#8212;", "--").replace("&ndash;", "--")

	return replace_text



def openURL(text, classurl):
	text = text.replace(".", "/")
	url = classurl % text
	try:
		classurl = str(urlopen(url).read())

	except: pass
	classurl = replaced(classurl)

	class_data = re.findall(r'Description</\w2> <div class="block">(.*?)(<\w\d|<!--|</p>{2})', classurl)

	pattern = re.compile(r'<.*?>')
	doc = pattern.sub("", "".join(class_data[0][0]))

	pattern = re.compile('\s{2,10}')
	doc = pattern.sub(" ", doc)

	return (doc[:700], url)

def getJavaPackDoc(text):

	try:
		result = openURL(text, javaseurl)
		return result
	except:
		result = openURL(text, javafxurl)
		return result