def calculadora(valor_um,valor_dois,operador):
    if operador == "+":
        resultado = valor_um + valor_dois
        return resultado
    elif operador == "-":
        resultado = valor_um - valor_dois
        return resultado
    elif operador == "*":
        resultado = valor_um * valor_dois
        return resultado
    elif operador == "/":
        if valor_dois == 0:
            print("Não é possivel fazer a divisão por zero.")
        else:
            resultado = valor_um / valor_dois
            return resultado
    else:
        resultado = "Operação inválida"
        return resultado
    

numero_um = int(input("Digite o primeiro valor: "))
op = input("Escolha a opção: (+,-,*,/)")
numero_dois = int(input("Digite o segundo Valor: "))

print(calculadora(numero_um,numero_dois,op))