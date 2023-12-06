#Horóscopo
#Apresentação
print('\n\t\t\t  --  Horóscopo - Simples   --')

#Entradas
mes = int(input('Informe o mês do ano (1 a 12): '))
dia = int(input('Informe o dia: '))

#Condicional e saída
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    print(f'Nascidos em {dia} de {mes} são do signo de Áries')
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    print(f'Nascidos em {dia} de {mes} são do signo de Touro')
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    print(f'Nascidos em {dia} de {mes} são do signo de Gêmeos')
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 21):
    print(f'Nascidos em {dia} de {mes} são do signo de Câncer')

elif (mes == 7 and dia >= 22) or (mes == 8 and dia <= 22):
    print(f'Nascidos em {dia} de {mes} são do signo de Leão')
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    print(f'Nascidos em {dia} de {mes} são do signo de Virgem')
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    print(f'Nascidos em {dia} de {mes} são do signo de Libra')
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    print(f'Nascidos em {dia} de {mes} são do signo de Escorpião')

elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    print(f'Nascidos em {dia} de {mes} são do signo de Sargitário')
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    print(f'Nascidos em {dia} de {mes} são do signo de Capricórnio')
elif (mes == 1 and dia >= 19) or (mes == 2 and dia <= 19):
    print(f'Nascidos em {dia} de {mes} são do signo de Aquário')
elif (mes == 2 and dia >= 20) or (mes == 3 and dia <= 20):
    print(f'Nascidos em {dia} de {mes} são do signo de Peixes')