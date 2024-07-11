# escreva um produto em python que solicite varios numeros para o usuario, um de cada vez, possibilitando encerrar a entrada de dados ao informar "sair"

# *Armanaze os numeros em uma lista
# percorra essa lista alimentando outras listas, uma com numero pares e um amigo impares
# ordene e imprima os numeros pares e impares separadament, mas em ordem crescente
# *some os valores de cada lista e imprima o resultado

numeros = []
mensagem = input("Digite um número ou 'sair' para encerrar): ")
while mensagem.lower() != 'sair':
    try:
        numero = int(mensagem)
        numeros.append(numero)
    except ValueError:
        print(" Inválido. Digite um número válido ou 'sair'.")
    entrada = input("Digite um número ou 'sair' para encerrar):")

numerospares = sorted([num for num in numeros if num % 2 == 0])
numerosimpares = sorted([num for num in numeros if num % 2 != 0])

print("Números pares em ordem crescente:", numerospares)
print("Números ímpares em ordem crescente:", numerosimpares)

somapares = sum(numerospares)
somaimpares = sum(numerosimpares)
print("Soma dos números pares:", somapares)
print("Soma dos números ímpares:", somaimpares)