k = int(input('Введите число: '))
f = ''
for i in range(1, k // 2 + 1):
    for j in range(i + 1, k):
        if k % (i + j) == 0:
            f += str(i) + str(j)
print(f)
