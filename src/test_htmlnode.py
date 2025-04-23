from htmlnode import HTMLNode

def test_props_to_html_empty():
	node = HTMLNode(tag="a", value="Click here", props={})
	assert node.props_to_html() == ""

def test_props_to_html_single():
	node = HTMLNode(props={"href": "https://example.com"})
	assert node.props_to_html() == ' href="https://example.com"'

def test_props_to_html_multiple():
	node = HTMLNode(props={"href": "https://example.com", "target": "_blank"})
	html = node.props_to_html()
	assert ' href="https://example.com"' in html
	assert ' target="_blank"' in html
	assert html.count('=') == 2

if __name__ == "__main__":
	test_props_to_html_empty()
	test_props_to_html_single()
	test_props_to_html_multiple()
	print("All tests passed!")
