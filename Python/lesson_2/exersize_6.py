int_num = int(input())
sum = 0

while int_num > 0:
    sum += int_num % 10
    int_num = int_num // 10
print(sum)