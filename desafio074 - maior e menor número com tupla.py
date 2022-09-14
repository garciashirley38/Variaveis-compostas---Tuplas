"""Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla."""

"""from random import randint
numeros = cont = maior = menor = 0
print('Os valores sorteados são: ')
while cont < 5:
    numeros = randint(0, 100)
    print(numeros, end=' ')
    cont += 1
    if cont == 1:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros
print(f'\n O maior valor sortido foi: {maior} \n'
      f' E o menor foi: {menor}')"""

from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10),
     randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end=' ')
for numeros in n:
    print(f'{numeros}', end=' ')
print(f'\nO maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')
