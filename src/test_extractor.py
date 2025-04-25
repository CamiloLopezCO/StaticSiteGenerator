import unittest
from extractor import extract_markdown_images, extract_markdown_links

class TestExtractor(unittest.TestCase):
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            matches, [("image", "https://i.imgur.com/zjjcJKZ.png")]
        )

    def test_extract_multiple_markdown_images(self):
        text = "Look at ![dog](https://dog.png) and ![cat](https://cat.png)"
        matches = extract_markdown_images(text)
        self.assertListEqual(
            matches, [
                ("dog", "https://dog.png"),
                ("cat", "https://cat.png"),
            ]
        )

    def test_extract_markdown_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            matches, [("to boot dev", "https://www.boot.dev")]
        )

    def test_extract_multiple_markdown_links(self):
        text = "[Google](https://google.com) and [YouTube](https://youtube.com)"
        matches = extract_markdown_links(text)
        self.assertListEqual(
            matches, [
                ("Google", "https://google.com"),
                ("YouTube", "https://youtube.com"),
            ]
        )

    def test_no_false_image_matches_in_links(self):
        text = "Regular [link](https://somewhere.com) no image here!"
        matches = extract_markdown_images(text)
        self.assertListEqual(matches, [])

    def test_no_false_link_matches_in_images(self):
        text = "An ![actual image](https://img.png) not a link"
        matches = extract_markdown_links(text)
        self.assertListEqual(matches, [])

if __name__ == "__main__":
    unittest.main()

