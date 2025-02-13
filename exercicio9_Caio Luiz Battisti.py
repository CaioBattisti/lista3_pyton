#Escreva um programa que faça o cálculo do imposto de renda 2025. Consulte a tabela no site da Receita federal.

renda =int( input("digite sua renda: "))
if renda < 2259.20:
    print("sem desconto de renda.")

elif renda >= 2259.20 and renda <= 2826.65:
    imposto = renda * 0.075
    print("foi descontado 7,5%:",imposto,)

elif renda >= 2826.66 and renda <=3751.05:
    imposto = renda * 0.15
    print("foi descontado 15%:",imposto,)

elif renda >=  3751.06 and renda <= 4664.68:
    imposto = renda * 0.225
    print("foi descontado 22.5%:",imposto)

elif renda > 4664.68:
    imposto = renda * 0.275
    print("voce foi descontado 27.5%:",imposto,)