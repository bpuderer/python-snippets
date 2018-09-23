from io import StringIO

from lxml import etree


# http://lxml.de/validation.html
def validate_against_xsd(xsd_file, xml_file):
    """validate xml doc against xsd"""

    xmlschema_doc = etree.parse(xsd_file)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    doc = etree.parse(xml_file)
    # xmlschema.assertValid(doc)    # raises lxml.etree.DocumentInvalid
    # xmlschema.validate(doc)       # returns True/False
    xmlschema.assert_(doc)          # raises AssertionError


def validate_against_xsd_str(xsd_str, xml_str):
    """validate xml doc against xsd from strings"""

    validate_against_xsd(StringIO(xsd_str), StringIO(xml_str))
