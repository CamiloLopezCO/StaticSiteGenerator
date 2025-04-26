from textnode import TextNode, TextType
from extractor import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)

        if not images:
            new_nodes.append(node)
            continue

        for alt_text, url in images:
            sections = text.split(f"![{alt_text}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, url))
            text = sections[1]

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)

        if not links:
            new_nodes.append(node)
            continue

        for link_text, url in links:
            sections = text.split(f"[{link_text}]({url})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, url))
            text = sections[1]

        if text:
            new_nodes.append(TextNode(text, TextType.TEXT))

    return new_nodes
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # If the node is NOT normal text, just pass it through
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # If there’s an odd number of parts, it's an error (should open and close)
        if len(parts) % 2 == 0:
            raise ValueError(f"Invalid Markdown syntax: missing closing delimiter '{delimiter}'")

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                # Even index: normal text
                new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index: special text (bold, italic, code, etc)
                new_nodes.append(TextNode(part, text_type))

    return new_nodes

