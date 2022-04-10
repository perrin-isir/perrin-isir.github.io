import arxiv
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
    
tree = ET.parse('sci_docs.reflib')
root = tree.getroot()
container = root.findall("./doclist/doc")
for doc in container:
    for x in doc.findall("./bib_title"):
        if x.text is not None:
          # print("[true title: ]", x.text)
          search = arxiv.Search(
            query = "ti:" + x.text,
            max_results = 1,
            sort_by = arxiv.SortCriterion.Relevance
          )
          for res in search.results():
            # print("[arXiv match]: ", res.title)
            # print(similar(x.text, res.title))
            if similar(x.text, res.title) >= 0.9:
              print(res.entry_id.replace('http://arxiv.org/abs/', ''))

