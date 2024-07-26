#19_String Operators String Methods_06.py
text = "Hello, world"

# เปลี่ยนเป็นตัวพิมพ์ใหญ่
upper_text = text.upper()
print(upper_text)  # ผลลัพธ์: "HELLO, WORLD"

# เปลี่ยนเป็นตัวพิมพ์เล็ก
lower_text = text.lower()
print(lower_text)  # ผลลัพธ์: "hello, world"

# แทนที่คำว่า "world" ด้วย "Python"
replaced_text = text.replace("world", "Python")
print(replaced_text)  # ผลลัพธ์: "hello, Python"

# หาตำแหน่งของคำว่า "world"
position = text.find("world")
print(position)  # ผลลัพธ์: 7

# แยกสตริงด้วย comma
words = text.split(", ")
print(words)  # ผลลัพธ์: ['hello', 'world']

# รวมสตริงในรายการด้วยเครื่องหมาย comma
#words = ['Hello', 'world']
joined_text = ", ".join(words)
print(joined_text)