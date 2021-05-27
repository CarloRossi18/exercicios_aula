n = int(input('Digite um número inteiro: '))
while n >= 0:
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    print(fat)
    m = int(input())