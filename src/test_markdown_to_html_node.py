import unittest

from markdown_to_html_node import markdown_to_html_node


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_headings_quotes_and_lists(self):
        md = """
# Heading

> quoted **text**
> next line

- first
- second

1. one
2. two
"""

        self.assertEqual(
            markdown_to_html_node(md).to_html(),
            "<div><h1>Heading</h1><blockquote>quoted <b>text</b>\nnext line</blockquote><ul><li>first</li><li>second</li></ul><ol><li>one</li><li>two</li></ol></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)

        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
