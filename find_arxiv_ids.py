import re
pattern = re.compile("(arXiv:|arxiv.org/abs/|ARXIV.)(\d{4,5}).(\d{4,5})")

count = 0
all_ids = set()
for i, line in enumerate(open('biblio.bib')):
    for match in re.finditer(pattern, line):
        count += 1
        # print('(%s) Found on line %s: %s' % (count, i+1, match.group()))
        # from IPython import embed
        # embed()
        all_ids.add(match.groups()[1] + "." + match.groups()[2])
id_list = list(all_ids)
for id in id_list:
    print(id)
