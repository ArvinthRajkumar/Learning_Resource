import xml.etree.ElementTree as ET
xml = """<catalog>
  <book id="b1"><title>Learning Python</title><price currency="USD">29.5</price></book>
  <book id="b2"><title>SQL Basics</title><price currency="EUR">19</price></book>
</catalog>"""
root = ET.fromstring(xml)
for b in root.findall("book"):
    print(b.get("id"), "|", b.findtext("title"), "|", b.find("price").get("currency"), float(b.findtext("price")))
new = ET.SubElement(root, "book", id="b3")
ET.SubElement(new, "title").text = "Algorithms"
print(ET.tostring(root, encoding="unicode").count("<book"), "books after adding one")
print(root.findall(".//price[@currency='EUR']")[0].text, "(XPath-like query)")
