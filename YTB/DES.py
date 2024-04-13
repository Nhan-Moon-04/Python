from Crypto.Cipher import DES
import binascii

# Hàm chuyển đổi từ hex sang nhị phân
def hex_to_bin(hex_str):
    return binascii.unhexlify(hex_str)

# Hàm chuyển đổi từ nhị phân sang hex
def bin_to_hex(bin_str):
    return binascii.hexlify(bin_str)

# Hàm mã hóa DES
def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(message)

# Thông điệp và khóa dưới dạng hex
M_hex = "0123456789ABCDEF"
K_hex = "13345799BBCDDFF1"

# Chuyển đổi thành dạng nhị phân
M_binary = hex_to_bin(M_hex)
K_binary = hex_to_bin(K_hex)

# Mã hóa DES
encrypted_message = des_encrypt(M_binary, K_binary)

# Kết quả mã hóa dưới dạng hex
encrypted_message_hex = bin_to_hex(encrypted_message)
print("Kết quả mã hóa DES:", encrypted_message_hex)
