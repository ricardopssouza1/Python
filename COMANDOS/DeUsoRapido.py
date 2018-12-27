#Variáveis
>>> a, b = 10, 20
>>> a
10
>>> b
20


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

#Endentação
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
	
	# Exempo com while...	
	count = 0
	while count <= 5:
		print(count)
		count += 1
	# 0 1 2 3 4 5
	
	
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




















