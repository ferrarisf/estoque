# Status da solicitação
AGUARDANDO = "aguardando_aprovacao"
REPROVADO = "sem_aprovacao_gestor"
SOLICITADO = "solicitado"
RECEBIDO = "recebido"
ENTREGUE = "entregue"
CANCELADO = "cancelado"

# Ordem das etapas da compra
ANDAMENTO = [SOLICITADO, RECEBIDO, ENTREGUE]
ENCERRADOS = [ENTREGUE, CANCELADO]

class SolicitacaoCompra:

    def __init__(self, numero, unidade, solicitante, supervisor):
        self.numero = numero
        self.unidade = unidade
        self.solicitante = solicitante
        self.supervisor = supervisor
        self.itens = []
        self.status = AGUARDANDO
        self.historico = []

        self._registrar(solicitante, "Solicitação aberta")

    # Registra as alterações no histórico
    def _registrar(self, quem, nota):
        self.historico.append({
            "status": self.status,
            "quem": quem,
            "nota": nota
        })
        # Adiciona itens enquanto o pedido aguarda aprovação
    def adicionar_item(self, codigo, nome, quantidade):
        if self.status != AGUARDANDO:
            return "Depois de aprovada, a solicitação não recebe itens novos."

        if quantidade <= 0:
            return "A quantidade precisa ser maior que zero."

        self.itens.append({
            "codigo": codigo,
            "nome": nome,
            "quantidade": quantidade
        })

        return None
        # Aprova somente se for o supervisor responsável pelo pedido
    def aprovar(self, usuario):
        if not usuario.pode("aprovar_pedido") or usuario.matricula != self.supervisor:
            return "Só o supervisor desta solicitação pode aprová-la."

        if self.status != AGUARDANDO:
            return "Só dá para aprovar o que está aguardando aprovação."

        if len(self.itens) == 0:
            return "A solicitação não tem itens."

        self.status = SOLICITADO
        self._registrar(usuario.matricula, "Aprovada")

        return None
        # Reprova a solicitação pelo supervisor responsável
    def reprovar(self, usuario, motivo):
        if not usuario.pode("aprovar_pedido") or usuario.matricula != self.supervisor:
            return "Só o supervisor desta solicitação pode reprová-la."

        if self.status != AGUARDANDO:
            return "Só dá para reprovar o que está aguardando aprovação."

        if motivo.strip() == "":
            return "Informe o motivo da reprovação."

        self.status = REPROVADO
        self._registrar(usuario.matricula, motivo)

        return None
        # Avança a solicitação para a próxima etapa
    def avancar(self, usuario):
        if not usuario.pode("andamento_pedido"):
            return "Só o almoxarifado mexe no andamento da compra."

        if self.status not in ANDAMENTO or self.status == ENTREGUE:
            return "Esta solicitação não está em andamento."

        posicao = ANDAMENTO.index(self.status)
        self.status = ANDAMENTO[posicao + 1]

        self._registrar(usuario.matricula, "Etapa concluída")

        return None