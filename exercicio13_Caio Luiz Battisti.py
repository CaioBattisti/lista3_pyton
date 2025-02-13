#Escreva um programa que leia dois números e que pergunte qual operação você deseja subtração (-)
#multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada. 
#(usar ELIF)
num1 = int(input("digite um numero:"))
num2 = int(input("digite outro numero:"))
escolha = input("vc deseja fazer qual operação?")
if escolha == ("+"):
    print("a soma e:",num1 + num2)
elif escolha == ("-"):
    print("a subtração e:",num1 - num2)
elif escolha == ("*"):
    print("a multiplicação e:",num1 * num2)
elif escolha == ("/"):
    print("sua divisao e:",num1 / num2)