# Import necessary modules
import re
# Exception handling checks between python 2 and 3
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

# Method to replace unwanted characters
def replacer(text):
	return (
		text.replace("\\n", " ").replace("\\t", "").replace("\\r", "")
		.replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"")
		.replace("\\;", "").replace("\\'", "'").replace("&lt;", "<")
		.replace("&gt;", ">").replace("&#8220;", "\"").replace("&#8221;", "\"")
		.replace("\xe2\x80\x94", " -- ").replace("\\xe2\\x80\\x94", " -- ")
		.replace("&#8217;", "'").replace("&para;", "|").replace("&uarr", "↑")
		.replace("\xe2\x80\x98", "'").replace("\\xe2\\x80\\x98", "'")
		.replace("\xe2\x80\x99", "'").replace("\\xe2\\x80\\x99", "'")
		.replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"")
		.replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"")
		.replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"")
		.replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"")
		.replace("\xe2\x80\x93", "-").replace("\\xe2\\x80\\x93", "-")
		.replace("&#8212;", "--")
	)

# Method to parse text into dictionary link
def getDictWords(text, word_type):
	""" Takes in two arguments, text and what to find """

	# Choose between word definition, antonyms and synonyms
	if word_type == "definition":
		head = "http://dictionary.reference.com/"
	else:
		head = "http://www.thesaurus.com/"
	word_url = "%sbrowse/%s" % (head, text)

	# Try to open link
	try:
		url_data = str(urlopen(word_url).read())
	except: return

	# Exception handling in method body
	try:
		# Replace some html tags and unnecessary stuffs for better presentation
		url_data = replacer(url_data)

		spell = re.findall(r'spellpron">(.*?)<span class="pron', url_data)[0:1]
		pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
		spell = pattern.sub("", "".join(spell)).strip()


		# Get defiinition
		if word_type == "definition":
			value = re.findall(r'<div class="def-content">(.*?)</div>' , url_data)
			word_with_friend = "".join(re.findall('<div class="game-wwf"><span>([\d\w\s]+)</span></div>', url_data))
			scrabble = "".join(re.findall('<div class="game-scrabble"><span>([\d\w\s]+)</span></div>', url_data))

			result = "*".join((value[0:5]))

			pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
			description = pattern.sub(u" ", result)

			pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
			description = pattern.sub(u" ", result)

			pattern = re.compile(r'\s{2,10}')
			description = pattern.sub(u" ", description)

			description = "*" + description.replace("*", "<br>*")
			description = str(description[:700]) + "<br><br>Scrabble Point: %s<br>Word With Friends Point: %s" % (scrabble, word_with_friend)

			return word_url, spell, description

		# Get something else
		else:
			if word_type == "synonyms":
				value = re.findall(r'data-category="\{"name": "relevant-\d+", .*?\}" data-complexity="\d+" .*?<span class="text">(.*?)</span>', url_data)
				value = list(set(value[:30]))
				result = ", ".join((value))

			elif word_type == "antonyms":
				value = re.findall(r'data-category="\{"name": "relevant--\d+", .*?\}" data-complexity="\d+" .*?<span class="text">(.*?)</span>', url_data)
				value = list(set(value[:30]))

			result = ", ".join((value))
			return word_url, spell, result


	except ValueError: return ""

print(getDictWords("excellent", "antonyms"))