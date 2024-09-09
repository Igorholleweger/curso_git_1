# Função para somar os números de uma lista
def soma_lista(lista):
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Testando a função
numeros = [2, 5, 8, 12]
resultado = soma_lista(numeros)

# Exibindo o resultado
print(f"A soma dos números {numeros} é: {resultado}")
