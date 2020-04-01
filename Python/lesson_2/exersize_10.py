int_num = int(input())
n = 0

while int_num > 0:
    if int_num % 10 == 5:
        n += 1

    int_num = int_num // 10
print(n)