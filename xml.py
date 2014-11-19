from xml.dom import minidom

content = minidom.parse('new.xml')
#print content.toxml()

book_list=content.getElementsByTagName('book')
#print book_list[0].toxml()
print book_list[0].childNodes[1].toxml()

print book_list[0].childNodes[1].childNodes[0].data

#print book_list[0].attributes.keys()

print book_list[0].attributes["url"].value
