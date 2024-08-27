import xml.etree.ElementTree as ET
import re

tree = ET.parse('./scidox.reflib')
root = tree.getroot()
wfile = open('./arxiv_list.html', 'w+')
container = root.findall("./doclist/doc")
# tags = root.findall("./taglist/tag")
# listtags={}
# for t in tags:
#     a = t.findall("./uid")[0].text.encode('ascii', 'xmlcharrefreplace')
#     b = t.findall("./name")[0].text.encode('ascii', 'xmlcharrefreplace')
#     listtags[a.decode('UTF-8')] = b.decode('UTF-8')

listtags = ['contrastive', 'control', 'deep', 'distill', 'diversity', 'entropy', 'evolution', 'exoskeleton', 'explainable', 'exploration', 'few-shot', 'goal-conditioned', 'gradient', 'hierarchical', 'humanoid', 'imitation', 'intrinsic', 'kinematic', 'lifelong learning', 'meta', 'model-based', 'motion planning', 'multi-task', 'off-policy', 'offline', 'on-policy', 'open-ended', 'optimal', 'population', 'reinforcement', 'replay', 'robot', 'self-supervised', 'skill', 'sparse', 'transfer', 'unsupervised']
data = []
# names = []
for doc in container:
    key = str(9999 - int(doc.findtext("./bib_year"))) + '/' + doc.findtext("./bib_authors") + '/' + doc.findtext("./bib_title")
    data.append((key, doc))
data.sort()  # error if there are duplicate keys

firstpart = open('./index_files/first_part.html', 'r')
for line in firstpart:
    print(line, file=wfile)

print("<script type=\"text/javascript\">", file=wfile)
print(
    "function toggleVisibility(x) { var e = document.getElementById(x); if(e.style.display == 'block') e.style.display = 'none'; else e.style.display = 'block';}",
    file=wfile)
print("</script>", file=wfile)
print("<script type=\"text/javascript\">", file=wfile)
print("function change(x){ elt = document.getElementById(\"qs_field\"); elt.value = x; elt.dispatchEvent(new Event('change')); elt.dispatchEvent(new Event('change')); }", file=wfile)
print("</script>", file=wfile)
print(
    "<div style=\"font-size:1rem\"><a href=\"./index.html\">HOME</a> - Click on [|&bull;|] to show the abstract and on the abstract to hide it - Click on the title to open on arXiv - Click on the authors to open on ar5iv</div>",
    file=wfile)

print("<div id=\"links\" style=\"display:none;\">", file=wfile)
print("<table style=\"font-size:1rem\"><td width=\"100\%\"><i>", file=wfile)
sortedtags = listtags.copy()
sortedtags.sort()

for x in sortedtags:
    print("<a onclick=\"change('" + x + "');\">" + x + " /</a>",
          file=wfile)
print("</i></td></table>", file=wfile)
print("</div>", file=wfile)

middlepart = open('./index_files/middle_part.html', 'r')
for line in middlepart:
    print(line, file=wfile)
    
print("</table><table style=\"font-size:1rem\" bgcolor=\"#F5F6CE\" WIDTH=\"300\" id=\"qs_table\" border=\"0\" cellspacing=\"0\" cellpadding=\"0\">", file=wfile)

i = 0
for d in data:
    doc = d[1]
    title = ""
    authors = ""
    url = ""
    url_ar5iv = ""
    year = ""
    dockey = ""
    tag = []
    for x in doc.findall("./bib_title"):
        if x.text is not None:
            title = x.text.encode('ascii', 'xmlcharrefreplace')
    for x in doc.findall("./bib_authors"):
        if x.text is not None:
            authors = x.text.encode('ascii', 'xmlcharrefreplace')
    for x in doc.findall("./bib_extra"):
        if x.attrib['key'] == 'Url' or x.attrib['key'] == 'url':
            if x.text is not None:
                url = x.text.encode('ascii', 'xmlcharrefreplace')
                url_ar5iv = url.replace(b'arxiv', b'ar5iv')
        if x.attrib['key'] == 'Abstract' or x.attrib['key'] == 'abstract':
            if x.text is not None:
                abstract = x.text
                for tg in sortedtags:
                    if re.search(tg, abstract, re.IGNORECASE) or re.search(
                            tg.replace('-', ' '), abstract, re.IGNORECASE):
                        tag.append(tg.encode('ascii', 'xmlcharrefreplace'))
                abstract = abstract.encode('ascii', 'xmlcharrefreplace')
                url = x.text.encode('ascii', 'xmlcharrefreplace')
                url_ar5iv = url.replace(b'arxiv', b'ar5iv')
    for x in doc.findall("./bib_year"):
        if x.text is not None:
            year = x.text.encode('ascii', 'xmlcharrefreplace')
    for x in doc.findall("./key"):
        if x.text is not None:
            dockey = x.text.encode('ascii', 'xmlcharrefreplace')
    # for x in doc.findall("./tagged"):
    #     if x.text is not None:
    #       tag.append(x.text.encode('ascii', 'xmlcharrefreplace'))
    i += 1
    print("<tr id=\"", str(i), "\" class=\"entry\"><td>", file=wfile)
    print("<a onclick=\"toggleVisibility('abstract"
         + str(i)
         + "');\">[|&bull;|]</a><a href=\"" + url.decode(
             'UTF-8') + "\">", file=wfile)
    # __import__("IPython").embed()
    if type(year) == bytes:
        year = year.decode('UTF-8')
    print("<b/>",
         title.decode('UTF-8').replace('{', '').replace('}', ''),
         "(" + year + ")</b>", file=wfile)
    print("</a>", file=wfile)
    print("&nbsp; - &nbsp;", file=wfile)
    print("<I><a href=\"" + url_ar5iv.decode('UTF-8') + "\">",
         file=wfile)
    print(authors.decode('UTF-8').replace(" and ", ", "), "&nbsp;", file=wfile)
    print("</a></I><span style=\"float:right\"><a onclick=\"toggleVisibility('abstract"
         + str(i)
         + "');\">[|&bull;|]</a></span>", file=wfile)
    print("<a onclick=\"toggleVisibility('abstract"
         + str(i)
         + "');\"><div id=\"abstract"
         + str(i)
         + "\" style=\"font-size: 1rem; color:black; display: none\">", file=wfile)
    print("<u><I>", dockey.decode('UTF-8'), "&nbsp; - &nbsp;", file=wfile)
    for tg in tag:
         print("{" + tg.decode('UTF-8') + "}", file=wfile)
    print("</I></u><br>", abstract.decode('UTF-8'), "<br><br></div></a>", file=wfile)
    print("</td></tr>", file=wfile)

firstpart = open('./index_files/last_part.html', 'r')
for line in firstpart:
    print(line, file=wfile)
