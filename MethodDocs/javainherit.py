import re
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

javaseurl = "https://docs.oracle.com/javase/8/docs/api/%s.html"
jfxurl = "https://docs.oracle.com/javase/8/javafx/api/%s.html"

def replaced(text):

    replace_text = text.replace("\\n", " ").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\xe2\x80\x94", " -- ").replace("\\xe2\\x80\\x94", " -- ").replace("&#8217;", "'").replace("&para;", "|").replace("&uarr", "↑").replace("\xe2\x80\x98", "'").replace("\\xe2\\x80\\x98", "'").replace("\xe2\x80\x99", "'").replace("\\xe2\\x80\\x99", "'").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9c", "\"").replace("\\xe2\\x80\\x9c", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x9d", "\"").replace("\\xe2\\x80\\x9d", "\"").replace("\xe2\x80\x93", "-").replace("\\xe2\\x80\\x93", "-").replace("\\xc2\\xa0", " ").replace("\xc2\xa0", " ").replace("&#8217;", "'").replace("&#8212;", "--").replace("&ndash;", "--")

    return replace_text

def getOthers(text):
    text = text.replace(".", "/")

    try:
        link = javaseurl % text
        classurl = replaced(str(urlopen(link).read()))

        intface = re.findall(r'<dl> <dt>All Implemented Interfaces:</dt> <dd>(.*?)</a></dd> </dl>', classurl)
        inherit = re.findall(r'<h3>\w+ inherited from .*?</h3>(.*?)<!--   -->', classurl)

        if text == "java/util/Scanner":
            intface = ["Closeable, AutoCloseable, Iterator&lt;String&gt;"]
    except:
        link = jfxurl % text
        classurl = replaced(str(urlopen(link).read()))

        intface = re.findall(r'<dl> <dt>All Implemented Interfaces:</dt> <dd>(.*?)</a></dd> </dl>', classurl)
        inherit = re.findall(r'<h3>\w+ inherited from .*?</h3>(.*?)<!--   -->', classurl)


    interface = "Implemented Interfaces are:\n"; interface += "%s\n" % ("=" * (len(interface) - 1))
    inherited = "\nInherited Methods are:\n"; inherited += "%s\n" % ("=" * (len(inherited) - 1))
    fields = "\nInherited Fields are:\n"; fields += "%s\n" % ("=" * (len(fields) - 1))

    pattern = re.compile(r'<.*?>')

    intface = pattern.sub("", "".join(intface)).split(", ")
    inherit = pattern.sub("", "".join(inherit))

    pattern = re.compile(r'\s{2,20}')
    inherit = pattern.sub(" ", "".join(inherit.replace(",", ""))).split(" ")

    for x in sorted(set(inherit)):
        if len(x) > 0:
            if x.isupper():
                fields += "%s, " % x
            else:
                inherited += "%s(), " % x

    for x in sorted(set(intface)):
        interface += x + ", "

    interface += "\n" + fields
    return (interface + "\n" + inherited, link)

print(getOthers("java.util.Scanner"))