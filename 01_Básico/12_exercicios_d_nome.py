"""
-> Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4
    letras ou menos, escreva "seu nome é curto"; se tiver entre 5 e 6 letras,
    escreva "seu nome é normal"; maior que 6 escreva "Seu nome é grande"
"""


nome = input("\nDigite um nome: ")

if len(nome) > 0 and len(nome) <= 4:
    print("\nSeu nome é curto.\n")
elif len(nome) > 4 and len(nome) <= 6:
    print("\nSeu nome é normal\n")
elif len(nome) > 6:
    print("\nSeu nome é grande.\n")
else:
    print("\nErro. Digite um nome válido.\n")
