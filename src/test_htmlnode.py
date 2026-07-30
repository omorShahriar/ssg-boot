
import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        node = HTMLNode("div", props={"class": "container", "id": "main"})
        self.assertEqual(node.props_to_html(), 'class="container" id="main"')
        node2 = HTMLNode("span", props={"style": "color: red;"})
        self.assertEqual(node2.props_to_html(), 'style="color: red;"')
        node3 = HTMLNode("p")
        self.assertEqual(node3.props_to_html(), '')
    # create more test for other edge cases that could happend create at least 2 more
    def test_props_to_html_empty_values(self):
        node = HTMLNode("input", props={"type": "text", "value": ""})
        self.assertEqual(node.props_to_html(), 'type="text" value=""')

    def test_props_to_html_special_characters(self):
        node = HTMLNode("a", props={"href": "https://example.com", "title": "Example Website"})
        self.assertEqual(node.props_to_html(), 'href="https://example.com" title="Example Website"')


class TestLeafNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_span_with_props(self):
        node = LeafNode("span", "Important", props={"class": "highlight"})
        self.assertEqual(node.to_html(), '<span class="highlight">Important</span>')
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just text")
        self.assertEqual(node.to_html(), "Just text")

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_children(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>")
    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", [])
        self.assertEqual(parent_node.to_html(), "<div></div>")
    

    

if __name__ == "__main__":    unittest.main()