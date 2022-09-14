"""Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense."""

times = ('Atletico MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
         'Atlético-GO', 'Santos', 'Ceará', 'Internacional', 'São Paulo',
         'Atletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport Recife',
         'Chapecoense')
print(f'Lista de times do brasileirão:')
for t in times:
    print(t)
print('-'*100)
print(f'Os primeiros 5 colocados são: {times[0:5]}')
print('-'*100)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-'*100)
print(f'Os times em ordem alfabética são: {sorted(times)}')
print('-'*100)
print(f'A Chapecoense esta na {times.index("Chapecoense")+1}ª posição')
