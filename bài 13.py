n = int(input("Nhập số lượng phần tử: "))
so_chan = 0
for i in range(n):
    so = int(input(f"Nhập số thứ {i + 1}: "))
    if so % 2 == 0:
        so_chan = so_chan + 1
print("Có", so_chan, "số chẵn.")