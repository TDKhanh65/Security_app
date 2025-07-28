def encrypt(input_string, key):
    result = ""
    for i in range(len(input_string)):
        result += chr(ord(input_string[i]) ^ ord(key[i % len(key)]))
    return result

def decrypt(encrypted_string, key):
    return encrypt(encrypted_string, key)

def main():
    chuoi_goc = input("🔐 Nhập chuỗi cần mã hóa: ").strip()
    khoa = input("🔑 Nhập khóa (key): ").strip()

    ma_hoa = encrypt(chuoi_goc, khoa)
    print("\n🧪 Chuỗi sau khi mã hóa (dạng thô):", ma_hoa)

    ma_hoa_hex = ma_hoa.encode('utf-8').hex()
    print("📦 Mã hóa dạng hex:", ma_hoa_hex)

    giai_ma = decrypt(ma_hoa, khoa)
    print("\n🔓 Chuỗi sau khi giải mã:", giai_ma)

if __name__ == "__main__":
    main()
