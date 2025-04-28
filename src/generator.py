import os
from generator import generate_page

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # Loop through all files and directories inside the content folder
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content, entry)

        if os.path.isfile(entry_path) and entry_path.endswith(".md"):
            # If it's a markdown file, create the corresponding HTML file
            relative_path = os.path.relpath(entry_path, dir_path_content)
            dest_path = os.path.join(dest_dir_path, relative_path)
            dest_path = dest_path.replace(".md", ".html")

            os.makedirs(os.path.dirname(dest_path), exist_ok=True)

            print(f"Generating page: {entry_path} -> {dest_path}")
            generate_page(entry_path, template_path, dest_path)

        elif os.path.isdir(entry_path):
            # If it's a directory, recurse into it
            generate_pages_recursive(entry_path, template_path, dest_dir_path)

