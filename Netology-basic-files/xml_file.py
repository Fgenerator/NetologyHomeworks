import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse('newsafr.xml', parser)

root = tree.getroot()

print(root.attrib)