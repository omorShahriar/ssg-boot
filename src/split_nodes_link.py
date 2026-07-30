
from textnode import TextType,TextNode
def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.LINK:
            new_nodes.append(node)
        elif node.text_type == TextType.TEXT:
            parts = node.text.split('[')
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    link_parts = part.split(']')
                    if len(link_parts) > 1:
                        link_text = link_parts[0]
                        link_url = link_parts[1].strip('()')
                        new_nodes.append(TextNode(link_text, TextType.LINK))
                        new_nodes.append(TextNode(link_url, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)

    return new_nodes