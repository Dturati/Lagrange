#Python 3
#David Turati
#Metodo de imterpolacao  da forma de lagrange

# _*_ coding:latin 1 _*_
from math import sqrt
from functools import reduce

class Lagrange(object):
	dominio=[]
	imagem = []
	resultado_numerador = []
	resultado_denominador = []
	temp = []
	#construtor
	def __init__(self,tm):
		print("Inicio")
		self.__tamanho = tm
		for i in range(tm):
			self.resultado_denominador.append(0)
			self.resultado_numerador.append(str(" "))

	#metodos getters
	def get__Tamanho(self):
		return self.__tamanho

	#metodos setters
	def set__Tamanho(self,tm):
		sefl.__tamanho = tm
	
	#preenche vetor com os valores do dominio
	def preeche_dominio(self):
		for i in range(self.__tamanho):
			print("Digite um valor para x:")
			self.dominio.append(int(input()))
		print(" ")

	#preenche vetor com os valores da imagem
	def preeche_imagem(self):
		for i in range(self.__tamanho):
			print("Digite um valor pra fx:")
			self.imagem.append(int(input()))
		print(" ")
	
	#calcula valores do denominador
	def calcula(self):
		for i in range(self.tamanho):
			self.resultado_numerador[i]=(str(self.imagem[i])+"*")
			for j  in range(self.tamanho):
				if (j != i):
					#realiza subtracoes dos elentos do denominador
					self.temp.append(self.subtracao(self.dominio[i],self.dominio[j]))
					self.resultado_numerador[i]+=str(('x',-self.dominio[j]))
			#realiza multiplicacao dos elementos do denominador
			self.resultado_denominador[i] = reduce( (lambda x,y : x*y),self.temp)
			#remove elementos da lista 
			tm = len(self.temp)-1
			while(tm >= 0):
				del self.temp[tm]
				tm = tm-1
		print(" ")

	#realiza subtracao no denominador
	def subtracao(self,x,y):
		return x-y

	#imprime dominio e imagem
	def imprime_dominio_imagem(self):
		dm = lambda i : i
		print("Dominio X")
		print(dm(self.dominio))

		print("Imagem F(x)")
		img = lambda j : j
		print(img(self.imagem))

	#imprime resultado
	def imprime_resultado(self):
		print("As equações são:")
		for i,j in enumerate(self.resultado_numerador):
			print(j,"Divido por",self.resultado_denominador[i])
		print(" ")

	#property
	tamanho = property(fget = get__Tamanho , fset = set__Tamanho)

class Calcula(Lagrange):
		def fim(self):
			print("Fim")

print("digite o tamando do dominio e da imagem")
c = Calcula(int(input())) #cria objeto

#chamada de funcoes
c.preeche_dominio()

c.preeche_imagem()

c.imprime_dominio_imagem()

c.calcula()

c.imprime_resultado()

c.fim()