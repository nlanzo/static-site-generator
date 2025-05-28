import sys
import os
import shutil
from copystatic import copy_from_static_to_public
from generate_page import generate_pages_recursive


dir_path_public = "./docs"
dir_path_static = "./static"

content_path = "./content"
template_path = "./template.html"


def main():
    basepath = sys.argv[1]
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print(f"Copying files from {dir_path_static} to {dir_path_public}")
    copy_from_static_to_public(dir_path_static, dir_path_public)
    print(f"Done")

    generate_pages_recursive(content_path, template_path, dir_path_public, basepath)

    

    
main()