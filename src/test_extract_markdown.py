import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
    def test_extract_markdown_links_no_images(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and no images"
        )
        self.assertListEqual([("link", "https://example.com")], matches)
    def test_extract_markdown_images_no_links(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and no links"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    def test_extract_markdown_links_with_exclamation(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://example.com) and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link with exclamation!](https://example.com)"
        )
        self.assertListEqual([("link", "https://example.com"), ("link with exclamation!", "https://example.com")], matches)
    def test_extract_markdown_images_with_exclamation(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and an ![image with exclamation!](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image with exclamation!", "https://i.imgur.com/zjjcJKZ.png")], matches)
    