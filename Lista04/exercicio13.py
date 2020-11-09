def FizzBuzz(n1):
    for x in range(1,n1+1):
        if (x % 3 == 0) and (x % 5 == 0):
            print(f"FizzBuzz: {x}")
        elif (x % 3 == 0):
            print(f"Fizz: {x}")
        elif (x % 5 == 0):
            print(f"Buzz: {x}")
        else:
            print (f"Ignorado: {x}")

def main():
    n1 = 0
    n1 = int(input("Insira um número : "))
    FizzBuzz(n1)

if __name__ == "__main__":
    main()



