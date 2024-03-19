from Factory import factory

class Pessoa:
    def __init__(self, nome:str, cpf:str, email:str):
        self.__Nome:str = nome
        self.__Cpf:str = cpf
        self.__Email:str = email
        self.__Endereco:str = ""
    
    def setEndereco(self, endereco:str):
        self.__Endereco = endereco

    def __str__(self) -> str:
        return f"{self.__Nome} {self.__Email} {self.__Endereco}"