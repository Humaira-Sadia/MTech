# pip install pycryptodome
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

text = b'SECRET42'
key = b'8bytekey'

cipher = DES.new(key, DES.MODE_ECB)

enc = cipher.encrypt(pad(text, 8))
dec = unpad(cipher.decrypt(enc), 8)

print("Original Text:", text)
print("Key:", key)
print("Encrypted Text:", enc)
print("Decrypted Text:", dec)
