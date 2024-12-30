class Cliente:
    def __init__(self, nm, fone):

        self.nome = nm
        self.telefone = fone

    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome
