# perrin-isir.github.io

1) Define a list of arXiv ids in arxiv_id_list.txt

2) Run 'python deduplicate_id_list.py > tmp.txt'.

3) Run 'arxiv2bib < tmp.txt > biblio.bib' to generate the bib file. 

4) With Referencer, create a new library, import biblio.bib, and save the library as scidox.reflib.

5) Run 'python create_html.py' to generate index.html

6) Replace arxiv_id_list.txt by tmp.txt
