stone1 = int(input('Ввидите число: '))
if stone1 < 3 or stone1 > 20:
        print("Число вне параметров")
        quit()
list_l = []
list_j = []
sum_ = []
res_ = []
result = []
a = []
b = []
for l  in range(1,21):
    list_l.append(l)
    if l > stone1:
        break
    for j in range(2,21):
        list_j.append(j)
        if j > stone1:
            break
        sum = l + j
        sum_.append(sum)
        if sum > stone1:
            break
        if (stone1 % sum) == 0:
            if l >= j:
                continue
            a.append(l)
            b.append(j)
for a1 in zip(a, b):
    res_.append(a1)
for lis in res_:
    for cor in lis:
        result.append(cor)
result_ = ''.join(str(item) for item in result)
print('Пароль:', result_)




import random

number = random.randint(3,21)

list = []
for i in range(1, number):
    for j in range(1, number):
        if i >= j:
            continue
        if number % (i + j) == 0:
            list.append(i)
            list.append(j)
print(list)
