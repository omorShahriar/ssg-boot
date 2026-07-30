from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType
import unittest
# Write a bunch of tests. Be sure to test various types of delimiters.

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        old_nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is an italic node", TextType.ITALIC),
        ]
        delimiter = " "
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected_nodes = [
            TextNode("This", TextType.TEXT),
            TextNode("is", TextType.BOLD),
            TextNode("a", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode("node", TextType.TEXT),
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is an italic node", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    def test_split_nodes_delimiter_comma(self):
        old_nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is an italic node", TextType.ITALIC),
        ]
        delimiter = ","
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected_nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is an italic node", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_nodes)
    def test_split_nodes_delimiter_pipe(self):
        old_nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is an italic node", TextType.ITALIC),
        ]
        delimiter = "|"
        text_type = TextType.BOLD
        new_nodes = split_nodes_delimiter(old_nodes, delimiter, text_type)
        expected_nodes = [
            TextNode("This is a text node", TextType.TEXT),
            TextNode("This is a bold node", TextType.BOLD),
            TextNode("This is an italic node", TextType.ITALIC),
        ]
        self.assertEqual(new_nodes, expected_nodes)
if __name__ == "__main__":
    unittest.main()