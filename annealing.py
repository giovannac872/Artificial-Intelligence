from math import exp, expm1
from random import randint
import time

class OBJECT:

	def __init__(self, beneficio, valorBeneficio, peso, valorPeso, pesoMax, instancia):
		self.beneficio = beneficio
		self.valorBeneficio  = valorBeneficio
		self.peso = peso
		self.valorPeso = valorPeso
		self.pesoMax = pesoMax
		self.instancia = instancia

	def get_valorPeso(self):
		return self.valorPeso

	def get_beneficio(self):
		return self.beneficio

	def get_peso(self):
		return self.peso

	def get_instancia(self):
		return self.instancia


def instanciaAleatoria():
	instancia = []
	for i in range(8):
		instancia.append(randint(0,1))

	return instancia



def valorPesoMochila(instancia, peso, tam):
	soma = 0
	for i in range(tam):
		if instancia[i] == 1:
			soma += peso[i]

	return soma

def valorBeneficioMochila(instancia, beneficio, tam):
	soma = 0
	for i in range(tam):
		if instancia[i] == 1:
			soma += beneficio[i]

	return soma

def criaObjeto(beneficio, peso, tam, pesoMax):
	instancia = instanciaAleatoria()
	valorBeneficio = valorBeneficioMochila(instancia, beneficio, tam)
	valorPeso = valorPesoMochila(instancia, peso, tam)

	objeto = OBJECT(beneficio, valorBeneficio, peso, valorPeso, pesoMax, instancia)

	return objeto

def probabilidadeAceitar(deltaE, temperaturaCorrente):
	return exp(deltaE / temperaturaCorrente)



startTime = time.time()
beneficio = [3, 3, 2, 4, 2, 3, 5, 2]
peso = [5, 4, 7, 8, 4, 4, 6, 8]

objetoAtual = instanciaAleatoria()
while valorPesoMochila(objetoAtual, peso, 8) >25:
	objetoAtual = instanciaAleatoria()

pesoObjetoAtual = valorPesoMochila(objetoAtual, peso, 8)
beneficioObjetoAtual = valorBeneficioMochila(objetoAtual, beneficio, 8)
temperaturaInicial= 1.0
temperaturaFinal = 0.00001
alpha = 0.99
i=0
resultado = None

print("primeiro objeto: ", objetoAtual)
while temperaturaInicial > temperaturaFinal:
#while temperaturaFinal == 0.00001:
	if i == 10000:
		resultado = OBJECT(beneficio, beneficioObjetoAtual, peso, pesoObjetoAtual, 25, objetoAtual)
		break

	novoObjeto = instanciaAleatoria()
	pesoNovoObjeto = valorPesoMochila(novoObjeto, peso, 8)
	if pesoNovoObjeto > 25:
		continue
	beneficioNovoObjeto = valorBeneficioMochila(novoObjeto, beneficio, 8)
	print("Estado Atual: " + str(novoObjeto))
	print("Temperatura Atual: " + str(temperaturaInicial) + "\n")
	deltaE = beneficioNovoObjeto - beneficioObjetoAtual
	if deltaE > 0:
		objetoAtual = novoObjeto
		pesoObjetoAtual = pesoNovoObjeto
		beneficioObjetoAtual = beneficioNovoObjeto
	else:
		if probabilidadeAceitar(deltaE, temperaturaInicial) > 0.5: # se a probabilidade for maior que 50% eu aceito esse "caso pior"
			objetoAtual = novoObjeto
			pesoObjetoAtual = pesoNovoObjeto
			beneficioObjetoAtual = beneficioNovoObjeto

	temperaturaInicial = temperaturaInicial * alpha

	i +=1


if resultado != None:
	print(resultado.instancia)
else:
	print(objetoAtual)

endTime = time.time()
print("time: ", endTime - startTime)