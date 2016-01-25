from .PackageDocs.javapac import getJavaPackDoc
import sublime, sublime_plugin


class Package_docsCommand(sublime_plugin.WindowCommand):
    def run(self):
        sublime.set_timeout_async(self.getPackageData, 0)


    def getPackageData(self):
        window = self.window
        view = window.active_view()
        selText = view.sel()[0]
        xt = str(window.active_view().file_name())

        scope = (view.scope_name(0).split(" ")[0].split(".")[1])
        selected = view.substr(selText)

        try:
            if scope == "java":
                doc = getJavaPackDoc(selected)[0]
                url = getJavaPackDoc(selected)[1]

                if len(doc) > 2:
                    doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, doc, url)
                    sublime.status_message("Reading documentation ...")
                    sublime.message_dialog(doc)
                else:
                    sublime.status_message("LangDocs: Can't find documentation")
        except:
            sublime.status_message("LangDocs: Can't find documentation")