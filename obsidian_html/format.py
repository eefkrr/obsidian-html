import regex as re
from obsidian_html.utils import slug_case, md_link


def format_tags(document):
    """Obsidian style tags. Removes #-icon and adds a span tag."""
    matches = re.finditer(r"\s#([\p{L}_]+)", document)

    for match in matches:
        document = document.replace(
            match.group(), "<span class=\"tag\">" + match.group(1) + "</span>")

    return document


def format_blockrefs(document):
    """Formats Obsidian block references into a span element that can be linked to"""
    regex = re.compile(r" \^(.+)$", re.MULTILINE)
    matches = regex.finditer(document)

    for match in matches:
        document = document.replace(match.group(), f"<spand id=\"{match.group(1)}\"></span>")
        
    return document