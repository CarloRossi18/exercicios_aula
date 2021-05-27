n = int(input('digite o tamanho da sequencia numerica: '))
i = 0
cneg = 0
cnulo = 0
cpos = 0
while i < n:
    i += 1
    num = int(input('digite um numero: '))
    if num > 0:
        cpos += 1
    elif num == 0:
        cnulo += 1
    else:
        cneg += 1
print(f'{cpos} positivo(s) \n {cnulo} nulo(s) \n {cneg} negativo(s)')

