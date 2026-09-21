import random
so_bi_mat = random.randint(1, 10)
du_doan = 0
while du_doan != so_bi_mat:
    du_doan = int(input("Đoán một số từ 1 đến 10: "))

    if du_doan < so_bi_mat:
        print("Lớn hơn")
    elif du_doan > so_bi_mat:
        print("Nhỏ hơn")
    else:
        print("Chính xác! Bạn đã đoán đúng.")