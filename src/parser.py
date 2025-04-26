from textnode import TextNode, TextType
from splitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    # Important: Handle in correct order
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def markdown_to_blocks(markdown):
    # Step 1: Split the raw markdown into rough blocks
    raw_blocks = markdown.split("\n\n")

    # Step 2: Clean up each block and remove empty ones
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]

    return blocks

