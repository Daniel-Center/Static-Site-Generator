from markdown_blocks import markdown_to_html_node, extract_title
import os

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")
    m = open(from_path, 'r')
    markdown = m.read()
    t = open(template_path, 'r')
    template = t.read()
    node = markdown_to_html_node(markdown)
    content = node.to_html()
    title = extract_title(markdown)
    i = template.replace('{{ Title }}', title)
    index = i.replace('{{ Content }}', content)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(index)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    dir_list = os.listdir(dir_path_content)
    print(dir_list)
    for item in dir_list:
        test = os.path.join(dir_path_content, item)
        print(test)
        if os.path.isfile(test):
            to_file = os.path.join(dest_dir_path, 'index.html')
            from_file = os.path.join(dir_path_content, item)
            generate_page(from_file, template_path, to_file)
        if os.path.isdir(test):
            sub_path = os.path.join(dir_path_content, item)
            print(sub_path)
            dst_path = os.path.join(dest_dir_path, item)
            print(dst_path)
            os.makedirs(dst_path, exist_ok=True)
            generate_pages_recursive(sub_path, template_path, dst_path)
    
    
