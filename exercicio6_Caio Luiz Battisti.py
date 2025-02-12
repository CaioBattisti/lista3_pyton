#Pergunte a idade do usuário. Se tiver 16 anos ou mais, exiba a mensagem "Você pode votar"
#se tiver 18 anos, exiba a mensagem "Você pode aprender a dirigir"
#se tiver 14 anos, exiba a mensagem "Você pode comprar um bilhete de loteria"
#se tiver menos de 14 anos, exiba a mensagem "Você pode fazer doces ou travessuras".
idade =int(input("qual sua idade? "))
if idade == 18:
    print("Voce pode aprender a dirigir.")
if idade == 16:
    print("Voce pode votar.")
if idade == 14:
    print("Voce pode comprar um bilhete de loteria.")
if idade < 14:
    print("Voce pode fazer doces ou travessuras.")