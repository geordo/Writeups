def ror(val, r_bits, max_bits):
    return ((val & (2 ** max_bits - 1)) >> r_bits % max_bits) | (val << (max_bits - (r_bits % max_bits)) & (2 ** max_bits - 1))

X = [0x52, 0xDF, 0xB3, 0x60, 0xF1, 0x8B, 0x1C, 0xB5, 0x57, 0xD1,
     0x9F, 0x38, 0x4B, 0x29, 0xD9, 0x26, 0x7F, 0xC9, 0xA3, 0xE9,
     0x53, 0x18, 0x4F, 0xB8, 0x6A, 0xCB, 0x87, 0x58, 0x5B, 0x39,
     0x1E]

flag = 'DH{'
for i in range(len(X)):
    X[i] ^= i 
    X[i] = ror(X[i], i & 7, 8)
    flag += chr(X[i])
flag += '}'

print(flag)

# DH{Roll_the_left!_Roll_the_right!}