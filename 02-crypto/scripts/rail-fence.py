import sys

def decrypt_rail_fence(cipher, rails):
    length = len(cipher)
    # Create the rail matrix and mark the positions with '*'
    rail = [['\n' for _ in range(length)] for _ in range(rails)]
    dir_down = False
    row, col = 0, 0
    for i in range(length):
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        rail[row][col] = '*'
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    
    # Fill the rail matrix with ciphertext
    index = 0
    for i in range(rails):
        for j in range(length):
            if rail[i][j] == '*' and index < length:
                rail[i][j] = cipher[index]
                index += 1
    
    # Read the matrix in zigzag manner to get the original text
    result = []
    row, col = 0, 0
    dir_down = False
    for i in range(length):
        if row == 0 or row == rails - 1:
            dir_down = not dir_down
        if rail[row][col] != '*': # Should always have a char here now
            result.append(rail[row][col])
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 rail_decode.py <ciphertext> <number_of_rails>")
        sys.exit(1)
    
    ciphertext = sys.argv[1]
    try:
        rails = int(sys.argv[2])
    except ValueError:
        print("Number of rails must be an integer.")
        sys.exit(1)
        
    decrypted_message = decrypt_rail_fence(ciphertext, rails)
    print(decrypted_message)

