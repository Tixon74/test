int_num = int(input())

while int_num > 0:
    if int_num % 10 == 5:
        print('yes')
        break
    int_num = int_num // 10
else: print('no')