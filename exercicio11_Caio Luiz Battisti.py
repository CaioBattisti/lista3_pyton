#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
#Calcule o preço da passagem,cobrando R$ 0,50 por km para viagens de até de 200 km
#e R$ 0,45 para viagens mais longas.
distancia =int(input("quantos km vc deseja percorrer?"))
if distancia == 200:
    print("o preço ficou:",(distancia * 0.50))
elif distancia > 200:
    print("o preço ficou:",(distancia - 200) * 0.45)