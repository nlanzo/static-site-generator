class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return "".join(list(map(lambda x: f' {x[0]}="{x[1]}"', self.props.items())))
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, props: {self.props})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)


    def to_html(self):
        if self.value == None:
            raise ValueError("leaf nodes must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, props: {self.props})"
        

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("a ParentNode must have a tag. Currently None")
        if self.children == None:
            raise ValueError("a ParentNode must have children. Currently None")
        
        for child in self.children:
            if not isinstance(child, HTMLNode):
                raise ValueError("all children of a ParentNode must be HTMLNodes")
        
        return f"<{self.tag}{self.props_to_html()}>" + "".join(list(map(lambda x: x.to_html(), self.children))) + f"</{self.tag}>"

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, props: {self.props})"