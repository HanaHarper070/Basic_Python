#04_Arithmetic Operators_Floor Division.py
bottles = int(input("กรุณากรอกจำนวนขวดน้ำ: "))
box_capacity = 6 # แต่ละกล่องใส่น้ำได้ 6 ขวด
boxes = bottles // box_capacity
remaining_bottles = bottles % box_capacity
print(f"มีน้ำจำนวน {bottles} ขวด ต้องใช้ {boxes} กล่อง และจะเหลือขวดน้ำ {remaining_bottles} ขวด")
