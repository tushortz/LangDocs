from .ClassDocs.javadoc import openURL, multiJava, getJavaDoc
from .ClassDocs.pythondoc import getPythonDoc
from .ClassDocs.rubydoc import getRubyDoc
from .ClassDocs.webdoc import getWebDoc
import sublime, sublime_plugin


class Class_docsCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout_async(self.getClassData, 0)


    def getClassData(self):
        window = self.window
        view = window.active_view()
        selText = view.sel()[0]
        xt = str(window.active_view().file_name())

        scope = (view.scope_name(0).split(" ")[0].split(".")[1])
        selected = view.substr(selText)

        try:
            if scope == "java":
                for x in getJavaDoc(selected):
                    doc = multiJava(x)[0]
                    url = multiJava(x)[1]

                    if len(doc) > 1:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, doc, url)
                        sublime.status_message("LangDocs: Reading documentation ...")
                        sublime.message_dialog(doc)
                    else:
                        sublime.status_message("LangDocs: Can't find documentation")


            elif scope == "ruby":
                result = getRubyDoc(selected)[0]
                url = getRubyDoc(selected)[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.status_message("LangDocs: Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation ...")

            elif scope == "css":
                url = getWebDoc(selected, "css")[0]
                result = getWebDoc(selected, "css")[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("LangDocs: Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")

            elif scope == "html":
                url = getWebDoc(selected, "html")[0]
                result = getWebDoc(selected, "html")[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("LangDocs: Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")

            elif scope == "js":
                url = getWebDoc(selected, "javascript")[0]
                result = getWebDoc(selected, "javascript")[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("LangDocs: Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")

            elif scope == "python":
                url = str(getPythonDoc(selected)[0])
                result = getPythonDoc(selected)[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("LangDocs: Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")

        except:
            sublime.status_message("LangDocs: Can't find documentation")