# tpessoa = "Lucas, 21, 1.80"
# print(tpessoa)

# pessoa = ("Ana", 25, 1.65)
# print(f"A {pessoa[0]} tem {pessoa[1]} anos e mede {pessoa[2]}m")

dados = input("Digite seu nome, idade e altura separados por vírgula: ")
tupla = nome, idade, altura = dados.split(",")
print(tupla)
