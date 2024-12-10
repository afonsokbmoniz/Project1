from classes_intro_blueprints import Pessoa 
from classes_intro_blueprints import Carro 
from classes_intro_blueprints import Compra

#Atribuição de valores
pessoa = Pessoa("Afonso", 19) 
carro = Carro("Lexus", "570" , "Japonesa") 
preco = Compra("80.000$")

#Faz o print da informação da função saudação dntro da class pessoa
print(pessoa.saudacao())    
#Faz o print da informação da class carro
print(carro.informacao_do_carro()) 
print(preco.mostra())