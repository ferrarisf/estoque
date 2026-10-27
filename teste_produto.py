from produto import Produto

p1 = Produto()
p1.nome = "Luva de vaqueta"
p1.quantidade = 12
p1.codigo = 546367834
p1.preco = 20.99
p1.tipo = "Luva"

p2 = Produto()
p2.nome = "óculos"
p2.quantidade = 25
p2.codigo = 55765685
p2.preco = 29.99
p2.tipo = "De Sol"

print(p1.listar_produtos())
print(p2.listar_produtos())

p1.entrada(30)
print(p1.listar_produtos())

p1.saida(15)
print(p1.listar_produtos())

if p1.saida(100):
    print("saida registrada")
else:
    print("saida recusada")

    print(p1.quantidade)
