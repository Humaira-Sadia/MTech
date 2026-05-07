p = 29
g = 2

a = 7
b = 12

A = pow(g, a, p)
B = pow(g, b, p)

key1 = pow(B, a, p)
key2 = pow(A, b, p)

print("Public Values: p =", p, "g =", g)
print("Private Keys: a =", a, "b =", b)
print("Shared Key User1:", key1)
print("Shared Key User2:", key2)
