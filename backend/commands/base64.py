import base64

def encrypt():
    original_string = input("Nhập chuỗi cần mã hóa Base64: ").strip()
    encoded_bytes = base64.b64encode(original_string.encode('utf-8'))
    encoded_string = encoded_bytes.decode('utf-8')
    print("🔐 Chuỗi sau khi mã hóa Base64:", encoded_string)
    return encoded_string  # Trả về chuỗi đã mã hóa

def decrypt(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string.encode('utf-8'))
    decoded_string = decoded_bytes.decode('utf-8')
    print("🔓 Chuỗi sau khi giải mã:", decoded_string)

def main():
    encoded = encrypt()
    decrypt(encoded)

if __name__ == "__main__":
    main()

