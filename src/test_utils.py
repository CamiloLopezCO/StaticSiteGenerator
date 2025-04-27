import unittest
from parser import extract_title

class TestExtractTitle(unittest.TestCase):
	def test_extract_title_valid(self):
		md = "# This is the title\nSome other text"
		self.assertEqual(extract_title(md), "This is the title")

	def test_extract_title_strip_spaces(self):
		md = "#     A title with spaces      "
		self.assertEqual(extract_title(md), "A title with spaces")

	def test_extract_title_no_title(self):
		md = "## Subtitle but no H1"
		with self.assertRaises(Exception):
			extract_title(md)

if __name__ == "__main__":
	unittest.main()
