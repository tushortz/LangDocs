from .ClassDocs.dictionary import getDictWords
import sublime, sublime_plugin

class AntonymsCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime.set_timeout_async(self.getWordInfo, 0)

	def getWordInfo(self):
		window = self.window
		view = window.active_view()
		selText = view.sel()[0]
		xt = str(window.active_view().file_name())

		scope = (view.scope_name(0).split(" ")[0].split(".")[1])
		selected = view.substr(selText)

		try:
			if scope == "plain":
				url = getDictWords(selected, "antonyms")[0]
				spell = getDictWords(selected, "antonyms")[1]
				result = getDictWords(selected, "antonyms")[2]
				text = selected[0].title() + selected[1:]

				if len(result) > 2:
					doc =  "Antonym of \"%s\" %s\n\n%s \n\nRead more at: \"%s\"" % (text, spell, result, url)
					sublime.status_message("LangDocs: Looking up word ...")
					sublime.message_dialog(doc)
				else:
					sublime.status_message("LangDocs: Can't find word")
		except:
			sublime.status_message("LangDocs: Can't find word")


class DefinitionCommand(sublime_plugin.WindowCommand):
	def run(self):
		sublime.set_timeout_async(self.getWordInfo, 0)

	def getWordInfo(self):
		window = self.window
		view = window.active_view()
		selText = view.sel()[0]
		xt = str(window.active_view().file_name())

		scope = (view.scope_name(0).split(" ")[0].split(".")[1])
		selected = view.substr(selText)

		try:
			if scope == "plain":
				url = getDictWords(selected, "definition")[0]
				spell = " - " + getDictWords(selected, "definition")[1]
				result = getDictWords(selected, "definition")[2]
				text = selected[0].title() + selected[1:]

				if len(result) > 2:
					doc =  "%s Meaning%s\n\n%s\n\nRead more at: \"%s\"" % (text, spell, result, url)
					sublime.status_message("LangDocs: Looking up word ...")
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
		xt = str(window.active_view().file_name())

		scope = (view.scope_name(0).split(" ")[0].split(".")[1])
		selected = view.substr(selText)

		try:
			if scope == "plain":
				url = getDictWords(selected, "synonyms")[0]
				spell = getDictWords(selected, "synonyms")[1]
				result = getDictWords(selected, "synonyms")[2]
				text = selected[0].title() + selected[1:]

				if len(result) > 2:
					doc =  "Synonym of \"%s\" %s\n\n%s \n\nRead more at: \"%s\"" % (text, spell, result, url)
					sublime.status_message("LangDocs: Looking up word ...")
					sublime.message_dialog(doc)
				else:
					sublime.status_message("LangDocs: Can't find word")

		except:
			sublime.status_message("LangDocs: Can't find word")
