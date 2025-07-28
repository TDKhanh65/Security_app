def encrypt(plain_text, key):
    plain_text = plain_text.upper()
    key = key.upper()
    encrypted = ''
    for i, char in enumerate(plain_text):
        if char.isalpha():
            shift = (ord(char) - 65 + ord(key[i % len(key)]) - 65) % 26
            encrypted += chr(shift + 65)
        else:
            encrypted += char  # Giữ nguyên ký tự không phải chữ cái
    return encrypted

def decrypt(cipher_text, key):
    cipher_text = cipher_text.upper()
    key = key.upper()
    decrypted = ''
    for i, char in enumerate(cipher_text):
        if char.isalpha():
            shift = (ord(char) - 65 - (ord(key[i % len(key)]) - 65)) % 26
            decrypted += chr(shift + 65)
        else:
            decrypted += char  # Giữ nguyên ký tự không phải chữ cái
    return decrypted

def main():
    chuoi_goc = input("🔐 Nhập chuỗi cần mã hóa: ").strip()
    key = input("🔑 Nhập khóa: ").strip()

    if not chuoi_goc or not key:
        print("❌ Chuỗi và khóa không được để trống.")
        return

    chuoi_ma_hoa = encrypt(chuoi_goc, key)
    print("\n🧪 Chuỗi đã mã hóa:", chuoi_ma_hoa)

    chuoi_giai_ma = decrypt(chuoi_ma_hoa, key)
    print("🔓 Giải mã lại:", chuoi_giai_ma)

if __name__ == "__main__":
    main()
