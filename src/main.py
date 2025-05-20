from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    text_node = TextNode("test test test", TextType.BOLD, "www.internet.com")
    print(text_node)

    html_node = HTMLNode("h1", "Title", HTMLNode("p", "hello"), props={"href": "https://www.google.com"})
    print(html_node)
    
main()