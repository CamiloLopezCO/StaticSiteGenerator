import os
import shutil
import sys
from extractor import extract_title
from parser import markdown_to_html_node
from generator import generate_pages_recursive  # <-- NEW import

def clear_and_copy_static(src_dir, dest_dir):
    if os.path.exists(dest_dir):
        print(f"Deleting existing directory: {dest_dir}")
        shutil.rmtree(dest_dir)

    os.makedirs(dest_dir)
    print(f"Created directory: {dest_dir}")

    for item in os.listdir(src_dir):
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
            print(f"Copied file: {src_path} -> {dest_path}")
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
            print(f"Copied directory: {src_path} -> {dest_path}")

def main():
    #Get base path from CLI argument (or default to '/')
    base_path = sys.argv[1] if len(sys.argv) > 1 else "/"

    clear_and_copy_static("static", "docs")  # 🚨 Now generate into 'docs' no

    # 🚨 Now generate ALL pages recursively (index.md + all blog posts)
    generate_pages_recursive("content", "template.html", "docs", base_path)

if __name__ == "__main__":
    main()

