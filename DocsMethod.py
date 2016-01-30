from .MethodDocs.matlabdoc import getMatlabFuncDoc
from .MethodDocs.pydoc import pyFunc
from .MethodDocs.javainherit import getOthers
import sublime, sublime_plugin

css = (
    "html {background-color: #1B1B17; color: #eefbee; padding: 2px; }" +
    "body {font-size: 11px; border-color: red;}" +
    "b {color: #22aa22; }" +
    "a {color: hotpink; }" +
    "h1 {color: #cccccc; font-weight: bold; font-size: 14px; }"
)

class Method_docsCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout_async(self.getFuncData, 0)


    def getFuncData(self):
        window = self.window
        view = window.active_view()
        selText = view.sel()[0]
        xt = str(window.active_view().file_name())

        scope = (view.scope_name(0).split(" ")[0].split(".")[1])
        selected = view.substr(selText)

        try:
            if scope == "java":

                doc = getOthers(selected)[0]
                url = getOthers(selected)[1]

                sublime.status_message("Searching for methods ...")

                try:
                    doc =  "<h1>%s</h1><br>%s<br><br>Read more at: \"<a>%s</a>\"" % (selected, doc.replace("\n", "<br>"), url)
                    view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)
                except:
                    doc =  "%s Fields and Methods\n\n%s \n\nRead more at: \"%s\"" % (selected, doc, url)
                    sublime.message_dialog(doc)

            elif scope == "python":
                url = (pyFunc(selected)[0])
                result = pyFunc(selected)[1]

                if len(result) > 2:
                    sublime.status_message("Reading documentation ...")

                    try:
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result[:700], url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[:700], url)
                        sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find documentation")

            elif scope == "matlab":
                url = str(getMatlabFuncDoc(selected)[0])
                result = getMatlabFuncDoc(selected)[1]

                if len(result) > 2:
                    sublime.status_message("Reading documentation ...")

                    try:
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a>%s</a>\"" % (selected, result[:700], url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700)

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[:700], url)
                        sublime.message_dialog(doc)
            else:
                sublime.status_message("LangDocs: Language not yet supported")
        except:
            sublime.status_message("Can't find documentation")