altura = float(input("Digite uma quantidade em metros"))
largura = float(input("Digite outra quantidade em metros"))
área = altura*largura
tinta = área/2
print("Sua parede tem a dimensão de {:.0f}x{:.0f} e sua área mede {:.0f}m².".format(altura,largura,área))
print("Será necessária {:.0f} litros de tinta para pintar a parede.".format(tinta))
