peso = int(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

peso = float(peso)
altura = float(altura)

imc = peso / altura**2
print("Seu IMC é {:.0f}".format(imc))