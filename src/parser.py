from textnode import TextNode, TextType
from blocktype import BlockType

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

def block_to_block_type(block):
    # Code block: starts and ends with ```
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    # Heading: starts with 1-6 # followed by a space
    if block.startswith("#"):
        count = 0
        for char in block:
            if char == "#":
                count += 1
            else:
                break
        if 1 <= count <= 6 and block[count] == " ":
            return BlockType.HEADING

    lines = block.split("\n")

    # Quote block: every line starts with >
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    # Unordered list block: every line starts with "- "
    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Ordered list block: every line starts with an incrementing number and ". "
    is_ordered = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i+1}. "
        if not line.strip().startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    # Otherwise: Paragraph
    return BlockType.PARAGRAPH

