import unittest

from xml_utils import validate_against_xsd, validate_against_xsd_str


XSD_FILENAME = './example.xsd'

class XMLSchemaValidationTestCase(unittest.TestCase):

    def test_schema_valid(self):
        validate_against_xsd(XSD_FILENAME, './valid_example.xml')

    def test_schema_invalid(self):
        with open(XSD_FILENAME) as f:
            xsd_str = f.read()
        with open('./invalid_example.xml') as f:
            xml_str = f.read()
        validate_against_xsd_str(xsd_str, xml_str)


if __name__ == '__main__':
    unittest.main()
