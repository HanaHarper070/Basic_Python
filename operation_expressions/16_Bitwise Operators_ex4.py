#16_Bitwise Operators_ex4.py
a = 0b0101  # ตัวเลขในรูปแบบบิต
result = ~a
result = result & 0b1111
print("สถานะของหลอดไฟ: ", bin(result))