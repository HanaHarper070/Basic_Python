#17_Membership Operators.py

# List
fruits = ['apple', 'banana', 'cherry']
print(fruits)
print("apple อยู่ในลิสใช่หรือไม่: ", 'apple' in fruits)
print("mango อยู่ในลิสใช่หรือไม่: ", 'mango' in fruits)
print("apple ไม่อยู่ในลิสใช่หรือไม่: ", 'apple' not in fruits)
print("mango ไม่อยู่ในลิสใช่หรือไม่: ", 'mango' not in fruits)

# String
sentence = "Hello, world!"
print(sentence)
print("คำว่า Hello อยู่ในกลุ่มคำนี้ใช่หรือไม่: ", 'Hello' in sentence)
print("คำว่า hi อยู่ในกลุ่มคำนี้ใช่หรือไม่: ",'hi' in sentence)
print("คำว่า Hello ไม่ได้อยู่ในกลุ่มคำนี้ใช่หรือไม่: ",'Hello' not in sentence)
print("คำว่า python ไม่ได้อยู่ในกลุ่มคำนี้ใช่หรือไม่: ",'python' not in sentence)