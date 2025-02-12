#Pergunte ao usuário se está chovendo e converta sua resposta em minúsculas para que não importe em que caso ele digite.
#Se ele responder "sim", pergunte se está ventando. Se ele responder "sim" a esta segunda pergunta, exiba a resposta "Está ventando muito para um guarda-chuva"
#caso contrário, exiba a mensagem "Pegue um guarda-chuva".
#Se ele não respondera sim à primeira pergunta, mostre a resposta "Aproveite o seu dia".
clima = input("Esta chovendo ai?")
if clima == ("nao"):
    print("Aproveite seu dia")
if clima == ("sim"):
    clima2 = input("Esta ventando muito?")
elif clima == ("nao"):
    print("Leve um guarda-chuva")
else:
    print("Esta ventando muito para um guarda-chuva")