from .PackageDocs.javapac import getJavaPackDoc
import sublime, sublime_plugin, webbrowser

css = (
    "html {background-color: #1B1B17; color: #eefbee; padding: 2px; }" +
    "body {font-size: 11px; border-color: red;}" +
    "b {color: #22aa22; }" +
    "a {color: hotpink; }" +
    "h1 {color: #cccccc; font-weight: bold; font-size: 14px; }"
)

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
                sublime.status_message("LangDocs: Looking up package definition")
                doc = getJavaPackDoc(selected)[0]
                url = getJavaPackDoc(selected)[1]

                if len(doc) > 2:
                    try:
                        doc =  "<h1>%s documentation</h1><br>%s ... <br><br>Read more at: \"<a href=\"%s\">%s</a>\"" % (selected, doc, url, url)
                        view.show_popup("<style>%s</style>%s" % (css, doc), max_width=700,
                            on_navigate=lambda x:(webbrowser.open(url)))

                    except:
                        doc =  "%s documentation\n\n%s ... \n\nRead more at: \"%s\"" % (selected, doc, url)
                        sublime.message_dialog(doc)

                else:
                    sublime.status_message("LangDocs: Can't find documentation")
        except:
            sublime.status_message("LangDocs: Can't find documentation")