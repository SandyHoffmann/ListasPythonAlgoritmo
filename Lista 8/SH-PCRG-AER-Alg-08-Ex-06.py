
def mdc(a,b):
    if b  == 0:
        return a
    else: 
        c = a%b
        return(mdc(b,c)) 

def main():
    a = int(input("Me diga um num: "))
    b = int(input("Me diga um num: "))

    print(mdc(a,b))

if __name__ == "__main__":
    main()
