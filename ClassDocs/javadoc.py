import re
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen

javaseurl = "https://docs.oracle.com/javase/8/docs/api/%s.html"
javaseclass_url = "https://docs.oracle.com/javase/8/docs/api/allclasses-frame.html"

jfxurl = "https://docs.oracle.com/javase/8/javafx/api/%s.html"
jfxclass_url = "https://docs.oracle.com/javase/8/javafx/api/allclasses-frame.html"

def openURL(text, url, classurl):
    text = text.replace(".", "/")
    try:
        classurl = str(urlopen(classurl).read())
    except: return

    class_data = re.findall(r'<li><a href="([\w\s\d\\\/\.\-\_]+).html" title="[\w\s\.\"\>\<=]+">%s</\w+></' % text, classurl)

    if len(class_data) == 0:
        class_data = re.findall(r'<li><a href="(%s).html" title="[\w\s\.\"\>\<=]+">[\w\s\d\_\\\/\-\.]+</\w+></' % text, classurl)
    return class_data

def multiJava(url):

    link = str(urlopen(url).read())
    link = link.replace("\\n", "").replace("\\t", "").replace("\\r", "").replace("&nbsp;", " ").replace("\'", "'").replace("&quot;", "\"").replace("\\;", "").replace("\\'", "'").replace("&lt;", "<").replace("&gt;", ">").replace("&trade;", "(TM)").replace("&#8220;", "\"").replace("&#8221;", "\"").replace("\n", "").replace("\t", "").replace("\r", "").replace("&#8217;", "'")

    description = re.findall(r'<div class="block">(.*?)<div class="summary">', link)

    pattern = re.compile(r'<.*?>')
    doc = pattern.sub("", "".join(description))

    pattern = re.compile(r'\s{3,10}')
    doc = pattern.sub(" ", doc).replace("See Also:", " See Also: ").replace("Since:JDK", " Since: JDK ")
    return doc[:700], url

def getJavaDoc(text):
    text = text.replace(".", "/")
    class_data = []

    class_data1 = openURL(text, javaseurl, javaseclass_url)
    class_data2 = openURL(text, jfxurl, jfxclass_url)

    for x in class_data1:
        class_data.append(javaseurl % x)

    for x in class_data2:
        class_data.append(jfxurl % x)

    return(class_data)