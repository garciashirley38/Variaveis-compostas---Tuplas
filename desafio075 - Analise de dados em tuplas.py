"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares."""


num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Mais um número: ')),
       int(input('Mais um: ')))
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 not in num:
    print('O número 3 não apareceu nenhuma vez')
else:
    print(f'O número 3 apareceu pela primeira vez na {num.index(3) + 1}ª posição')
print('Os valores pares digitados foram: ', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
