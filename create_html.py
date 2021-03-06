import xml.etree.ElementTree as ET
import re

tree = ET.parse('./scidox.reflib')
root = tree.getroot()
wfile = open('./index.html', 'w+')
container = root.findall("./doclist/doc")
# tags = root.findall("./taglist/tag")
# listtags={}
# for t in tags:
#     a = t.findall("./uid")[0].text.encode('ascii', 'xmlcharrefreplace')
#     b = t.findall("./name")[0].text.encode('ascii', 'xmlcharrefreplace')
#     listtags[a.decode('UTF-8')] = b.decode('UTF-8')

listtags = ['lifelong', 'primal', 'evolution', 'dual', 'self-supervised', 'contrastive',
            'compos', 'explor', 'robot', 'reinforce', 'model', 'kinematic', 'humanoid',
            'control', 'deep', 'meta', 'optim', 'theory', 'hierarchical',
            'motion planning', 'gradient', 'skill', 'multi-task', 'explainab',
            'goal-conditioned', 'entropy', 'diversity', 'intrinsic', 'unsupervised',
            'distill', 'hybrid', 'network', 'imitation', 'open-ended', 'simul',
            'population', 'sparse', 'replay', 'on-policy', 'off-policy', 'few-shot',
            'transfer']
data = []
# names = []
for doc in container:
    key = doc.findtext("./bib_authors") + '/' + doc.findtext("./bib_title")
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
print(
    "<div id=\"content\" style=\"font-size:2.0vh\">[Links to arXiv/ar5iv articles] <a href=\"#\" onclick=\"toggleVisibility('links')\">[TAGS on/off]</a></div>",
    file=wfile)
print("<div id=\"links\" style=\"display:block\">", file=wfile)
print("<table style=\"font-size:2.0vh\"><td width=\"100\%\"><i>", file=wfile)
# sortedtags = []
# for x in listtags:
#     sortedtags.append(listtags[x])
sortedtags = listtags.copy()
sortedtags.sort()
for x in sortedtags:
    print("<a href=\"index.html?search=&quot;[^]*{" + x + "}&quot;\">" + x + " /</a>",
          file=wfile)
print("</i></td></table>", file=wfile)
print("</div>", file=wfile)

middlepart = open('./index_files/middle_part.html', 'r')
for line in middlepart:
    print(line, file=wfile)

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
    print("<tr id=\"", str(i), "\" class=\"entry\"><td>",
          "<div style=\"height:100%;width:100%\"><small><a href=\"" + url.decode(
              'UTF-8') + "\"><font color=\"black\">", file=wfile)
    print("\n&nbsp; &bull;<b/>",
          title.decode('UTF-8').replace('{', '').replace('}', ''),
          "(" + year.decode('UTF-8') + ")</b>", file=wfile)
    print("</font></a>", file=wfile)
    print("&nbsp; - &nbsp;", file=wfile)
    print("<a href=\"" + url_ar5iv.decode('UTF-8') + "\"><font color=\"black\">",
          file=wfile)
    print(authors.decode('UTF-8'), "&nbsp; - &nbsp;",
          dockey.decode('UTF-8'), "&nbsp; - &nbsp;<I>", file=wfile)
    for tg in tag:
        print("{" + tg.decode('UTF-8') + "}", file=wfile)

    print("</I></font></a>&nbsp; - &nbsp;<a href=\"#\" onclick=\"toggleVisibility('abstract"
          + str(i)
          + "'); return false;\">[abstract]</a></small></div><div id=\"abstract"
          + str(i)
          + "\" style=\"display: none\"><small>", abstract.decode('UTF-8'), "</small></div>", file=wfile)
    print("</td></tr>", file=wfile)

firstpart = open('./index_files/last_part.html', 'r')
for line in firstpart:
    print(line, file=wfile)
