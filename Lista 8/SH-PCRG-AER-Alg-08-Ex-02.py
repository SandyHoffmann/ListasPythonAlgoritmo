def fibonacci(n):
    if n == 1:
        return (0)
    if n == 2:
        return (1)
    else:
        n = (fibonacci(n-1)+fibonacci(n-2))
        return n

def main():
    n = int(input("Fibonnacci até que numero? "))
    for x in range(1,n+1):
        print(fibonacci(x))


if __name__ == "__main__":
    main()
