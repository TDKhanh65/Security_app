def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    try:
        shift_input = input("Nhập độ dịch chuyển (shift): ").strip()
        shift = int(shift_input)
        if shift < 0:
            print("❌ Độ dịch chuyển phải là số nguyên không âm.")
            return
    except ValueError:
        print("❌ Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
        return

    chuoi_goc = input("Nhập chuỗi cần mã hóa Caesar: ").strip()
    if not chuoi_goc:
        chuoi_goc = "Hello world"  # Chuỗi mặc định

    ma_hoa = encrypt(chuoi_goc, shift)
    giai_ma = decrypt(ma_hoa, shift)

    print("🔐 Mã hóa Caesar:", ma_hoa)
    print("🔓 Giải mã Caesar:", giai_ma)

if __name__ == "__main__":
    main()
