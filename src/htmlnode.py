
class HTMLnode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not Implemented yet")

    def props_to_htnl(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            prop_html += f'{prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return  "TAG:  " + str(self.tag) + " - " + "VALUE:   " + str(self.value) + " - " + str(self.children) + " -" + str(self.props)
