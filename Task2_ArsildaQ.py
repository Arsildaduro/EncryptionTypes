# This task belongs to Arsilda Qato
import random
import string
from collections import Counter


# === Task 1: Generate Random Monoalphabetic Key ===
def generate_random_key():
    alphabet = list(string.ascii_uppercase)
    shuffled = alphabet[:]
    random.shuffle(shuffled)
    return dict(zip(alphabet, shuffled))


# === Task 2: Encrypt and Decrypt ===
def monoalphabetic_encrypt(text, key):
    return ''.join(
        key.get(char.upper(), char) if char.isalpha() else char
        for char in text
    )


def monoalphabetic_decrypt(ciphertext, key):
    reverse_key = {v: k for k, v in key.items()}
    return ''.join(
        reverse_key.get(char.upper(), char) if char.isalpha() else char
        for char in ciphertext
    )


# === Task 3: Enhanced Frequency Analysis (with fallback) ===
english_letter_frequency = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'H', 'R', 'D', 'L', 'C',
                            'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']


def frequency_analysis(ciphertext):
    """Analyze ciphertext letter frequencies and guess a substitution key."""
    filtered = [c.upper() for c in ciphertext if c.isalpha()]
    counts = Counter(filtered)

    # Fill in missing letters with zero counts to ensure 1-to-1 mapping
    for letter in string.ascii_uppercase:
        if letter not in counts:
            counts[letter] = 0

    sorted_cipher_letters = [item[0] for item in counts.most_common()]

    # Show frequency counts for clarity
    print("Frequency Counts of Ciphertext Letters:")
    for letter, count in counts.items():
        print(f"{letter}: {count}")

    guessed_mapping = {}
    for i, cipher_letter in enumerate(sorted_cipher_letters):
        if i < len(english_letter_frequency):
            guessed_mapping[cipher_letter] = english_letter_frequency[i]
        else:
            guessed_mapping[cipher_letter] = cipher_letter  # fallback

    return guessed_mapping


def decrypt_with_mapping(ciphertext, mapping):
    result = []
    for c in ciphertext:
        if c.upper() in mapping:
            replacement = mapping[c.upper()]
            result.append(replacement.lower() if c.islower() else replacement)
        else:
            result.append(c)
    return ''.join(result)


# === Task 4: Main Execution ===
def main():
    # Read original plaintext from file
    with open("PlainText.txt", "r", encoding="utf-8") as file:
        original_text = file.read()

    # 1. Generate and show key
    key = generate_random_key()
    print("Monoalphabetic Key:\n", key, "\n")

    # 2. Encrypt + Decrypt
    encrypted = monoalphabetic_encrypt(original_text, key)
    decrypted = monoalphabetic_decrypt(encrypted, key)

    print("Encrypted (Sample):")
    print(encrypted[:300], "\n")

    print("Decrypted (Sample):")
    print(decrypted[:300], "\n")

    # 3. Frequency Analysis to Guess Key
    guessed_key = frequency_analysis(encrypted)
    hacked = decrypt_with_mapping(encrypted, guessed_key)

    print("Guessed Mapping (Frequency Analysis):")
    print(guessed_key, "\n")

    print("Hacked Decryption (Sample):")
    print(hacked[:300])


if __name__ == "__main__":
    main()
