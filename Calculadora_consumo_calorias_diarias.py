# CALCULANDO CONSUMO DE CALORIA DIÁRIA.
"""
Sedentário (pouco ou nenhum exercício): TMB x 1,2
Levemente ativo (exercício leve 1-3 dias/semana): TMB x 1,375
Moderadamente ativo (exercício moderado 3-5 dias/semana): TMB x 1,55
Altamente ativo (exercício pesado 6-7 dias/semana): TMB x 1,725
Extremamente ativo (exercício muito pesado e treinamento físico): TMB x 1,9 
HOMEM - 66,5 + (13,75 x peso em kg) + (5,003 x altura em cm) - (6,75 x idade)
MULHER - 655,1 + (9,563 x peso em kg) + (1,850 x altura em cm) - (4,676 x idade)
DÉFICIT CALÓRICO = calorias - 500
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')
sexo = input('Digite seu sexo: ')
nivel_de_exercicio = input('Digite seu nível de exercicio: ')

if nome and idade and altura and peso and sexo and nivel_de_exercicio:
    altura = float(altura)
    peso = float(peso)
    idade = float(idade)
    nivel_de_exercicio = nivel_de_exercicio.lower().strip()

    # Calcular TMB
    if sexo in ['masculino', 'homem']:
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * idade)
        print(f'{nome}, sua taxa metabólica basal é: {tmb:.2f}')
    elif sexo in ['feminino', 'mulher']:
        tmb = 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * idade)
        print(f'{nome}, sua taxa metabólica basal é: {tmb:.2f}')
    else:
        print('Desculpe, você não digitou seu sexo corretamente!')
        tmb = None

    # Calcular calorias diárias recomendadas
    if tmb:
        fatores = {
            'sedentario': 1.2,
            'sedentário': 1.2,
            'levemente ativo': 1.375,
            'moderadamente ativo': 1.55,
            'altamente ativo': 1.725,
            'extremamente ativo': 1.9
        }
        fator = fatores.get(nivel_de_exercicio)
        if fator:
            calorias = tmb * fator
            print(f'{nome}, para manter seu peso, consuma aproximadamente {calorias:.2f} calorias por dia.')
        else:
            print('Exercício não reconhecido. Use: sedentario, levemente ativo, moderadamente ativo, altamente ativo ou extremamente ativo.')

# HOMEM RETORNA:
"""
Digite seu nome: Gabriel
Digite sua idade: 35
Digite sua altura: 170
Digite seu peso: 79
Digite seu sexo: masculino
Digite seu nível de exercicio: sedentario
Gabriel, sua taxa metabólica basal é: 1767.01
Gabriel, para manter seu peso, consuma aproximadamente 2120.52 calorias por dia.
"""

# MULHER RETORNA:
"""
Digite seu nome: Isabela
Digite sua idade: 34
Digite sua altura: 165
Digite seu peso: 60
Digite seu sexo: feminino
Digite seu nível de exercicio: sedentario
Isabela, sua taxa metabólica basal é: 1226.62
Isabela, para manter seu peso, consuma aproximadamente 1471.95 calorias por dia.
"""
