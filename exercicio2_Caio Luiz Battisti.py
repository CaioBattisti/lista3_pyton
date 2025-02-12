#Peça ao usuário para inserir um número inferior a 20. Se ele inserir um número 20 ou mais, exiba a mensagem "Muito alto", caso contrário, exiba "Obrigado".
num1 =int(input("insira um numero menor que 20:"))
if num1 < 20:
    print("Obrigado")
else:
    print("Muito alto")