def decBinRec(q,result = ""):
    if q != 0:
        r = q%2
        result = str(r) + result
        q = q//2
        return decBinRec(q,result)
    if q == 0:
        return (result)

def main():

    print(decBinRec(4))

if __name__ == "__main__":
    main()