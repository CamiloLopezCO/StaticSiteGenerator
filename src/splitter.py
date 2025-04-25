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

