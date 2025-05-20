import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode("h1", "Title", props={"href": "https://www.google.com", "alt": "google link"})
        props_to_html = node.props_to_html()
        correct_props = ' href="https://www.google.com" alt="google link"'
        self.assertEqual(props_to_html, correct_props)

    def test_props_to_html_with_no_props(self):
        node = HTMLNode("h1", "Title")
        props_to_html = node.props_to_html()
        correct_props = ''
        self.assertEqual(props_to_html, correct_props)

    def test_repr(self):
        node = HTMLNode("h1", "Title", HTMLNode("p", "hello"), {"href": "https://www.google.com", "alt": "google link"})
        repr = node.__repr__()
        correct_repr = "HTMLNode(h1, Title, HTMLNode(p, hello, None, None), {'href': 'https://www.google.com', 'alt': 'google link'})"
        self.assertEqual(repr, correct_repr)
