from block_markdown import extract_title, markdown_to_html_node
import os


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        markdown = file.read()
    with open(template_path) as file:
        template = file.read()
    
    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    page = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    
    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    with open(dest_path, "w") as file:
        file.write(page)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    files = os.listdir(dir_path_content)

    for file in files:
        from_path = os.path.join(dir_path_content, file)
        to_path = os.path.join(dest_dir_path, file)
        if os.path.isfile(from_path):
            filename = f"{to_path[:-3]}.html"
            generate_page(from_path, template_path, filename, basepath)
        else:
            generate_pages_recursive(from_path, template_path, to_path, basepath)
