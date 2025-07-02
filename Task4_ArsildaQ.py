# This task belongs to Arsilda Qato

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Step 1: Read the input file
with open("PlainText.txt", "rb") as file:
    plaintext = file.read()

# Step 2: Prepare key and IV
key = b'8bytekey'  # DES key must be exactly 8 bytes
iv = get_random_bytes(8)  # IV must also be 8 bytes for DES

# Step 3: Encrypt using DES in CFB mode
cipher_encrypt = DES.new(key, DES.MODE_CFB, iv)
ciphertext = cipher_encrypt.encrypt(plaintext)

# Step 4: Save encrypted data to file
with open("Encrypted_DES_CFB.bin", "wb") as enc_file:
    enc_file.write(iv + ciphertext)  # store IV + ciphertext together

# Step 5: Decrypt to verify
# (In practice, you'd retrieve the IV from the file)
with open("Encrypted_DES_CFB.bin", "rb") as enc_file:
    stored_data = enc_file.read()
    iv_from_file = stored_data[:8]
    ciphertext_from_file = stored_data[8:]

    cipher_decrypt = DES.new(key, DES.MODE_CFB, iv_from_file)
    decrypted = cipher_decrypt.decrypt(ciphertext_from_file)

# Step 6: Save decrypted text to file for verification
with open("Decrypted_DES_CFB.txt", "wb") as dec_file:
    dec_file.write(decrypted)

print("Key (hex):", key.hex())
print("IV (hex):", iv.hex())
print("Plaintext (full):", plaintext)
print("Ciphertext (hex, full):", ciphertext.hex())
print("Decrypted matches:", plaintext == decrypted)
