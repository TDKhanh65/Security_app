def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = ''
    for i in range(len(plaintext)):
        x = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        c = (x + k) % 26
        ciphertext += chr(c + ord('A'))
    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = ''
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        x = (c - k + 26) % 26  # +26 để tránh giá trị âm
        plaintext += chr(x + ord('A'))
    return plaintext

def main():
    plaintext = input("🔐 Nhập văn bản gốc: ").strip().upper()
    if not plaintext.isalpha():
        print("❌ Văn bản gốc chỉ chứa chữ cái A-Z.")
        return

    key = input("🔑 Nhập khóa: ").strip().upper()
    if not key.isalpha() or len(key) != len(plaintext):
        print("❌ Khóa phải chứa chữ cái A-Z và có độ dài bằng văn bản gốc.")
        return

    cipher = encrypt(plaintext, key)
    print("\n📄 Mã hóa:", cipher)

    decrypted = decrypt(cipher, key)
    print("🔓 Giải mã lại:", decrypted)

if __name__ == "__main__":
    main()
