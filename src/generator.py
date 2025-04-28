import os
from parser import markdown_to_html_node
from extractor import extract_title

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        markdown = f.read()

    with open(template_path, "r") as f:
        template = f.read()

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    title = extract_title(markdown)

    result = template.replace("{{ Title }}", title).replace("{{ Content }}", html_content)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(result)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path) and entry_path.endswith(".md"):
            # It's a markdown file, create corresponding HTML
            relative_path = os.path.relpath(entry_path, "content")
            dest_path = os.path.join(dest_dir_path, os.path.splitext(relative_path)[0] + ".html")
            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            print(f"Generating page: {entry_path} -> {dest_path}")
            generate_page(entry_path, template_path, dest_path)

        elif os.path.isdir(entry_path):
            # It's a directory, recurse into it
            generate_pages_recursive(entry_path, template_path, dest_dir_path)

