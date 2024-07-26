#16_Bitwise Operators_ex2.py
lights = 0b0011  # ไฟดวงที่หนึ่งและดวงที่สองเปิด
mask = 0b1100   # เราต้องการเปิดไฟดวงที่สามและดวงที่สี่
result = lights | mask
print("สถานะของหลอดไฟ: ", bin(result))