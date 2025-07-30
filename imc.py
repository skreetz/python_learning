peso = int(input("Digite o seu peso em kg: "))
altura = input("Digite a sua altura em centímetros: ")

peso = float(peso)
altura = float(altura)

imc = peso / altura**2
print("Seu IMC é:" + str(imc))