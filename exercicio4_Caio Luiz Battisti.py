#Peça ao usuário para inserir sua cor favorita. Se ele digitar "vermelho", "VERMELHO" ou "Vermelho" exibem a mensagem "Eu também gosto de vermelho"
#caso contrário, exibem a mensagem "Eu não gosto de [cor], eu prefiro vermelho".
cor =input("digite sua cor favorita: ")
if cor == ("Vermelho"):
    print("eu tambem gosto de Vermelho")
elif cor == ("vermelho"):
    print("eu tambem gosto de vermelho")
elif cor == ("VERMELHO"):
    print("eu tambem gosto de VERMELHO")
else:
    print("eu nao gosto do ",cor," eu prefiro vermelho")