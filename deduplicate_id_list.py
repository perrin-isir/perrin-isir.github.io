count = 0
all_ids = set()

def is_only_spaces_or_newlines(s):
    return all(char in {' ', '\n'} for char in s)

for i, line in enumerate(open('arxiv_id_list.txt')):
    if not is_only_spaces_or_newlines(line):
        count += 1
        all_ids.add(line.replace('\n', ''))
id_list = list(all_ids)
for id in id_list:
    print(id)
