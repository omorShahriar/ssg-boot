import unittest

from block_to_block_type import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("## Heading"), BlockType.HEADING)

    def test_heading_requires_one_to_six_hashes_and_a_space(self):
        for hashes in ("#", "##", "###", "####", "#####", "######"):
            with self.subTest(hashes=hashes):
                self.assertEqual(block_to_block_type(f"{hashes} heading"), BlockType.HEADING)

        self.assertEqual(block_to_block_type("####### heading"), BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type("#heading"), BlockType.PARAGRAPH)

    def test_multiline_code_block(self):
        block = "```\nprint('hello')\nprint('world')\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_requires_a_newline_after_opening_fence(self):
        self.assertEqual(block_to_block_type("```code``"), BlockType.PARAGRAPH)

    def test_multiline_quote_block(self):
        self.assertEqual(
            block_to_block_type(">first quote\n> second quote"),
            BlockType.QUOTE,
        )

    def test_quote_requires_every_line_to_start_with_greater_than(self):
        self.assertEqual(
            block_to_block_type(">first quote\nplain text"),
            BlockType.PARAGRAPH,
        )

    def test_unordered_list_block(self):
        self.assertEqual(
            block_to_block_type("- first\n- second\n- third"),
            BlockType.UNORDERED_LIST,
        )

    def test_unordered_list_requires_dash_and_space_on_every_line(self):
        self.assertEqual(
            block_to_block_type("- first\n* second"),
            BlockType.PARAGRAPH,
        )

    def test_ordered_list_block(self):
        self.assertEqual(
            block_to_block_type("1. first\n2. second\n3. third"),
            BlockType.ORDERED_LIST,
        )

    def test_ordered_list_must_start_at_one_and_increment(self):
        for block in ("2. first\n3. second", "1. first\n3. third", "1. first\n2. second\n4. fourth"):
            with self.subTest(block=block):
                self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_normal_paragraph(self):
        self.assertEqual(
            block_to_block_type("This is an ordinary paragraph."),
            BlockType.PARAGRAPH,
        )
