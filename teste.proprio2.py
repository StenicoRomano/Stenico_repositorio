"""
EXERCÍCIO TESTE PRÓPRIO 2 -> EXAME MÉDICO
"""
"""
PASSO 1
Digite seu nome {nome}
Digite sua idade {idade}
Digite seu sexo {sexo}

PASSO 2
Se for sexo1 MASCULINO ser encaminhado para corredor AMARELO {corredor_amarelo}
Se for sexo2 FEMININO ser encaminhado para corredor VERDE {corredor_verde}
Se não digitar sexo, ser atendido por uma enfermeira {enfermeira}

PASSO 3
Se for menor de 18 anos {idadde} <= 18 ser atendido na senha infantil {senha_infantil}
Se tiver {idade} 18 <= 64 ser atendido na senha padrão {senha_padrao
Se tiver {idade} 65 >= ser atendido na senha preferencial {senha_preferencial}

"""

# Passo 1
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
sexo = input("Digite seu sexo: ")

# Conversão e validação da idade
try:
    idade = float(idade)
except:
    print("Procure por uma enfermeira.")
    exit(1)

# Passo 2
if 1 <= float(idade) < 18:
    print("Senha de atendimento infantil")
elif 18 <= float(idade) < 64:
    print("Senha de atendimento padrão")
elif float(idade) >= 65:
    print("Senha de atendimento preferencial")

# Passo 3
if sexo == "masculino" or sexo == "Masculino" or sexo == "MASCULINO":
    print("Dirija-se ao corredor AMARELO")
elif sexo == "feminino" or sexo == "Feminino" or sexo == "FEMININO":
    print("Dirija-se ao corredor VERDE")
else:
    print("Dirija-se ao atendimento da enfermagem")

"""
DIGITANDO AS INFORMAÇÕES PEDIDAS (MASC):
Digite seu nome: Gabriel
Digite sua idade: 35
Digite seu sexo: masculino
Dirija-se ao corredor AMARELO
Senha de atendimento padrão 

DIGITANDO AS INFORMAÇÕES PEDIDAS (FEM):
Digite seu nome: Isabela
Digite sua idade: 34
Digite seu sexo: feminino
Dirija-se ao corredor VERDE
Senha de atendimento padrão

DIGITANDO AS INFORMAÇÕES PEDIDAS INFANTIL:
Digite seu nome: Murillo
Digite sua idade: 6
Digite seu sexo: Masculino
Dirija-se ao corredor AMARELO
Senha de atendimento infantil

DIGITANDO AS INFORMAÇÕES PEDIDAS PREFERENCIAL:
Digite seu nome: Manoel
Digite sua idade: 82
Digite seu sexo: masculino
Dirija-se ao corredor AMARELO
Senha de atendimento preferencial

NÃO DIGITANDO AS INFORMAÇÕES PEDIDAS:
Digite seu nome: 
Digite sua idade: 
Digite seu sexo: 
Procure por uma enfermeira.
"""

