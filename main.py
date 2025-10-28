# Ghi chú: ví dụ tổng hợp các loại câu lệnh
import math  # nạp thư viện toán

# Khai báo biến
ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))

# Điều kiện
if tuoi >= 18:
    print(f"{ten} đã đủ tuổi trưởng thành.")
else:
    print(f"{ten} chưa đủ tuổi.")

# Vòng lặp for
for i in range(3):
    print("Lặp:", i)

# Vòng lặp while
x = 0
while x < 2:
    print("Đếm:", x)
    x += 1

# Hàm
def binh_phuong(n):
    return n ** 2

print("Bình phương của 4 là:", binh_phuong(4))

# Danh sách và từ điển
dich_vu = ["Cắt tóc", "Massage", "Tập gym"]
lich_hen = {"ten": ten, "dich_vu": dich_vu[0], "thoi_gian": "10:00"}

print("Chi tiết lịch hẹn:", lich_hen)
