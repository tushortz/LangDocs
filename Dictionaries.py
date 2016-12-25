from .ClassDocs.dictionary import getDictWords
import sublime, sublime_plugin, webbrowser

css = (
	"html {background-color: #1B1B17; color: #eefbee; padding: 2px; }" +
	"body {font-size: 11px; border-color: red;}" +
	"b {color: #22aa22; }" +
	"a {color: hotpink; }" +
	"h1 {color: #cccccc; font-weight: bold; font-size: 14px; }"
)

class AntonymsCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime.set_timeout_async(self.getWordInfo, 0)

	def getWordInfo(self):
		window = self.window
		view = window.active_view()
		selText = view.sel()[0]

		scope = (view.scope_name(0).split(" ")[0].split(".")[1])
		selected = view.substr(selText)

		try:
			if scope == "plain":
				sublime.status_message("LangDocs: Looking up antonyms of '%s'" % selected)
				data = getDictWords(selected, "antonyms")
				url = data[0]
				spell = data[1]
				result = data[2]
				text = selected[0].title() + selected[1:]

				if len(result) > 2:
					doc =  "<h1>Antonym of \"%s\"</h1> <b>%s</b><br/>%s <br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (text, spell, result, url, url)

					try:
						view.show_popup("<style>%s</style>%s" % (css, doc),  max_width=700,
							on_navigate=lambda x:(webbrowser.open(url)))

					except:
						doc = doc.replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<h1>", "").replace("</h1>","\n").replace("<a>", "").replace("</a>", "").replace("<br/>", "\n")
						sublime.message_dialog(doc)

				else:
					sublime.status_message("LangDocs: Can't find word")
		except Exception as e:
			sublime.status_message("LangDocs: Can't find word")


class DefinitionCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime.set_timeout_async(self.getWordInfo, 0)

	def getWordInfo(self):
		window = self.window
		view = window.active_view()
		selText = view.sel()[0]

		scope = (view.scope_name(0).split(" ")[0].split(".")[1])
		selected = view.substr(selText)

		try:
			if scope == "plain":
				sublime.status_message("LangDocs: Looking up definition of '%s'" % selected)
				data = getDictWords(selected, "definition")
				url = data[0]
				spell = " - " + data[1]
				result = data[2]
				text = selected[0].title() + selected[1:]

				if len(result) > 2:
					doc =  "<h1>%s Meaning</h1> <b>%s</b><br><br>%s<br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (text, spell, result, url, url)

					try:
						view.show_popup("<style>%s</style>%s" % (css, doc),  max_width=700, on_navigate=lambda x:(webbrowser.open(url)))

					except:
						doc = doc.replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<h1>", "").replace("</h1>","").replace("<a>", "").replace("</a>", "").replace("<br/>", "\n")
						sublime.message_dialog(doc)

				else:
					sublime.status_message("LangDocs: Can't find word")
			else:
				sublime.status_message("LangDocs: Use only on plain text files")
		except:
			sublime.status_message("LangDocs: Can't find word")

class SynonymsCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime.set_timeout_async(self.getWordInfo, 0)

	def getWordInfo(self):
		window = self.window
		view = window.active_view()
		selText = view.sel()[0]

		scope = (view.scope_name(0).split(" ")[0].split(".")[1])
		selected = view.substr(selText)

		try:
			if scope == "plain":
				sublime.status_message("LangDocs: Looking up synonyms of '%s'" % selected)
				data = getDictWords(selected, "synonyms")
				url = data[0]
				spell = data[1]
				result = data[2]
				text = selected[0].title() + selected[1:]

				if len(result) > 2:
					doc =  "<h1>Synonyms of \"%s\"</h1> <b>%s</b><br/>%s <br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (text, spell, result, url, url)

					try:
						view.show_popup("<style>%s</style>%s" % (css, doc),  max_width=700,
							on_navigate=lambda x:(webbrowser.open(url)))

					except:
						doc = doc.replace("<br>", "\n").replace("<b>", "").replace("</b>", "").replace("<h1>", "").replace("</h1>","\n").replace("<a>", "").replace("</a>", "").replace("<br/>", "\n")
						sublime.message_dialog(doc)
				else:
					sublime.status_message("LangDocs: Can't find word")

		except:
			sublime.status_message("LangDocs: Can't find word")
