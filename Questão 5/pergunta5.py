# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

entrada = input("Digite uma palavra: ")

# Inverte a string usando fatiamento e exibe o resultado
print(f"Sua palavra invertida fica: {entrada[::-1]}")