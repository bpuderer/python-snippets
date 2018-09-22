import unittest

from xml_utils import validate_against_xsd_from_files


XSD_FILENAME = './example.xsd'

class SchemaValidationTestCase(unittest.TestCase):

    def test_schema_valid(self):
        validate_against_xsd_from_files(XSD_FILENAME, './valid_example.xml')

    def test_schema_invalid(self):
        validate_against_xsd_from_files(XSD_FILENAME, './invalid_example.xml')


if __name__ == '__main__':
    unittest.main()
