import re

def clean_text(text: str) -> str:
    # Strip unnecessary whitespace, convert to lowercase, and clean up punctuation/symbols
    text = text.strip()
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\w\s]", "", text)
    return text

if __name__ == "__main__":
    # Expanded set of test sentences
    sample_texts = [
        "   I NEED HELP!!!   ",
        "Hello World... How are you doing today??",
        "Python is AMAZING for Data Science & Machine Learning!   ",
        "   Data Science, NLP, and LLMs are transforming software engineering...   "
    ]

    print("--- Running Text Preprocessing Pipeline ---\n")
    for original in sample_texts:
        cleaned = clean_text(original)
        print(f"Original: {original}")
        print(f"Cleaned:  {cleaned}\n")