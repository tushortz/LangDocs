from .MethodListDocs.javalist import openURL, multiJava, getMethods
from .MethodListDocs.pythonlist import getPythonFunc
from .MethodListDocs.rubylist import getRubyFunc
from .MethodListDocs.webfuncattr import getWebFunc
import sublime, sublime_plugin, re, sys

class Method_listCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout_async(self.getData, 0)


    def getData(self):
        window = self.window
        view = window.active_view()
        selText = view.sel()[0]
        xt = str(window.active_view().file_name())

        scope = (view.scope_name(0).split(" ")[0].split(".")[1])
        selected = view.substr(selText)

        try:
            if scope == "java":
                javaseurl = "https://docs.oracle.com/javase/8/docs/api/%s.html"
                javaseclass_url = "https://docs.oracle.com/javase/8/docs/api/allclasses-frame.html"

                jfxurl = "https://docs.oracle.com/javase/8/javafx/api/%s.html"
                jfxclass_url = "https://docs.oracle.com/javase/8/javafx/api/allclasses-frame.html"

                for x in getMethods(selected):
                    doc = multiJava(x)[0]
                    url = multiJava(x)[1]

                    if len(doc) > 5:
                        doc =  "%s Fields and Methods\n\n%s ... \n\nRead more at: \"%s\"" % (selected, doc, url)
                        sublime.status_message("Searching for methods ...")
                        sublime.message_dialog(doc)
                    else:
                        sublime.status_message("Can't find methods")

            elif scope == "ruby":
                result = getRubyFunc(selected)[0]
                url = getRubyFunc(selected)[1]

                if len(result) > 2:
                    doc =  "%s methodsn\n\n%s\n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.status_message("Searching for methods ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find methods ...")

            elif scope == "html":
                url = getWebFunc(selected, "html")[0]
                result = getWebFunc(selected, "html")[1]

                if len(result) > 2:
                    doc =  "%s attributes\n\n%s \n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.status_message("LangDocs: Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find attributes")

            elif scope == "css":
                url = str(getWebFunc(selected, "css")[0])
                result = getWebFunc(selected, "css")[1]

                if len(result) > 2:
                    doc =  "%s values\n\n%s \n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find property values")

            elif scope == "js":
                url = str(getWebFunc(selected, "javascript")[0])
                result = getWebFunc(selected, "javascript")[1]

                if len(result) > 2:
                    doc =  "%s Methods and properties\n\n%s \n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find methods/properties")

            elif scope == "python":
                mainlist = getPythonFunc(selected)[0]
                otherlist = getPythonFunc(selected)[1]
                url = getPythonFunc(selected)[2]

                if len(mainlist) > 0:
                    doc =  "%s Method Lists\n\n%s ... \n\nRead more at: \"%s\"" % (selected, mainlist, url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find /methods")

                if len(otherlist) > 0:
                    doc =  "%s Constants and others\n\n%s \n\nRead more at: \"%s\"" % (selected, otherlist, url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
        except:
            sublime.status_message("Can't find result")

