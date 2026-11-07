from transformers import AutoTokenizer

def run_tokenization():
    # Load BERT's pretrained tokenizer
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    
    text = "Large language models are powerful."
    
    print(f"Original text: {text}\n")
    
    # Convert sentence into tokens
    tokens = tokenizer.tokenize(text)
    print("Tokens:", tokens)
    
    # Convert tokens into token IDs with special tokens
    token_ids = tokenizer.encode(text, add_special_tokens=True)
    print("Token IDs:", token_ids)
    print("Number of tokens:", len(token_ids))
    
    # Decode token IDs back into text
    decoded = tokenizer.decode(token_ids)
    print("Decoded text:", decoded)

if __name__ == "__main__":
    run_tokenization()