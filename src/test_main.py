import os
import tempfile
import unittest

from main import extract_title, generate_page


class TestExtractTitle(unittest.TestCase):
    def test_extracts_h1_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_strips_title_whitespace(self):
        self.assertEqual(extract_title("#   Hello world  "), "Hello world")

    def test_ignores_non_h1_headings(self):
        with self.assertRaises(Exception):
            extract_title("## Not an h1")

    def test_raises_when_title_is_missing(self):
        with self.assertRaises(Exception):
            extract_title("A paragraph without a heading")

    def test_generate_page_replaces_template_placeholders(self):
        with tempfile.TemporaryDirectory() as directory:
            markdown_path = os.path.join(directory, "index.md")
            template_path = os.path.join(directory, "template.html")
            destination_path = os.path.join(directory, "nested", "index.html")

            with open(markdown_path, "w") as markdown_file:
                markdown_file.write("# Hello\n\nThis is **bold**.")
            with open(template_path, "w") as template_file:
                template_file.write("<title>{{ Title }}</title>{{ Content }}")

            generate_page(markdown_path, template_path, destination_path)

            with open(destination_path) as output_file:
                self.assertEqual(
                    output_file.read(),
                    "<title>Hello</title><div><h1>Hello</h1><p>This is <b>bold</b>.</p></div>",
                )
