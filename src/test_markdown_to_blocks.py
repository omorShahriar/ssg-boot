import unittest

from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_strips_whitespace_and_ignores_empty_blocks(self):
        markdown = "\n\n  first block  \n\n\n second block \n\n"

        self.assertEqual(
            markdown_to_blocks(markdown),
            ["first block", "second block"],
        )

    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        self.assertEqual(
            markdown_to_blocks(md),
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
