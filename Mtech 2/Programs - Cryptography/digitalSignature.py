import hashlib
def sign(message, key):
    hash_val = hashlib.sha256(message.encode()).hexdigest()
    return hash_val + key

def verify(message, signature, key):
    hash_val = hashlib.sha256(message.encode()).hexdigest()
    return signature == hash_val + key

msg = "CRYPTO"
key = "private"
sig = sign(msg, key)

print("Original Message:", msg)
print("Key:", key)
print("Generated Signature:", sig)
print("Verification Result:", verify(msg, sig, key))
