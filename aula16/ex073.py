priColocados2022 = ('Palmeiras', 'Flamengo', 'Corinthians ', 'Fluminense ', 'Athletico-PR ', 'Internacional ', 'Atlético-MG',
           'América-MG', 'Bragantino', 'Santos', 'São Paulo ', 'Botafogo', 'Goiás', 'Ceará ', 'Fortaleza', 'Cuiabá',
           'Avaí', 'Coritiba', 'Atletico-GO', 'Juventude')
print(f'Os cinco primeiros colocados foram {priColocados2022[:5]}')
print(f'Os últimos 4 colocados foram {priColocados2022[-4:]}')
print(f'Em ordem alfabética {sorted(priColocados2022)}')
print(f'O time Atletico-GO esta na posição {priColocados2022.index("Atletico-GO")+1}º')
