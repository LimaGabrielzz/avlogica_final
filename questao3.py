#armazene uma senha
senha = 2000
a = int(input("digite uma senha: "))

#verifique se a senha que o usuario digitou é "2000"
while a != senha:
    print("senha incorreta")
    a = int(input("digite uma senha: "))

#se a senha digitada for "2000" está correta e será usado 'PRINT' para a saida de
#'ACESSO PERMITIDO'
print("acesso permitido")