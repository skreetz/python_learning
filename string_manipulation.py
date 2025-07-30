texto = "python no inicio"
print(texto.title())

mensagem = "Ola, mundo!"
print(len(mensagem))

frase = input("Digite uma frase: ")
frase_maiuscula = frase.upper()
print("Frase em maiúsculas:", frase_maiuscula)

frase_minuscula = frase.lower()
print("Frase em minúsculas:", frase_minuscula)

numero = int(input("Digite um número: "))
if numero > 0:
    print("O número é positivo.")