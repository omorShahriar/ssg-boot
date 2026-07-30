from block_to_block_type import BlockType, block_to_block_type
from htmlnode import ParentNode
from main import text_node_to_html_node
from markdown_to_blocks import markdown_to_blocks
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


def text_to_children(text: str):
    return [text_node_to_html_node(node) for node in text_to_textnodes(text)]


def block_to_html_node(block: str):
    block_type = block_to_block_type(block)

    if block_type == BlockType.HEADING:
        level = block.index(" ")
        return ParentNode(f"h{level}", text_to_children(block[level + 1:]))

    if block_type == BlockType.CODE:
        code = block[4:-3]
        code_node = text_node_to_html_node(TextNode(code, TextType.CODE))
        return ParentNode("pre", [code_node])

    if block_type == BlockType.QUOTE:
        quote = "\n".join(line[1:].lstrip() for line in block.splitlines())
        return ParentNode("blockquote", text_to_children(quote))

    if block_type == BlockType.UNORDERED_LIST:
        items = [
            ParentNode("li", text_to_children(line[2:]))
            for line in block.splitlines()
        ]
        return ParentNode("ul", items)

    if block_type == BlockType.ORDERED_LIST:
        items = [
            ParentNode("li", text_to_children(line.split(". ", 1)[1]))
            for line in block.splitlines()
        ]
        return ParentNode("ol", items)

    paragraph = " ".join(block.splitlines())
    return ParentNode("p", text_to_children(paragraph))


def markdown_to_html_node(markdown: str):
    return ParentNode("div", [block_to_html_node(block) for block in markdown_to_blocks(markdown)])
