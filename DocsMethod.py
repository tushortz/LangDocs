from .MethodDocs.matlabdoc import getMatlabFuncDoc
from .MethodDocs.pydoc import pyFunc
import sublime, sublime_plugin

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
            if scope == "python":
                url = str(pyFunc(selected)[0])
                result = pyFunc(selected)[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find documentation")

            elif scope == "matlab":
                url = str(getMatlabFuncDoc(selected)[0])
                result = getMatlabFuncDoc(selected)[1]

                if len(result) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, result[0:700], url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("Can't find documentation")

            else:
                sublime.status_message("LangDocs: Language not yet supported")
        except:
            sublime.status_message("Can't find documentation")
