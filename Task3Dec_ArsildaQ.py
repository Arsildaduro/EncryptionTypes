# This task belongs to Arsilda Qato



from Task3Enc_ArsildaQ import generate_keys, bytes_to_bits, bits_to_bytes, des_block


def decrypt(cipher, key):
    keys = generate_keys(bytes_to_bits(key))[::-1]  # Reverse keys for decryption
    plain = b''
    for i in range(0, len(cipher), 8):
        block = bytes_to_bits(cipher[i:i + 8])
        decrypted = bits_to_bytes(des_block(block, keys))
        plain += decrypted
    # Remove PKCS#7 padding
    pad_len = plain[-1]
    if 1 <= pad_len <= 8 and plain[-pad_len:] == bytes([pad_len] * pad_len):
        return plain[:-pad_len]
    return plain


if __name__ == '__main__':
    with open('encrypted.bin', 'rb') as f:
        ciphertext = f.read()

    with open('key.bin', 'rb') as f:
        key = f.read()

    plaintext = decrypt(ciphertext, key)

    print("\nDecryption Results:")
    print(f"Decrypted text: {plaintext.decode('utf-8')}")