count = 0
all_ids = set()
for i, line in enumerate(open('arxiv_id_list.txt')):
    count += 1
    all_ids.add(line.replace('\n', ''))
id_list = list(all_ids)
for id in id_list:
    print(id)
