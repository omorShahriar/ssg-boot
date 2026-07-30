import re

from textnode import TextType,TextNode


IMAGE_PATTERN = re.compile(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)")


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.IMAGE:
            new_nodes.append(node)
        elif node.text_type == TextType.TEXT:
            cursor = 0
            for match in IMAGE_PATTERN.finditer(node.text):
                if match.start() > cursor:
                    new_nodes.append(TextNode(node.text[cursor:match.start()], TextType.TEXT))
                new_nodes.append(TextNode(match.group(1), TextType.IMAGE, match.group(2)))
                cursor = match.end()
            if cursor < len(node.text):
                new_nodes.append(TextNode(node.text[cursor:], TextType.TEXT))
            elif cursor == 0:
                new_nodes.append(node)
        else:
            new_nodes.append(node)

    return new_nodes
