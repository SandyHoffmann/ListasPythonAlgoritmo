
def decBinIte(q,result = ""):
    while q!=0:
        r = q%2
        result = str(r) + result
        q = q//2
    return (result)

def main():

    print(decBinIte(5))

if __name__ == "__main__":
    main()
