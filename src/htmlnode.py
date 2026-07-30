
class HTMLNode:
    def __init__(self, tag, value=None, children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError("to_html method must be implemented by subclasses")
    def props_to_html(self):
        if not self.props:
            return ''
        return ' '.join(f'{key}="{value}"' for key, value in self.props.items())
    def __repr__(self):
        return f"HTMLNode(tag='{self.tag}', value='{self.value}', children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        props_str = self.props_to_html()
        if self.tag is None:
            return self.value
        if props_str:
            return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    def __repr__(self):
        return f"LeafNode(tag='{self.tag}', value='{self.value}', props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        
        props_str = self.props_to_html()
        if props_str:
            opening_tag = f"<{self.tag} {props_str}>"
        else:
            opening_tag = f"<{self.tag}>"
        children_html = ''.join(child.to_html() for child in self.children)
        closing_tag = f"</{self.tag}>"
        return f"{opening_tag}{children_html}{closing_tag}"
    def __repr__(self):
        return f"ParentNode(tag='{self.tag}', children={self.children}, props={self.props})"