import os
import shutil

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
    clear_and_copy_static("static", "public")

if __name__ == "__main__":
    main()
