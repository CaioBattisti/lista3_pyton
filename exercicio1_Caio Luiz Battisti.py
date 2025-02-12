#peça dois numeros.Se o primeiro numero for maior que o que o segundo,exiba primeiro o segundo numero e depois o primeiro,caso contrario,mostre o primeiro numero e depois o segundo.
num1 =int(input("digite um numero:"))
num2 =int(input("digite outro numero:"))
if num1 > num2:
    print(num2)
    print(num1)
else:
    print(num1)
    print(num2)