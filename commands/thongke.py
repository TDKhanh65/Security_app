from collections import Counter

def decrypt():
    chuoi = input("🔐 Nhập chuỗi thống kê: ").replace(" ", "")
    thong_ke = Counter(chuoi)

    print("Tần suất xuất hiện:")
    for ky_tu, so_lan in thong_ke.items():
        print(f"{ky_tu}: {so_lan}")

    # Sắp xếp theo tần suất giảm dần
    sap_xep = thong_ke.most_common()
    print("\nSắp xếp theo tần suất:")
    for ky_tu, so_lan in sap_xep:
        print(f"{ky_tu}: {so_lan}")
    
    return sap_xep  # trả về danh sách đã sắp xếp

def main():
    sap_xep = decrypt()  # gọi hàm decrypt() và nhận kết quả trả về
    ky_tu_pho_bien, tan_suat = sap_xep[0]
    print(f"\n🔎 Dự đoán: ký tự xuất hiện nhiều nhất là '{ky_tu_pho_bien}' ({tan_suat} lần)")

if __name__ == "__main__":
    main()
