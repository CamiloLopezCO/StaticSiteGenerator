import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq_same_properties(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.TEXT)
        self.assertEqual(node1, node2)

    def test_not_eq_different_text(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Goodbye", TextType.TEXT)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_text_type(self):
        node1 = TextNode("Hello", TextType.TEXT)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_not_eq_different_url(self):
        node1 = TextNode("Link text", TextType.LINK, "https://a.com")
        node2 = TextNode("Link text", TextType.LINK, "https://b.com")
        self.assertNotEqual(node1, node2)

    def test_eq_with_none_url(self):
        node1 = TextNode("Text", TextType.IMAGE)
        node2 = TextNode("Text", TextType.IMAGE, None)
        self.assertEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()

