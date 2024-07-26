#18_Identity Operators.py

#การเปรียบเทียบตัวแปรที่อ้างอิงถึงวัตถุเดียวกัน
a = [1, 2, 3]
b = a
print(a is b)
print(a is not b)

#การเปรียบเทียบตัวแปรที่อ้างอิงถึงวัตถุต่างกันแม้ว่าจะมีค่าเดียวกัน
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)
print(a is not b)