def tabuada(numero):
    print(f"\nTabuada do {numero}:")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado}")
    print("-" * 20)

def main():
    try:
        numero = int(input("Digite um número: "))
        tabuada(numero)
    except ValueError:
        print("Por favor, digite um número válido.")

if __name__ == "__main__":
    main()
