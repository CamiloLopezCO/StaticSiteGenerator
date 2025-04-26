import unittest
from parser import block_to_block_type
from blocktype import BlockType

class TestBlockToBlockType(unittest.TestCase):
    def test_heading_block(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("## Another Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("###### Level 6 Heading"), BlockType.HEADING)

    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)

    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> quote\n> another line"), BlockType.QUOTE)

    def test_unordered_list_block(self):
        self.assertEqual(block_to_block_type("- item 1\n- item 2"), BlockType.UNORDERED_LIST)

    def test_ordered_list_block(self):
        self.assertEqual(block_to_block_type("1. item one\n2. item two\n3. item three"), BlockType.ORDERED_LIST)

    def test_paragraph_block(self):
        self.assertEqual(block_to_block_type("This is just a normal paragraph."), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()

