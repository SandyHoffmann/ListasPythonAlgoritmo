import calendario

def is_magica(dia,mes,ano):
    anototal = ano - 1900
    if dia*mes == anototal:
        print (f'{dia}, {mes}, {ano}')
def main():
    for x in range(1,101):
        ano = 1900 + x
        for y in range(1,13):
            dias = calendario.dias_mes(y,ano)
            for x in range(1, dias+1):
                is_magica(x,y,ano)

if __name__ == "__main__":
    main()