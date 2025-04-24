from enum import Enum
from typing import Optional

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, TextNode):
            return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode(text={self.text!r}, type={self.text_type.value!r}, url={self.url!r})"
from enum import Enum
from typing import Optional

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    TEXT = "text"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text: str, text_type: TextType, url: Optional[str] = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other: object) -> bool:
	if not isinstance(other, TextNode):
		return False
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )

    def __repr__(self) -> str:
        return f"TextNode(text={self.text!r}, type={self.text_type.value!r}, url={self.url!r})"

