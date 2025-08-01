real = float(input("Quanto você tem na carteira? "))
dolar = real / 3.27
print("Com R$ {:.0f} você pode comprar US${:.2f}".format(real, dolar))