def encrypt(chuoi, thu_tu):
    return ''.join([chuoi[i - 1] for i in thu_tu])

def decrypt(chuoi_ma_hoa, thu_tu):
    giai_ma = [''] * len(chuoi_ma_hoa)
    for i, vi_tri in enumerate(thu_tu):
        giai_ma[vi_tri - 1] = chuoi_ma_hoa[i]
    return ''.join(giai_ma)

def main():
    chuoi = input("🔐 Nhập chuỗi cần mã hóa: ").strip()
    thu_tu_input = input(f"🔢 Nhập thứ tự hoán vị (vd: 3 1 4 2 ...): ").strip()
    try:
        thu_tu = list(map(int, thu_tu_input.split()))
    except ValueError:
        print("❌ Thứ tự hoán vị phải là các số nguyên, phân cách bằng dấu cách.")
        return
    if len(chuoi) != len(thu_tu):
        print("❌ Độ dài chuỗi và thứ tự hoán vị phải bằng nhau.")
        return
    if any(i < 1 or i > len(chuoi) for i in thu_tu):
        print(f"❌ Các số trong thứ tự phải nằm trong khoảng từ 1 đến {len(chuoi)}.")
        return
    ket_qua_ma_hoa = encrypt(chuoi, thu_tu)
    print("\n🔏 Chuỗi sau khi mã hóa:", ket_qua_ma_hoa)

    ket_qua_giai_ma = decrypt(ket_qua_ma_hoa, thu_tu)
    print("🔓 Giải mã lại:", ket_qua_giai_ma)

if __name__ == "__main__":
    main()
