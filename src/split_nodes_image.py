from textnode import TextType,TextNode

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.IMAGE:
            new_nodes.append(node)
        elif node.text_type == TextType.TEXT:
            parts = node.text.split('![')
            for i, part in enumerate(parts):
                if i % 2 == 0:
                    new_nodes.append(TextNode(part, TextType.TEXT))
                else:
                    image_parts = part.split(']')
                    if len(image_parts) > 1:
                        image_text = image_parts[0]
                        image_url = image_parts[1].strip('()')
                        new_nodes.append(TextNode(image_text, TextType.IMAGE))
                        new_nodes.append(TextNode(image_url, TextType.TEXT))
                    else:
                        new_nodes.append(TextNode(part, TextType.TEXT))
        else:
            new_nodes.append(node)

    return new_nodes