from textnode import TextNode, TextType
from blocktype import BlockType
from leafnode import LeafNode
from parentnode import ParentNode
from splitter import (
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)
from extractor import extract_markdown_images, extract_markdown_links
from conversions import text_node_to_html_node

# --- Inline Text Splitting ---

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes

def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []

    for node in nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)

    return html_nodes

# --- Block Splitting and Typing ---

def markdown_to_blocks(markdown):
    raw_blocks = markdown.split("\n\n")
    blocks = [block.strip() for block in raw_blocks if block.strip() != ""]
    return blocks

def block_to_block_type(block):
    block = block.strip()

    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

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

    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(line.strip().startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    is_ordered = True
    for i, line in enumerate(lines):
        expected_prefix = f"{i+1}. "
        if not line.strip().startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

# --- Markdown to Full HTML Node ---

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block = block.strip()
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block = block.replace("\n", " ")
            paragraph_node = ParentNode("p", text_to_children(block))
            children.append(paragraph_node)

        elif block_type == BlockType.HEADING:
            heading_lines = block.split("\n")
            for line in heading_lines:
                heading_level = line.count("#", 0, line.find(" "))
                heading_text = line[heading_level+1:].strip()
                heading_node = ParentNode(f"h{heading_level}", text_to_children(heading_text))
                children.append(heading_node)

        elif block_type == BlockType.CODE:
            code_lines = block.split("\n")
            code_content = "\n".join(code_lines[1:-1]) + "\n"  # ✅ Add missing \n at end
            code_leaf = LeafNode("code", code_content)
            pre_node = ParentNode("pre", [code_leaf])
            children.append(pre_node)

        elif block_type == BlockType.QUOTE:
            quote_lines = [line.lstrip("> ").strip() for line in block.split("\n")]
            quote_text = "\n".join(quote_lines)
            quote_node = ParentNode("blockquote", text_to_children(quote_text))
            children.append(quote_node)

        elif block_type == BlockType.UNORDERED_LIST:
            list_items = []
            for line in block.split("\n"):
                item_text = line.lstrip("- ").strip()
                item_node = ParentNode("li", text_to_children(item_text))
                list_items.append(item_node)
            ul_node = ParentNode("ul", list_items)
            children.append(ul_node)

        elif block_type == BlockType.ORDERED_LIST:
            list_items = []
            for line in block.split("\n"):
                parts = line.split(". ", 1)
                if len(parts) == 2:
                    item_text = parts[1]
                    item_node = ParentNode("li", text_to_children(item_text))
                    list_items.append(item_node)
            ol_node = ParentNode("ol", list_items)
            children.append(ol_node)

    return ParentNode("div", children)
