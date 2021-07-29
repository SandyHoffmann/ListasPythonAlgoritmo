
def soma(num, num_ant = 0,somar=0):
    num = input("Me diga um num: ")
    if num != "":
        num2 = int(num) + int(somar)
        num_ant = num
        som = soma(num2,num_ant,num2)
        print(f'{num} + {num_ant} + {somar}')
        return som
    else:
        return somar    

def main():
    print(soma(0,0,0))



if __name__ == "__main__":
    main()
