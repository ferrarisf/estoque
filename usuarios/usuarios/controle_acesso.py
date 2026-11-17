


class ControleAcesso:

   
    def __init__(self):
        self.usuarios = []
        self.sessoes = {}  

    # Devolve o Usuario com essa matrícula, ou None
    def buscar(self, matricula):
        for u in self.usuarios:
            if u.matricula == matricula:
                return u

        return None

    # Guarda um usuário novo; False se a matrícula já existe
    def cadastrar(self, usuario):
        achado = self.buscar(usuario.matricula)

        if achado is not None:
            return False

        self.usuarios.append(usuario)
        return True

    # Faz o login e devolve um token se as credenciais forem válidas
    def entrar(self, matricula, senha):
        usuario = self.buscar(matricula)

       
        if usuario is None:
            return None

        if usuario.situacao != "ativo":
            return None

        if not usuario.conferir_senha(senha):
            return None

        # Cria um token de acesso
        token = secrets.token_hex(16)

        # Guarda o token relacionado à matrícula
        self.sessoes[token] = matricula

        return token

    # Procura o usuário associado ao token
    def usuario_logado(self, token):
        # Verifica se o token existe
        if token not in self.sessoes:
            return None

        # Recupera a matrícula associada ao token
        matricula = self.sessoes[token]

        # Busca e retorna o usuário
        return self.buscar(matricula)

    # Encerra uma sessão
    def sair(self, token):
        # Verifica se o token existe
        if token not in self.sessoes:
            return False

        # Remove o token da sessão
        del self.sessoes[token]

        return True

    # Altera os papéis de um usuário
    def mudar_papeis(self, quem, matricula, papeis):

        # Verifica se quem está alterando tem permissão
        if not quem.pode("mudar_papeis"):
            return "Você não tem permissão para mudar papéis."

        # Procura o usuário pela matrícula
        usuario = self.buscar(matricula)

        if usuario is None:
            return "Usuário não encontrado."

        # Verifica se a lista de papéis está vazia
        if not papeis:
            return "Escolha pelo menos um papel."

        # Verifica se todos os papéis são válidos
        for papel in papeis:
            if papel not in papeis_validos():
                return "Papel inválido: " + papel

        # Atualiza os papéis do usuário
        usuario.papeis = papeis