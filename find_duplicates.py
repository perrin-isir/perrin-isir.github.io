import xml.etree.ElementTree as ET
import os
import collections

import xml.etree.ElementTree as ET
tree = ET.parse('./scidox.reflib')
root = tree.getroot()
wfile = open('./scidox.html', 'w+')
container = root.findall("./doclist/doc")

titles_list = []
for doc in container:
    ttl = doc.findtext("bib_title")
    titles_list.append(ttl)

duplicates = [item for item, count in collections.Counter(titles_list).items() if count > 1]
for elt in duplicates:
    print(elt)
  
