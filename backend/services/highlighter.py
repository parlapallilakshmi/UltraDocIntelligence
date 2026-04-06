import re

def highlight_text(source, answer):
    words = [w for w in re.findall(r'\w+', answer) if len(w) > 4]

    highlighted = source

    for w in set(words):
        highlighted = re.sub(
            f"({w})",
            r"<mark>\1</mark>",
            highlighted,
            flags=re.IGNORECASE
        )

    return highlighted