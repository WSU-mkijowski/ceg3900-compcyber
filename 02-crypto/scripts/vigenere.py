import sys

def vigenere_cipher(text, key, mode='encrypt'):
    """
    Performs Vigenere encryption or decryption.
    mode='encrypt' or 'decrypt'
    """
    result = ""
    key = key.upper()
    key_index = 0
    alphabet_len = 26
    
    for char in text:
        if 'A' <= char.upper() <= 'Z':
            is_upper = char.isupper()
            char_index = ord(char.upper()) - ord('A')
            key_char = key[key_index % len(key)]
            key_char_index = ord(key_char) - ord('A')
            
            if mode == 'encrypt':
                new_index = (char_index + key_char_index) % alphabet_len
            elif mode == 'decrypt':
                new_index = (char_index - key_char_index + alphabet_len) % alphabet_len
            
            new_char = chr(new_index + ord('A'))
            result += new_char if is_upper else new_char.lower()
            key_index += 1
        else:
            result += char # Append non-alphabetic characters as is

    return result

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python vigenere.py <mode> <key> <text_or_file>")
        print("Mode: encrypt or decrypt")
        print("Text can be a string or a filename (prefix with file: for filename)")
        sys.exit(1)
    
    mode = sys.argv[1]
    key = sys.argv[2]
    content_source = sys.argv[3]

    if content_source.startswith("file:"):
        filename = content_source[5:]
        try:
            with open(filename, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            sys.exit(1)
    else:
        content = content_source
    
    output = vigenere_cipher(content, key, mode)
    print(output)

