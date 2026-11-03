
class Almoxarifado:

    # Inicializa o almoxarifado
    def __init__(self, unidade):
        self.unidade = unidade
        self.produtos = []

    # Adiciona um produto ao almoxarifado
    def adicionar(self, produto):
        self.produtos.append(produto)

    # Conta quantos produtos estão em falta
    def contar_em_falta(self):
        total = 0
        for p in self.produtos:
            if p.situacao() == "Em falta":
                total = total + 1
        return total

    # Procura um produto pelo código
    def buscar(self, codigo):
        for p in self.produtos:
            if p.codigo == codigo:
                return p
        return None

    # Registra a entrada de produtos
    def entrada(self, codigo, qtd):
        p = self.buscar(codigo)
        if p is None:
            return False
        p.entrada(qtd)
        return True

    # Registra a saída de produtos
    def saida(self, codigo, qtd):
        p = self.buscar(codigo)
        if p is None:
            return False
        return p.saida(qtd)

    # Lista todos os produtos
    def listar(self):
        lista = []
        for p in self.produtos:
            lista.append(p.listar_produtos())
        return lista

    # Cria a solicitação de compra
    def solicitacao_compra(self):
        pedido = []
        for p in self.produtos:
            if p.situacao() != "OK":
                pedido.append({
                    "codigo": p.codigo,
                    "nome": p.nome,
                    "situacao": p.situacao()
                })
        return pedido

    # Calcula o valor total do estoque
    def valor_estoque(self):
        total = 0
        for p in self.produtos:
            total = total + (p.quantidade * p.preco)
        return total

    # Devolve um resumo do almoxarifado
    def para_dicionario(self):
        return {
            "unidade": self.unidade,
            "total_produtos": len(self.produtos),
            "produtos": self.listar()
        }





     

