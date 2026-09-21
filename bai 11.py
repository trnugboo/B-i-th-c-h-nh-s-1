n = int(input("Nhập một số n(1-9):"))
print("Bảng cửu chương của", n)
for i in range(1, 11):
    if 1<=n <=9:
        print(n, "x", i, "=", n*i)
