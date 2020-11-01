import regex as re
from obsidian_html.utils import slug_case, md_link

LINK_SYNTAX = {
    "#": "header",
    "|": "alias",
    "#^": "blockref"
}

class Link:
    def __init__(self, obsidian_link):
        self.obsidian_link = obsidian_link
        extended_link = re.match(r"([^#|^\n]+)([#|]\^?)(.*)", obsidian_link)
        if extended_link:
            self.file = extended_link.group(1)
            setattr(self, LINK_SYNTAX[extended_link.group(2)], extended_link.group(3))
        else:
            self.file = obsidian_link
        
        self.slug = slug_case(self.file)
        
    def md_link(self):
        """Returns a link string that follows the Markdown specification"""
        if hasattr(self, "alias"):
            alias = getattr(self, "alias")
            return md_link(alias, self.slug)
        elif hasattr(self, "header"):
            header = getattr(self, "header")
            return md_link(header, f"{self.slug}#{slug_case(header)}")
        elif hasattr(self, "blockref"):
            blockref = getattr(self, "blockref")
            return md_link(self.file, f"{self.slug}#{blockref}")
        else:
            return md_link(self.file, self.slug)
        
    def __eq__(self, other):
        return self.file == other.file