#16_Bitwise Operators.py
a = 5      # 5 ในฐานสองคือ 0101
b = 3      # 3 ในฐานสองคือ 0011

result_band = a & b  # ผลลัพธ์: 0001 (1 ในฐานสิบ)
result_bor = a | b  # ผลลัพธ์: 0111 (7 ในฐานสิบ)
result_bxor = a ^ b  # ผลลัพธ์: 0110 (6 ในฐานสิบ)
result_bnot = ~a  # ผลลัพธ์: 1010 (ใน Python, ผลลัพธ์จะเป็น -6)

print("ผลลัพธ์ของ Bitwise and: ", result_band)
print("ผลลัพธ์ของ Bitwise or: ", result_bor)
print("ผลลัพธ์ของ Bitwise xor: ", result_bxor)
print("ผลลัพธ์ของ Bitwise not: ", result_bnot)