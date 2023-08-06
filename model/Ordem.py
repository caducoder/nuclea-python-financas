
class Ordem:

    def __init__(self):
        self.__nome = None
        self.__ticket = None
        self.__valor_compra = None
        self.__quantidade_compra = None
        self.__data_compra = None
        self.__cliente_id = None


    def set_nome(self, nome: str):
        self.__nome = nome


    def get_nome(self):
        return self.__nome
    

    def set_ticket(self, ticket: str):
        self.__ticket = ticket


    def get_ticket(self):
        return self.__ticket
    

    def set_valor_compra(self, valor_compra: float):
        self.__valor_compra = valor_compra


    def get_valor_compra(self):
        return self.__valor_compra
    

    def set_quantidade_compra(self, quantidade_compra: int):
        self.__quantidade_compra = quantidade_compra


    def get_quantidade_compra(self):
        return self.__quantidade_compra
    

    def set_data_compra(self, data_compra: str):
        self.__data_compra = data_compra


    def get_data_compra(self):
        return self.__data_compra
    

    def set_cliente_id(self, cliente_id: int):
        self.__cliente_id = cliente_id


    def get_cliente_id(self):
        return self.__cliente_id
    