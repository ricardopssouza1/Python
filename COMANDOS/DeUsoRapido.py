#Variáveis
>>> a, b = 10, 20
>>> a
10
>>> b
20

print("Hello World")

#Valor nulo (null)
reais = None

#Saídas
	print("Welcome to Python!")
	ou
	string_1 = "Camelot"
	string_2 = "place"
	print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

#Entradas
	name  = input("What is your name?")
	quest = input("What is your quest?")
	color = input("What is your favorite color?")	
	print("Ah, so your name is %s, your quest is %s, " \
	"and your favorite color is %s." % (name, quest, color) )

#Indentação
	def spam():
		eggs = 12
		return eggs	
	print(spam())


#Blocos
	if/elif/else
	for/else
	while/else
	def
	try/except /finally/else
	class
	with	
	if n < 0: print('Valor inválido')
		
		
# Estrutura de decisão
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade > 16:
 print(f'{nome} pode comprar o jogo')
 
 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade > 16:
 print(f'{nome} pode comprar o jogo')
else:
 print(f'{nome} não pode comprar o jogo, possui {idade} anos') 
 
  
 
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 16:
 print(f'{nome} pode comprar o jogo')
else:
 print(f'{nome} não pode comprar o jogo, possui {idade} anos')
 
 
nome = input("Digite o nome do jogo: ")
codigo = int(input("Digite o código do jogo: "))

#Novos jogos
overwatch = []
dead_redenption = []
uncharted = []
god_of_war = []

if nome == 'overwatch':
    overwatch.append(codigo)
elif nome == 'dead redenption':
    dead_redenption.append(codigo)
elif nome == 'uncharted':
    uncharted.append(codigo)
elif nome == 'god of war':
    god_of_war.append(codigo)
else:
    print("Esse jogo não existe na loja") 		

		
#Comentários
	# comentário de linha. Em linha.
	""" Esse é de bloco mas está em uma linha só """
	# comentário de linha. Em bloco.
	"""
	comentários
	comentários
	comentários
	"""
	type("text")        # <class 'str'>
	type(1)             # <class 'int'>
	type(0.99)          # <class 'float'>


#Laços de repetição
	lista = ["p", "y", "t", "h", "o", "n"]
	for item in lista:
		print item
	"""
	p
	y
	t
	h
	o
	n
	"""	
	
# Exemplo um com while...	
	count = 0
	while count <= 5:
		print(count)
		count += 1
	# 0 1 2 3 4 5
	
# Exemplo dois com while	
vendidos = 0
parada = 1
while parada != 0:
   nome = input("Digite seu nome: ")
   idade = int(input("Digite sua idade: "))
   if idade >= 16:
       vendidos += 1
   else:
       print(f'{nome} não pode comprar o jogo, possui {idade} anos')
       parada = int(input("Para parar digite 0 para continuar 1: "))
print(f'Foram vendidos {vendidos} hoje!!')


# For
for i in range(0, 10):
   print(i)	
	
	
#Funções
def foo():
    return "retorno da função"

print(foo()) # "retorno da função"


#Imports
import math
print(math.sqrt(25))


#Datas
from datetime import datetime
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)

#Para imprimir a data no formato brasileiro:
print('%s/%s/%s' % (now.day, now.month, now.year))


#Imprimindo as horas:
print('%s:%s:%s' % (now.hour, now.minute, now.second))


#Listas (lists)
animals = ["pangolin", "cassowary", "sloth", "dog"];
animals[0]   # 'pangolin'
animals[1]   # 'cassowary'
animals[2]   # 'sloth'
animals[3]   # 'dog'



clientes = []
parada = 1
while parada != 0:
   nome = input("Digite seu nome: ")
   idade = int(input("Digite sua idade: "))
   if idade >= 16:
       clientes.append(nome)
   else:
       print(f'{nome} não pode comprar o jogo, possui {idade} anos')
       parada = int(input("Para parar digite 0 para continuar 1: "))
print(f'Foram vendidos {len(clientes)} hoje, para {clientes}!!')
   
   
   
clientes = [['Duda', 21], ["Joãozinho", 32], ['Carla', 23], ['José', 40]]
for cliente in clientes:
   print(f'Nome: {cliente[0]} \nIdade: {cliente[1]}')
 
print(f'Foram vendidos {len(clientes)} jogos') 



# Operações com lista
   
# .insert(pos,elemento), inserir o elemento na posição pos.
# .append() - semelhante ao insert()
# .pop() retira o último elemento da lista
# .pop(index) retira o elemento no index indicado. Lembre-se sempre que a numeração dos índices começa em zero.
# .sort() ordena os valores em ordem crescente ou alfabética, variando de acordo com o tipo de dados da lista
# .reverse() ou .sort(reverse=True) fazem o oposto do .sort() e ordenam a lista de forma decrescente.
# .count(elemento) mostra quantas vezes elemento aparece na lista.
	
 lista_frutas = ['morango', 'pessego', 'abacaxi', 'pêra', 'banana', 'maçã', 'abacate']

print(f'len(lista): {len(lista_frutas)}')
lista_frutas.append('pêra')
print(f'.append(elemento): {lista_frutas}')
print(f'.count(elemento): {lista_frutas.count("pêra")}')
lista_frutas.pop(2)
print(f'.pop(index): {lista_frutas}')
lista_frutas.pop()
print(f'.pop(): {lista_frutas}')
lista_frutas.sort()
print(f'.sort(): {lista_frutas}')
lista_frutas.reverse()
print(f'.reverse(): {lista_frutas}')
lista_frutas.sort(reverse=True)
print(f'.sort(reverse=True): {lista_frutas}')

lista_valores = [x for x in range(1, 10)]
print(f'list comprehension: {lista_valores}')
lista_teste = []
for i in range(1,10):
    lista_teste.append(i)
print(lista_teste)




# Dicionários
# Dicionário em Python funciona de maneira semelhante a um dicionário português, possui uma chave(palavra) e um valor atribuído a ela (significado)

# .keys() retorna todas as chaves do dicionário
# .values() retorna todos os valores.

informacao = {'nome': 'eduarda', 'idade': 21}

print(f'.keys(): {informacao.keys()}')
print(f'.valuers():{informacao.values()}')

informacao['altura'] = 1.60
print(f'adicionando valor: {informacao}')

informacao.pop('nome')
print(f'.pop(): {informacao}')

informacao.popitem()
print(f'.popitem(): {informacao}')

hobbies = {'ler': ['Fluent Python', 'Introdução do Python'], 'series': ['Friends', 'Brooklyn 99']}
informacao.update(hobbies)
print(f'.update(): {informacao}')
LETRA_NUM = [
    ('a', 1),
    ('b', 2),
    ('c', 3),
    ('d', 4),
    ('e', 5)
]

letra_num = {num: letra for letra, num in LETRA_NUM}
print(letra_num)








