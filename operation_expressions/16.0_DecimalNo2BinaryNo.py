#16.0_DecimalNo2BinaryNo.py
try :
    base10 = int(input('กรุณาป้อนตัวเลขฐานสิบ : '))
except:
    base10 = 0
print('ตัวเลขฐาน 10 คือ', base10, 'แปลงเป็นเลขฐาน 2 ได้', bin( base10 ))
