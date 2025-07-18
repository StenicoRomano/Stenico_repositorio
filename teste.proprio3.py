# CALCULANDO TAXXA METABÓLICA BASAL
"""
TMB HOMENS = 66,5 + (13,75 x peso em kg) + (5,003 x altura em cm) - (6,75 x idade) 
TMB MULHERES = 655,1 + (9,563 x peso em kg) + (1,850 x altura em cm) - (4,676 x idade) 
"""

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
altura = input('Digite sua altura: ')
peso = input('Digite seu peso: ')
sexo = input('Digite seu sexo: ')

if nome and idade and altura and peso and sexo:
    altura = float(altura)
    peso = float(peso)
    idade = float(idade)

    
    if sexo == 'masculino' and "Masculino" and "MASCULINO": # Verifica se o sexo é masculino
        tmb = 66.5 + (13.75 * peso) + (5.003 * altura) - (6.75 * idade)
        print(f'{nome}, sua taxa metabólica basal é: {tmb:.2f}')
    elif sexo == 'feminino' and "Feminino" and "FEMININO": # Verifica se o sexo é feminino
        tmb = 655.1 + (9.563 * peso) + (1.850 * altura) - (4.676 * idade)
        print(f'{nome}, sua taxa metabólica basal é: {tmb:.2f}')
    else:
        print('Desculpe, você não digitou seu sexo corretamente!')

# RETORNA MASCULINO:
"""
Digite seu nome: Gabriel
Digite sua idade: 35
Digite sua altura: 170
Digite seu peso: 79
Digite seu sexo: masculino
Gabriel, sua taxa metabólica basal é: 1767.01   
"""
# RETORNA FEMININO:
"""
Digite seu nome: Isabela
Digite sua idade: 34
Digite sua altura: 165
Digite seu peso: 60
Digite seu sexo: feminino
Isabela, sua taxa metabólica basal é: 1226.62
"""
