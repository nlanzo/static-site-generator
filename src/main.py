import sys
import os
import shutil
from copystatic import copy_from_static_to_public
from textnode import TextNode, TextType
from htmlnode import HTMLNode
from generate_page import generate_pages_recursive


dir_path_public = "./docs"
dir_path_static = "./static"

content_path = "./content"
template_path = "./template.html"
dest_path = "./docs"

def main():
    basepath = sys.argv[1]
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying files from static to public")
    copy_from_static_to_public(dir_path_static, dir_path_public)
    print("Done")

    generate_pages_recursive(content_path, template_path, dest_path, basepath)

    

    
main()