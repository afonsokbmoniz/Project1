class Pessoa:
    def __init__(self, nome, idade): 
        self.nome = nome
        self.idade = idade

#função saudacao serve para apresentar informações...
    def saudacao(self):
        return f"O meu nome é {self.nome} e tenho {self.idade} anos." 

#A class carro contém as iinformações sobre a variável carro
class Carro:
    def __init__(self, marca, modelo, origem):  
        self.marca = marca
        self.modelo = modelo
        self.origem = origem
        #informacao_do_carro é uma função defenida para fazer a apresentação da variável 
    def informacao_do_carro(self):
            return f"Este é um {self.marca} {self.modelo} de origem {self.origem}" 
class Compra:
     def __init__(self, preco): 
        self.preco = preco

        def mostra(self):
             return f"O preço deste carro corresponde à {self.preco}"
       