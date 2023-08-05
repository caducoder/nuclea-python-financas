class Cliente:

    def __init_(self):
        self.__id = None
        self.__nome = None
        self.__cpf = None
        self.__rg = None
        self.__data_nasc = None
        self.__endereco = None
        self.__num_casa = None


    def set_id(self, id: int):
        self.__id = id


    def get_id(self):
        return self.__id
    
    
    def set_nome(self, nome: str):
        self.__nome = nome


    def get_nome(self):
        return self.__nome
    

    def set_cpf(self, cpf: str):
        self.__cpf = cpf


    def get_cpf(self):
        return self.__cpf
    

    def set_rg(self, rg: str):
        self.__rg = rg


    def get_rg(self):
        return self.__rg
    

    def set_data_nasc(self, data_nasc: str):
        self.__data_nasc = data_nasc


    def get_data_nasc(self):
        return self.__data_nasc
    

    def set_endereco(self, endereco: dict):
        self.__endereco = endereco


    def get_endereco(self):
        return self.__endereco
    

    def set_num_casa(self, num_casa: int):
        self.__num_casa = num_casa


    def get_num_casa(self):
        return self.__num_casa