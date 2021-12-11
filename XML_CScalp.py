import xmltodict

XML_FILE_NAME = 'XML/BINAD.CCUR_FUT.GALAUSDT_Settings_4KHhv_original.xml'

with open(XML_FILE_NAME, 'r', encoding='utf-8') as f:
    xml = xmltodict.parse(f.read(), encoding='utf-8')

print(xml)
xml['Settings']['DOM']['AutoScroll']['@Value'] = str(False)
print(xml)

with open(XML_FILE_NAME, 'w', encoding='utf-8') as f:
    f.write(xmltodict.unparse(xml, pretty=True, short_empty_elements=True, full_document=True, encoding='utf-8'))


def change_tabs_to_spaces(xml_lines):
    for i in range(len(xml_lines)):
        old_len = len(xml_lines[i])
        xml_lines[i] = xml_lines[i].lstrip()
        new_len = len(xml_lines[i])
        diff = old_len - new_len
        xml_lines[i] = ' ' * diff * 2 + xml_lines[i]


def add_space_in_front_of_backslash(xml_lines):
    for i in range(len(xml_lines)):
        xml_lines[i] = xml_lines[i].replace('/>', ' />')


f = open(XML_FILE_NAME, 'r', encoding='utf-8')
xml_lines = f.readlines()
f.close()

change_tabs_to_spaces(xml_lines)
add_space_in_front_of_backslash(xml_lines)

with open(XML_FILE_NAME, 'w', encoding='utf-8') as f:
    f.writelines(xml_lines)