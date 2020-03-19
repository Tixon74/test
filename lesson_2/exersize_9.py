int_num = int(input())
max = 0

while int_num > 0:
    if int_num % 10 > max:
        max = int_num % 10
    int_num = int_num // 10
print(max)