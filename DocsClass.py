from .ClassDocs.javadoc import openURL, multiJava, getJavaDoc
from .ClassDocs.pythondoc import getPythonDoc
from .ClassDocs.rubydoc import getRubyDoc
from .ClassDocs.webdoc import getWebDoc
import sublime, sublime_plugin

css = (
    "html {background-color: #1B1B17; color: #eefbee; padding: 2px; }" +
    "body {font-size: 11px; border-color: red;}" +
    "b {color: #22aa22; }" +
    "a {color: hotpink; }" +
    "h1 {color: #cccccc; font-weight: bold; font-size: 14px; }"
)

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
                for x in getJavaDoc(selected)[0:1]:
                    doc = multiJava(x)[0]
                    url = multiJava(x)[1]

                    if len(doc) > 1:
                        sublime.status_message("LangDocs: Reading documentation ...")

                        try:
                            doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, doc, url)
                            view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                        except:
                            doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, doc, url)
                            sublime.message_dialog(doc)

                    else:
                        sublime.status_message("LangDocs: Can't find documentation")


            elif scope == "ruby":
                result = getRubyDoc(selected)[0]
                url = getRubyDoc(selected)[1]

                if len(result) > 2:
                    sublime.status_message("LangDocs: Reading documentation ...")

                    try:
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result, url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result, url)
                        sublime.message_dialog(doc)

                else:
                    sublime.status_message("LangDocs: Can't find documentation ...")

            elif scope == "css":
                url = getWebDoc(selected, "css")[0]
                result = getWebDoc(selected, "css")[1]

                if len(result) > 2:
                    sublime.status_message("LangDocs: Reading documentation ...")

                    try:
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result[:700], url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[:700], url)
                        sublime.message_dialog(doc)

                else:
                    sublime.status_message("LangDocs: Can't find documentation")

            elif scope == "html":
                url = getWebDoc(selected, "html")[0]
                result = getWebDoc(selected, "html")[1]

                if len(result) > 2:
                    # doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("LangDocs: Reading documentation ...")

                    try:
                        selected = selected.replace("</", "").replace("/>", "").replace("<","").replace(">", "")
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result[:700], url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[:700], url)
                        sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")

            elif scope == "js":
                url = getWebDoc(selected, "javascript")[0]
                result = getWebDoc(selected, "javascript")[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("LangDocs: Reading documentation ...")

                    try:

                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result[:700], url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[:700], url)
                        sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")

            elif scope == "python":
                url = str(getPythonDoc(selected)[0])
                result = getPythonDoc(selected)[1]


                if len(result) > 2:
                    sublime.status_message("LangDocs: Reading documentation ...")

                    try:
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result[:700], url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[:700], url)
                        sublime.message_dialog(doc)

                else:
                    sublime.status_message("LangDocs: Can't find documentation")

        except ValueError as e:
            sublime.status_message("LangDocs: Can't find documentation")