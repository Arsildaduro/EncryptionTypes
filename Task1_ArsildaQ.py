# This task belongs to Arsilda Qato
import random
import time

# === Task 1: Generate a random key (a, b) for Affine Cipher ===

def gcd(a, b):

    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = len(alphabet)
char_to_index = {char: idx for idx, char in enumerate(alphabet)}
index_to_char = {idx: char for idx, char in enumerate(alphabet)}

def affine_encrypt(text, a, b):
    """Encrypt text using Affine Cipher formula: E(x) = (a*x + b) mod m"""
    encrypted = ''
    for char in text.upper():
        if char in char_to_index:
            x = char_to_index[char]
            encrypted += index_to_char[(a * x + b) % m]
        else:
            encrypted += char
    return encrypted

def affine_decrypt(ciphertext, a, b):
    """Decrypt text using formula: D(y) = a_inv * (y - b) mod m"""
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return None
    decrypted = ''
    for char in ciphertext:
        if char in char_to_index:
            y = char_to_index[char]
            decrypted += index_to_char[(a_inv * (y - b)) % m]
        else:
            decrypted += char
    return decrypted

# Load input text
with open("PlainText.txt", "r", encoding="utf-8") as file:
    original_text = file.read()

# Generate valid values for a and b
valid_a = [x for x in range(1, m) if gcd(x, m) == 1]
a = random.choice(valid_a)
b = random.randint(0, m - 1)
key = (a, b)
print(f"Generated Key: a = {a}, b = {b}")

# === Task 2: Generate the Encrypted and Decrypted Text ===

# Encrypt the original text (no cleaning)
encrypted_text = affine_encrypt(original_text, a, b)

# Decrypt it back using the same key
decrypted_text = affine_decrypt(encrypted_text, a, b)

# Show sample output from both
print("\n--- Encrypted Text Sample ---\n", encrypted_text[:312])
print("\n--- Decrypted Text Sample ---\n", decrypted_text[:312])

# === Task 3: Brute Force Hack

def brute_force_affine(ciphertext):
    start = time.time()

    best_result = None
    best_key = None

    for a in range(1, m):
        if gcd(a, m) != 1:
            continue
        for b in range(m):
            decrypted = affine_decrypt(ciphertext, a, b)
            if decrypted:
                print(f"\n--- Trying Key a = {a}, b = {b} ---")
                print(decrypted[:312])
                if best_result is None:
                    best_result = decrypted
                    best_key = (a, b)

    end = time.time()
    hack_time = end - start

    return best_result, best_key, hack_time

# === Task 4: Record the time taken by Oscar (in seconds) ===

# Run the brute force attack
best_result, best_key, hack_time = brute_force_affine(encrypted_text)

# Print the time taken for brute force hacking (in seconds)
print(f"\nTime taken for brute force hacking by Oscar: {hack_time:.4f} seconds")


