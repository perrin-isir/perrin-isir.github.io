#!/bin/bash
cat arxiv_id_list.txt arxiv_ids_to_add.txt > tmp.txt
mv tmp.txt arxiv_id_list.txt
echo "" > arxiv_ids_to_add.txt
python deduplicate_id_list.py > tmp.txt
arxiv2bib < tmp.txt > biblio.bib
echo "In Referencer, create new library, import biblio.bib and save as scidox.reflib"
referencer
python create_html.py
mv tmp.txt arxiv_id_list.txt
echo "Done."
