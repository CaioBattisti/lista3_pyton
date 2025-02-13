#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.
renda = input("digite sua renda: ")
if renda <= 2259.20:
    print("sem desconto de renda.")
if renda > 2259.20 and renda <= 2826.65:
    float("foi descontado",renda *0.075)
