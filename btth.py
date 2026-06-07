blood_inventory = [
    "BL001-Nguyen Van A-O+-250-31/12/2026",
    "BL002-Tran Thi B-A--350-15/11/2026",
    "BL003-Le Van C-AB+-250-20/10/2026"
]

def display_inventory(inventory):
    # ham nay de split chuoi xong can le in ra danh sach voi tinh tong the tich
    if len(inventory) == 0:
        print("Kho máu hiện chưa có túi máu nào.")
    else:
        print("--- DANH SÁCH KHO MÁU ---")
        print(f"{'Mã Túi':<6} | {'Người Hiến':<16} | {'Nhóm Máu':<8} | {'Thể Tích':<8} | {'Ngày Hết Hạn'}")
        print("-" * 65)
        total_volume = 0
        for item in inventory:
            info = item.split("-")
            code = info[0]
            name = info[1]
            blood_type = info[2]
            volume = int(info[3])
            expiry = info[4]
            total_volume = total_volume + volume
            print(f"{code:<6} | {name:<16} | {blood_type:<8} | {volume} ml   | {expiry}")
        print("-" * 65)
        print("Tổng thể tích máu trong kho:", total_volume, "ml.")

def add_blood_bag(inventory):
    # ham nay de check trung ma voi check the tich bang try except xong append vao list
    print("--- NHẬP TÚI MÁU MỚI ---")
    code = input("Nhập mã túi máu mới: ").strip().upper()
    if code == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    trung = False
    for item in inventory:
        info = item.split("-")
        if info[0] == code:
            trung = True
            break
            
    if trung == True:
        print("Lỗi: Mã túi máu", code, "đã tồn tại! Vui lòng nhập mã khác.")
        return

    name = input("Nhập tên người hiến: ").strip().title()
    if name == "":
        print("Lỗi: Tên người hiến không được để trống!")
        return

    blood_type = input("Nhập nhóm máu: ").strip().upper()
    if blood_type == "":
        print("Lỗi: Nhóm máu không được để trống!")
        return

    try:
        volume = int(input("Nhập thể tích (ml): "))
        if volume <= 0:
            print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
            return
    except ValueError:
        print("Lỗi: Thể tích phải là số nguyên lớn hơn 0!")
        return

    date = input("Nhập ngày hết hạn (DD/MM/YYYY): ").strip()
    if date == "":
        print("Lỗi: Ngày hết hạn không được để trống!")
        return

    new_bag = code + "-" + name + "-" + blood_type + "-" + str(volume) + "-" + date
    inventory.append(new_bag)
    print("\nThành công: Đã nhập túi máu", code, "vào kho!")
    print("Sau khi chuẩn hóa, dữ liệu được lưu vào list là:")
    print(new_bag)

def update_expiry(inventory):
    # ham nay de dung split tach chuoi ra sua ngay het han o index 4 roi join lai ghi de
    print("--- GIA HẠN / SỬA NGÀY HẾT HẠN ---")
    code = input("Nhập mã túi máu cần cập nhật: ").strip().upper()
    if code == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    found_index = -1
    for index in range(len(inventory)):
        info = inventory[index].split("-")
        if info[0] == code:
            found_index = index
            break

    if found_index == -1:
        print("Lỗi: Không tìm thấy túi máu", code, "trong kho!")
        return

    new_date = input("Nhập ngày hết hạn mới: ").strip()
    if new_date == "":
        print("Lỗi: Ngày hết hạn mới không được để trống!")
        return

    info_list = inventory[found_index].split("-")
    info_list[4] = new_date
    inventory[found_index] = "-".join(info_list)
    print("Thành công: Đã cập nhật ngày hết hạn cho túi máu", code + "!")

def remove_blood_bag(inventory):
    # ham nay de tim ma tui mau va xoa khoi danh sach bang remove
    print("--- XUẤT / HỦY TÚI MÁU ---")
    code = input("Nhập mã túi máu cần xuất/hủy: ").strip().upper()
    if code == "":
        print("Lỗi: Mã túi máu không được để trống!")
        return

    target_item = ""
    for item in inventory:
        info = item.split("-")
        if info[0] == code:
            target_item = item
            break

    if target_item == "":
        print("Lỗi: Không tìm thấy túi máu", code, "trong kho!")
    else:
        inventory.remove(target_item)
        print("Thành công: Đã xuất túi máu", code, "khỏi kho!")

while True:
    print("\n=== HỆ THỐNG QUẢN LÝ KHO MÁU RIKKEI ===")
    print("1. Xem danh sách túi máu trong kho")
    print("2. Nhập túi máu mới")
    print("3. Gia hạn / Sửa ngày hết hạn")
    print("4. Xuất / Hủy túi máu")
    print("5. Thoát chương trình")
    print("=======================================")
    
    choice = input("Chọn chức năng (1-5): ").strip()
    
    match choice:
        case "1":
            display_inventory(blood_inventory)
        case "2":
            add_blood_bag(blood_inventory)
        case "3":
            update_expiry(blood_inventory)
        case "4":
            remove_blood_bag(blood_inventory)
        case "5":
            print("Cảm ơn bác sĩ đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")