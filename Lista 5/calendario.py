def dias_mes(mes,ano):
    if mes>12:
        return None
    elif mes==2 and (ano%4==0 and (not ano%100==0 or ano%400==0)):
        dia = 28
    elif mes==2:
        dia = 29
    elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
        dia = 31
    else:
        dia = 30

    return(dia)