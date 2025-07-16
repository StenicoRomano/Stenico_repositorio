# EERCÍCIO
"""
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Peça ao usuário para digitar sua altura em metros
Peça ao usuário para digitar seu peso em kg
Fórmula IMC: IMC = peso / (altura x altura)
Se o nome, idade, altura e peso forem digitados:
   Exiba:
   Seu nome é {nome}
   Sua idade é {idade}
   Sua altura é {altura}
   Seu peso é {peso}
   Seu IMC é {imc}
   Você é um indivíduo saudável ou não saudável.
Se o IMC for menor que 18.5, exiba: "Você está abaixo do peso."
Se o IMC estiver entre 18.5 e 24.9, exiba: "Você está com peso normal."
Se o IMC estiver entre 25 e 29.9, exiba: "Você está com sobrepeso."
Se o IMC for maior que 30, exiba: "Você está obeso."
Seu peso ideal é: {altura - 100 - [(altura - 150)/4]}
Seu IMC ideal é: {80 / (1.80 * 1.80)}
Se nada for digitado em nome e idade:
   Exiba: 'Desculpe, você deixou campos vazios.'
   """
nome = input("Digite seu nome: ") # Qualquer nome
idade = input("Digite sua idade: ") # Qualquer idade
altura = input("Digite sua altura: ") # Qualquer altura
peso = input("Digite seu peso: ") # Qualquer peso

if nome and idade and altura and peso:
    altura = float(altura)
    peso = float(peso)
    imc = (peso / (altura * altura))
    peso_ideal = altura - 100 - ((altura - 150)/4)
    imc_ideal = peso_ideal / (altura * altura)
    

    print("Seu nome é: ", nome)
    print("Sua idade é: ", idade)
    print("Sua altura é: ", altura)
    print(f'Seu peso é: {peso:.2f}')
    print('Seu IMC é: ', imc)
    print(f'Seu peso ideal é: {peso_ideal:.2f}')
    print('Seu IMC ideal é: ',imc_ideal)

    if imc <= 0.00185:
        print("Você está abaixo do peso.")
    elif imc >= 0.00185 and imc <= 0.00249:
        print("Você está com peso normal.")
    elif imc >= 0.0025 and imc <= 0.00299:
        print('Você está com sorepeso.')
    elif imc >= 0.003:
        print("Você está obeso(a).")
else:
    print("Desculpe, você deixou campos vaios!")

"""
DIGITANDO AS INFORMAÇÕES PEDIDAS:
Seu nome é:  Gariel
Sua idade é:  35   
Sua altura é:  170.0
Seu peso é:  79.0
Seu IMC é:  0.0027335640138408304
Seu peso ideal é:  65.0
Seu IMC ideal é:  0.002249134948096886
Você está obeso(a).

SEM DIGITAR NADA E/OU APENAS ALGUMAS:
Digite seu nome: Gabriel
Digite sua idade: 35
Digite sua altura: 
Digite seu peso: 79
Desculpe, você deixou campos vaios!
"""