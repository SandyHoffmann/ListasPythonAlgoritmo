def validar_senha(senha):
    pontoupp = 0
    pontolower = 0
    pontonumb = 0
    if len(senha)>7:
        if (not senha.isdigit()):
            for letra in senha:
                if letra == letra.lower() and not letra.isdigit():
                    pontoupp+=1
                if letra == letra.upper() and not letra.isdigit():
                    pontolower+=1
                if letra.isdigit():
                    pontonumb+=1
        
    if (pontonumb>0) and (pontolower>0) and (pontoupp>0):
        return True
    else:
        return False
def main():
    senha = input("Me diga a senha: ")
    validar = validar_senha(senha)
    if validar == True:
        print(f'{validar_senha(senha)} : {senha} é valida! ')
    else:
        print(f'{validar_senha(senha)} : {senha} NÃO é valida! ')

if __name__ == "__main__":
    main()