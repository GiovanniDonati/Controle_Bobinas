from datetime import datetime

class Bobina:
    def __init__(self, endereco: str, codigo: str, descricao: str, lote: str, metragem: float, data_entrada: datetime):
        self.__endereco = endereco
        self.__codigo = codigo
        self.__descricao = descricao
        self.__lote = lote
        self.__metragem = metragem
        self.__data_entrada = data_entrada

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco

    @property
    def codigo(self):
        return self.__codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def lote(self):
        return self.__lote

    @property
    def metragem(self):
        return self.__metragem

    @metragem.setter
    def metragem(self, metragem: float):
        self.__metragem = metragem

    @property
    def data_entrada(self):
        return self.__data_entrada