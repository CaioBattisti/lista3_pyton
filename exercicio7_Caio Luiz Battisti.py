#Peça ao usuário para inserir 1, 2 ou 3. Se ele inserir um 1, exiba a mensagem "Obrigado", se ele inserir um 2, exiba "Muito bem"
#se ele inserir um 3, exiba "Correto". Se ele inserir qualquer outra coisa, exiba "Mensagem de erro".
num1 =int(input("digite um numero:"))
if num1 == 1:
    print("Obrigado.")
elif num1 == 2:
    print("Muito Bem.")
elif num1 == 3:
    print("Correto")
else:
    print("Erro,tente de novo!!!")