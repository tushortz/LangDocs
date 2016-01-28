# Import necessary modules
import re
# Exception handling checks between python 2 and 3
try:
	from urllib2 import urlopen
except ImportError:
	from urllib.request import urlopen

# Method to parse text into dictionary link
def getDictWords(text, word_type):
	""" Takes in two arguments, text and what to find """

	# Choose between word definition, antonyms and synonyms
	if word_type == "definition":
		head = "http://dictionary.reference.com/"
	else:
		head = "http://www.thesaurus.com/"
	text = text.split(" ")[0]
	word_url = "%sbrowse/%s" % (head, text)

	# Try to open link
	try:
		class_link = str(urlopen(word_url).read())
	except: return

	# Exception handling in method body
	try:
		# Replace some html tags and unnecessary stuffs for better presentation
		class_link = class_link.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\xe2\x80\x94", " -- ").replace("\\xe2\\x80\\x94", " -- ").replace("&#8217;", "'").replace("&para;", "|").replace("&uarr", "↑").replace("\xe2\x80\x98", "'").replace("\\xe2\\x80\\x98", "'").replace("\xe2\x80\x99", "'").replace("\\xe2\\x80\\x99", "'").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x93", "-").replace("\\xe2\\x80\\x93", "-").replace("&#8212;", "--")

		# Get defiinition
		if word_type == "definition":
			value = re.findall(r'<div class="def-content">(.*?)</div>' , class_link)
			word_with_friend = "".join(re.findall('<div class="game-wwf"><span>([\d\w\s]+)</span></div>', class_link))
			scrabble = "".join(re.findall('<div class="game-scrabble"><span>([\d\w\s]+)</span></div>', class_link))

			result = "*".join((value[0:5]))

			pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
			description = pattern.sub(u" ", result)

		# Get something else
		else:
			if word_type == "antonyms":
				value = re.findall(r'"color": "#[cef][167][cef][278][cef][a28]"\}" [\w\d\s\-\"=]+> <span class="text">([\w\s\d\_\-\!\"&\*\(\)\?\'\;\:]+)</span>' , class_link)
				value = sorted(set(value))
				value = filter(str.islower, value)
				result = ", ".join((value))

			elif word_type == "synonyms":
				value = re.findall(r'"color": "#[f][bc][bde][b48][c48][e45]"\}" [\w\d\s\-\"=]+> <span class="text">([\w\s\d\_\-\!\"&\*\(\)\?\'\;\:]+)</span>' , class_link)
				value = sorted(set(value))
				value = filter(str.islower, value)
				result = ", ".join((value))

		spell = re.findall(r'spellpron">(.*?)<span class="pron', class_link)

		pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
		description = pattern.sub(u" ", result)

		pattern = re.compile(r'\s{2,10}')
		description = pattern.sub(u" ", description)

		pattern = re.compile(r'\\x[\w\d]\d|<.*?>')
		spell = pattern.sub("", "".join(spell[:1]))

		if word_type == "definition":
			description = "*" + description.replace("*", "<br>*")
			description = str(description[:700]) + "<br><br>Scrabble Point: %s<br>Word With Friends Point: %s" % (scrabble, word_with_friend)

		return word_url, spell, description
	except ValueError: return ""
