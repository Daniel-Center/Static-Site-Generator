from textnode import *
from htmlnode import *
from markup_to_html import *
from markdown_blocks import *
from copy_dir import *
from generate_page import *

dst = './public'
src = './static'
c = './content'
t = './template.html'


def main():
    if os.path.exists(dst):
        if len(os.listdir(dst)) > 0:
            shutil.rmtree(dst)
    copy_dir(src, dst)
    generate_pages_recursive(c,t,dst)


main()
