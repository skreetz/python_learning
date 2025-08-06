# quantos numeros negativos e positivos

positivos = 0
negativos = 0

for i in range(10):
    numero = int(input("Digite um número: "))
    if numero >= 0:
        positivos += 1
    else:
        negativos += 1
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")
