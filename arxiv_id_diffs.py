from IPython import embed
import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

all_ids1 = set()
for i, line in enumerate(open(file1)):
    all_ids1.add(line)

all_ids2 = set()
for i, line in enumerate(open(file2)):
    all_ids2.add(line)
    
embed()
