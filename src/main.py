import os
import shutil
from copystatic import copy_from_static_to_public
from textnode import TextNode, TextType
from htmlnode import HTMLNode


dir_path_public = "../public"
dir_path_static = "../static"

def main():
    print("Deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying from files from static to public")
    copy_from_static_to_public(dir_path_static, dir_path_public)
    print("Done")
    pass




    
main()