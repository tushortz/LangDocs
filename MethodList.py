from .MethodListDocs.javalist import getMethods
from .MethodListDocs.pythonlist import getPythonFunc
from .MethodListDocs.rubylist import getRubyFunc
from .MethodListDocs.webfuncattr import getWebFunc
import sublime, sublime_plugin, re, webbrowser

css = (
    "html {background-color: #1B1B17; color: #eefbee; padding: 2px; }" +
    "body {font-size: 11px; border-color: red;}" +
    "b {color: #22aa22; }" +
    "a {color: hotpink; }" +
    "h1 {color: #cccccc; font-weight: bold; font-size: 14px; }"
)

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

                doc = getMethods(selected)[0]
                url = getMethods(selected)[1]

                sublime.status_message("Searching for methods ...")

                try:
                    doc =  "<h1>%s</h1><br>%s<br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (selected, doc.replace("\n", "<br>"), url, url)
                    view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                            on_navigate=lambda x:(webbrowser.open(url)))
                except:
                    doc =  "%s Fields and Methods\n\n%s \n\nRead more at: \"%s\"" % (selected, doc, url)
                    sublime.message_dialog(doc)

            elif scope == "ruby":
                result = getRubyFunc(selected)[0]
                url = getRubyFunc(selected)[1]

                try:
                    doc =  "<h1>%s Methods</h1><br>%s ... <br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (selected, result.replace("\n", "<br>"), url, url)
                    view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                            on_navigate=lambda x:(webbrowser.open(url)))
                except:
                    doc =  "%s Fields and Methods\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.message_dialog(doc)

            elif scope == "html":
                url = getWebFunc(selected, "html")[0]
                result = getWebFunc(selected, "html")[1]

                if len(result) > 2:
                    try:
                        doc =  "<h1>%s Attributes</h1><br>%s <br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (selected, result.replace("\n", "<br>"), url, url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                            on_navigate=lambda x:(webbrowser.open(url)))
                    except:
                        doc =  "%s Fields and Methods\n\n%s\n\nRead more at: \"%s\"" % (selected, result, url)
                        sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find attributes")

            elif scope == "css":
                url = str(getWebFunc(selected, "css")[0])
                result = getWebFunc(selected, "css")[1]

                if len(result) > 2:
                    sublime.status_message("Reading documentation ...")
                try:
                    doc =  "<h1>%s values</h1><br>%s<br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (selected, result, url, url)
                    view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                        on_navigate=lambda x:(webbrowser.open(url)))
                except:
                    doc =  "%s values\n\n%s \n\nRead more at: \"%s\"" % (selected, result, url)
                    sublime.message_dialog(doc)

            elif scope == "js":
                url = str(getWebFunc(selected, "javascript")[0])
                result = getWebFunc(selected, "javascript")[1]

                if len(result) > 2:
                    sublime.status_message("Reading documentation ...")

                    try:
                        doc =  "<h1>%s Method and Properties</h1><br>%s<br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (selected, result, url, url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                            on_navigate=lambda x:(webbrowser.open(url)))
                    except:
                        doc =  "%s Methods and properties\n\n%s \n\nRead more at: \"%s\"" % (selected, result, url)
                        sublime.message_dialog(doc)


            elif scope == "python":
                mainlist = getPythonFunc(selected)[0]
                otherlist = getPythonFunc(selected)[1]
                url = getPythonFunc(selected)[2]

                sublime.status_message("Reading documentation ...")

                try:
                    doc =  "<h1>%s Method Lists</h1><br>%s <br><br><h1>%s Constants and Others </h1><br>%s <br><br>Read more at: \"<a href=\"%s\">%s<a>\"" % (selected, mainlist, selected, otherlist, url, url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                            on_navigate=lambda x:(webbrowser.open(url)))

                except:
                    if len(mainlist) > 0:
                        doc =  "%s Method Lists\n\n%s ... \n\nRead more at: \"%s\"" % (selected, mainlist, url)
                        sublime.message_dialog(doc)

                    if len(otherlist) > 0:
                        doc =  "%s Constants and others\n\n%s \n\nRead more at: \"%s\"" % (selected, otherlist, url)
                        sublime.message_dialog(doc)

        except:
            sublime.status_message("Can't find result")