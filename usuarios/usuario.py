# usuario.py — a classe Usuario: quem é a pessoa e o que ela pode fazer
# A senha nunca fica guardada como foi digitada: guardamos só o resumo (hash).
 
import hashlib
import secrets
 
from usuarios.papeis import PERMISSOES
class Usuario:
    # Construtor: matrícula, nome, senha e a lista de papéis
    def __init__(self, matricula, nome, senha, papeis, supervisor=None):
        self.matricula = matricula
        self.nome = nome
        self.papeis = papeis               # ex.: ["solicitante", "supervisor"]
        self.supervisor = supervisor       # matrícula de quem aprova os pedidos dele
        self.situacao = "ativo"            # pendente, ativo, recusado ou inativo
        # O _ na frente avisa: atributo interno, ninguém de fora mexe
        self._sal = secrets.token_hex(8)
        self._senha_hash = self._resumir(senha)
 
    # Transforma a senha em um resumo que não dá para desfazer
    def _resumir(self, senha):
        texto = (self._sal + senha).encode("utf-8")
        return hashlib.sha256(texto).hexdigest()
 
    # True se a senha digitada bate com a guardada
    def conferir_senha(self, senha):
        return self._resumir(senha) == self._senha_hash