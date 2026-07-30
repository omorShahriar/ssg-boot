import os
import shutil

from htmlnode import LeafNode
from textnode import TextNode, TextType


def copy_files(source, destination):
    for name in os.listdir(source):
        source_path = os.path.join(source, name)
        destination_path = os.path.join(destination, name)

        if os.path.isfile(source_path):
            shutil.copy(source_path, destination_path)
            print(f"Copied {source_path} to {destination_path}")
        else:
            os.mkdir(destination_path)
            copy_files(source_path, destination_path)


def copy_static_to_public():
    source = "static"
    destination = "public"

    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.mkdir(destination)
    copy_files(source, destination)


def extract_title(markdown):
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("No h1 header found")


def generate_page(from_path, template_path, dest_path):
    from markdown_to_html_node import markdown_to_html_node

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path) as markdown_file:
        markdown = markdown_file.read()
    with open(template_path) as template_file:
        template = template_file.read()

    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", content)

    destination_directory = os.path.dirname(dest_path)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)
    with open(dest_path, "w") as output_file:
        output_file.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for name in os.listdir(dir_path_content):
        content_path = os.path.join(dir_path_content, name)
        destination_path = os.path.join(dest_dir_path, name)

        if os.path.isfile(content_path):
            if name.endswith(".md"):
                destination_path = os.path.splitext(destination_path)[0] + ".html"
                generate_page(content_path, template_path, destination_path)
        else:
            os.makedirs(destination_path, exist_ok=True)
            generate_pages_recursive(content_path, template_path, destination_path)

def text_node_to_html_node(text_node):
    # It should handle each type of the TextType enum. If it gets a TextNode that is none of those types, it should raise an exception. Otherwise, it should return a new LeafNode object.
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode("img", None, props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unsupported TextType: {text_node.text_type}")


def main():
    copy_static_to_public()
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
