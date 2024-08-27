#!/bin/bash
echo >> arxiv_id_list.txt
cat arxiv_id_list.txt arxiv_ids_to_add.txt > tmp.txt
mv tmp.txt arxiv_id_list.txt
echo "" > arxiv_ids_to_add.txt
python deduplicate_id_list.py > tmp.txt
arxiv2bib < tmp.txt > biblio.bib
python parser.py
python create_html.py
mv tmp.txt arxiv_id_list.txt
line_count=$(wc -l < arxiv_id_list.txt)
echo "Done: $line_count entries."
