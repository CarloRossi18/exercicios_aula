n = int(input('Digite um número para ver sua fatoração: '))
fator = 2

while n > 1:
    mult = 0
    while n % fator == 0:
        mult += 1
        n /= fator
    if mult > 0:
        print(f'fator {fator} tem multiplicidade {mult}')
    fator += 1
