class Quarto:

    def __init__(self,numero,localizacao,ocupado):
        self.__numero=numero
        self.__localizacao=localizacao
        self.__ocupado=ocupado

    def atribuir_hospede():
        pass
    def desocupar():
        pass

class Hospede:

    def __init__(self,nome,quarto,conta):
        self.__nome =nome
        self.__quarto =quarto
        self.__conta =conta

    def fazer_check_in(quarto:Quarto):
        pass
    def fazer_check_out():
        pass
    def pagar_conta():  
        pass  
    def pedir_comida():
        pass

class Conta:

    def __init__(self):
        self.__itensconsumidos= []
    
    def adicionar_item(self,item):
        self.__itensconsumidos.append(item)

class ItemComida:

    def __init__(self,nome,preco):
        self.__nome=nome
        self.__preco=preco

class Chef:
    
    def __init__(self,nome):
        self.__nome=nome

    def preparar_pedido(nome):
        pass