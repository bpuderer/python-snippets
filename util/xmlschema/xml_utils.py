from io import StringIO

from lxml import etree


# http://lxml.de/validation.html
def validate_against_xsd(xsd_str, xml_str):
    """validate xml doc against xsd"""

    xmlschema_doc = etree.parse(StringIO(xsd_str))
    xmlschema = etree.XMLSchema(xmlschema_doc)

    doc = etree.parse(StringIO(xml_str))
    # xmlschema.assertValid(doc)    # raises lxml.etree.DocumentInvalid
    # xmlschema.validate(doc)       # returns True/False
    xmlschema.assert_(doc)          # raises AssertionError


def validate_against_xsd_from_files(xsd_filename, xml_filename):
    """helper to validate using files"""

    with open(xsd_filename) as f:
        xsd_str = f.read()

    with open(xml_filename) as f:
        xml_str = f.read()

    validate_against_xsd(xsd_str, xml_str)
