def fatorial(n, resultado=1):
    
    if n == 0 or n == 1:  
        return resultado
    else: 
        return fatorial(n - 1, n * resultado)


def main():
    n = int(input("Digite um número inteiro: "))
    resultado = fatorial(n)
    print(20 * "#")
    print("Fatorial:", resultado)
    print(20 * "#")


if __name__ == "__main__":
    main()
