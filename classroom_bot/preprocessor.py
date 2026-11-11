"""Preprocessing module using Python re.sub."""
import re

def preprocess_query(query: str) -> str:
    """Cleans punctuation, trims whitespace, removes polite filler prefixes, and lowercases text."""
    if not query:
        return ""

    text = query.strip().lower()

    # Strip conversational filler prefixes like "please tell me", "can you show", etc.
    filler_pattern = r'^(?:(?:can|could)\s+you\s+(?:please\s+)?(?:tell\s+me|show\s+me|inform\s+me|give\s+me)?\s*|please\s+(?:tell\s+me|show\s+me|inform\s+me|give\s+me)?\s*|tell\s+me\s+(?:about\s+)?|show\s+me\s+)'
    text = re.sub(filler_pattern, '', text, flags=re.IGNORECASE)

    # Replace punctuation (except alphanumeric and single spaces)
    text = re.sub(r'[^\w\s]', ' ', text)

    # Collapse multiple whitespace into a single space
    text = re.sub(r'\s+', ' ', text).strip()

    return text
