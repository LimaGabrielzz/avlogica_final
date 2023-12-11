#Peça o numero do usuario
num = int(input("Digite seu numero: "))

#Use os dois primeiros digitos do numero
num = int(str(num)[:2])
#Compare os dois primeiros numeros
if num == 61:
    print("seu DDD é de Brasilia")
elif num == 71:
    print("seu DDD é de Salvador")
elif num == 11:
    print("seu DDD é de São Paulo")
elif num == 21:
    print("seu DDD é do Rio de Janeiro")
elif num == 32:
    print("seu DDD é de Juiz de Fora")
elif num == 19:
    print("seu DDD é de Campinas")
elif num == 27:
    print("seu DDD é de Vitória")
elif num == 31:
    print("seu DDD é de Belo Horizonte")
else:
    print("seu DDD não foi encontrado")