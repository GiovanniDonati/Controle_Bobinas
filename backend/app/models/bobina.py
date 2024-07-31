from datetime import datetime

class Bobina:
    def __init__(self, endereco, codigo, descricao, lote, metragem, data_entrada):
        self.endereco = endereco
        self.codigo = codigo
        self.descricao = descricao
        self.lote = lote
        self.metragem = metragem
        self.data_entrada = data_entrada

    def alterar_informacoes(self, endereco=None, descricao=None, metragem=None):
        if endereco:
            self.endereco = endereco
        if descricao:
            self.descricao = descricao
        if metragem:
            self.metragem = metragem
