import bibtexparser
import xml.etree.ElementTree as ET
from xml.dom import minidom


def parse_bibtex_file(file_path):
    # Load the BibTeX file
    with open(file_path, 'r') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    # Create the root element for the XML file
    above_root = ET.Element("library")
    root = ET.SubElement(above_root, "doclist")

    # Convert each BibTeX entry to an XML element
    for entry in bib_database.entries:
        entry_element = ET.SubElement(root, "doc")

        field_element = ET.SubElement(entry_element, "key")
        field_element.text = entry.get('ID', 'N/A')

        field_element = ET.SubElement(entry_element, "bib_type")
        field_element.text = entry.get('ENTRYTYPE', 'N/A')

        field_element = ET.SubElement(entry_element, "bib_title")
        field_element.text = entry.get('title', 'N/A')

        field_element = ET.SubElement(entry_element, "bib_authors")
        field_element.text = entry.get('author', 'N/A')

        field_element = ET.SubElement(entry_element, "bib_year")
        field_element.text = entry.get('year', 'N/A')

        field_element = ET.SubElement(entry_element, "bib_extra", {
            "key": "Abstract"
        })
        field_element.text = entry.get('abstract', 'N/A')

        field_element = ET.SubElement(entry_element, "bib_extra", {
            "key": "Url"
        })
        field_element.text = entry.get('url', 'N/A')

        for field, value in entry.items():
            if field not in ['ENTRYTYPE', 'ID']:
                field_element = ET.SubElement(entry_element, field)
                field_element.text = value

    # Convert the ElementTree to a string
    xml_str = ET.tostring(above_root, encoding='utf-8')

    # Use minidom for pretty-printing with proper indentation
    pretty_xml = minidom.parseString(xml_str).toprettyxml(indent="    ",
                                                          encoding="utf-8")

    # Save the pretty-printed XML to a file
    output_file = 'scidox.reflib'
    with open(output_file, 'wb') as xml_file:
        xml_file.write(pretty_xml)

    # # Convert the ElementTree to a string and save it as an XML file
    # tree = ET.ElementTree(root)
    # output_file = 'bibtex_entries.xml'
    # tree.write(output_file, encoding='utf-8', xml_declaration=True)

    # # Save to a JSON file
    # output_file = 'bibtex_entries.json'
    # with open(output_file, 'w') as json_file:
    #     json.dump(entries_list, json_file, indent=4)


parse_bibtex_file('biblio.bib')