from datetime import datetime

class Movimentacao:
    def __init__(self, bobina, tipo, data, endereco):
        self.__bobina = bobina
        self.__tipo = tipo
        self.__data = data
        self.__endereco = endereco

    @property
    def bobina(self):
        return self.__bobina

    @property
    def tipo(self):
        return self.__tipo

    @property
    def data(self):
        return self.__data

    @property
    def endereco(self):
        return self.__endereco