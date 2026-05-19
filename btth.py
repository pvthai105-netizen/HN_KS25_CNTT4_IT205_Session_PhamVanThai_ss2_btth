print(" --- HỆ THỐNG QUẢN LÝ PHÒNG KHÁM --- ")

name = input("Nhập tên bệnh nhân: ").strip()
year_of_birth = int(input("Nhập năm sinh: "))
days_sick = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
base_fee = int(input("Nhập chi phí khám (VND): "))

CURRENT_YEAR = 2026

if name == "":
    print("\n[LỖI] Tên không được để trống!")
elif year_of_birth < 1900 or year_of_birth > CURRENT_YEAR:
    print(f"\n[LỖI] Năm sinh không hợp lệ! Phải nằm trong khoảng 1900 đến {CURRENT_YEAR}.")
elif days_sick < 0:
    print("\n[LỖI] Số ngày bị bệnh phải lớn hơn hoặc bằng 0!")
elif temperature < 30 or temperature > 45:
    print("\n[LỖI] Nhiệt độ không hợp lệ! Phải nằm trong khoảng 30 đến 45°C.")
elif base_fee <= 0:
    print("\n[LỖI] Chi phí khám phải lớn hơn 0!")
else:
    age = CURRENT_YEAR - year_of_birth
    surcharge = base_fee * 0.10
    total_fee = base_fee + surcharge

    if temperature > 38 and days_sick > 3:
        health_status = "Nguy hiểm"
    elif temperature > 38:
        health_status = "Sốt cao"
    elif temperature > 37.5:
        health_status = "Sốt nhẹ"
    else:
        health_status = "Bình thường"

    if health_status == "Nguy hiểm":
        if age > 60:
            priority_level = "Cấp cứu"
        else:
            priority_level = "Ưu tiên cao"
    else:
        priority_level = "Bình thường"

    cost_level = "Cao" if total_fee > 500000 else "Thấp"

    print("----KẾT QUẢ----")
    print(f"Tên: {name}")
    print(f"Tuổi: {age}")
    print(f"Nhiệt độ: {temperature:.1f} °C")
    print(f"Số ngày bệnh: {days_sick}")

    print(f"Tình trạng: {health_status}")
    print(f"Mức độ ưu tiên: {priority_level}")
    
    print(f"Tổng chi phí: {total_fee:,} VND")
    print(f"Mức chi phí: {cost_level}")
