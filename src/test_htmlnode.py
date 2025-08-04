import unittest

from htmlnode import HTMLnode

class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        html = HTMLNode("p", "test successful", ["test", "successful!"], {"href": "https://marc-os.com"})
