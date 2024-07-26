#10_Assignment Operators_ex.py
investment = float(input("กรุณากรอกจำนวนเงินลงทุน: "))
years = int(input("กรุณาจำนวนปีที่ลงทุน: "))
growth_rate = 1.05  # 5% growth
growth_rate **= years # growth_rate ** years
investment *= growth_rate  # investment * (growth_rate ** years)
print(investment, "บาท") # investment **= growth_rate ** years
# investment = investment * (growth_rate ** years)
