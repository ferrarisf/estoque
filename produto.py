class Produto: 
    def __init__(self, codigo=None, nome=None, quantidade=0, preco=0.0, tipo=None):

        self.codigo = codigo
        self.nome = nome 
        self.quantidade = quantidade
        self.preco = preco
        self.tipo = tipo

    def listar_produtos(self):
        return{
            "codigo": self.codigo,
            "nome": self.nome,
            "quantidade": self.quantidade,
            "preco": self.preco,
            "tipo": self.tipo,
            "situacao": self.situacao(),
        }

    def situacao(self):
        if self.quantidade == 0:
            return "Em falta"
        elif self.quantidade <= 1:
            return "Repor"
        else:
            return "OK"

    def entrada(self, qtd):
        self.quantidade = (self.quantidade + qtd)

    def saida(self, qtd):
        if qtd <= self.quantidade:
            self.quantidade = (self.quantidade - qtd)
            return True
        return False

        