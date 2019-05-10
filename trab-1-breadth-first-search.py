# -*- coding: utf-8 -*-
from collections import deque
import time
import math
#import copy
from copy import deepcopy



class NODE:
    def __init__(self, state, cost, parent, positionNull):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.positionNull = positionNull

def avoidingRepeatStates(state):
    global hashing

    if str(state) in hashing:
        return -1

    return 0

def rules(opens, closed, node):
    #global  v1
    #global arquivo
    global hashing

    auxiliar = list(node.positionNull)
    auxiliar2 = deepcopy(node.state)

    if auxiliar[0] > 0 and auxiliar[0]  <= 2: #primeira regra "subir posição nula"
        auxiliar2[auxiliar[0]][auxiliar[1]], auxiliar2[auxiliar[0]-1][auxiliar[1]] = auxiliar2[auxiliar[0]-1][auxiliar[1]], auxiliar2[auxiliar[0]][auxiliar[1]] 
        auxiliar[0] -= 1
        if avoidingRepeatStates(auxiliar2) != -1:
            #v1 += 1
            hashing[str(auxiliar2)] = True
            opens.append(NODE(auxiliar2, node.cost + 1, node, list(auxiliar)))

    auxiliar = list(node.positionNull)
    auxiliar2 = deepcopy(node.state)

    if auxiliar[0] < 2 and auxiliar[0] >=0: #segunda  regra, mover posicao nula para  baixo
        auxiliar2[auxiliar[0]][auxiliar[1]], auxiliar2[auxiliar[0]+1][auxiliar[1]] = auxiliar2[auxiliar[0]+1][auxiliar[1]], auxiliar2[auxiliar[0]][auxiliar[1]]
        auxiliar[0] += 1
        if avoidingRepeatStates(auxiliar2) != -1:
            #v1 += 1
            #arquivo.write(node.label + "->" + "N" + str(v1) + " [label=\"R2\"]\n")
            #arquivo.write("N" + str(v1) + "[label=\"" + str(auxiliar2) + "\"]\n")
            hashing[str(auxiliar2)] = True
            #insert(valueKey(auxiliar2), auxiliar2)
            opens.append(NODE(auxiliar2, node.cost + 1, node, list(auxiliar)))

    auxiliar = list(node.positionNull)
    auxiliar2 = deepcopy(node.state)	

    if auxiliar[1] < 2 and auxiliar[1] >= 0: #terceira regra, mover posição nula para a direita
        auxiliar2[auxiliar[0]][auxiliar[1]], auxiliar2[auxiliar[0]][auxiliar[1] + 1] = auxiliar2[auxiliar[0]][auxiliar[1] + 1], auxiliar2[auxiliar[0]][auxiliar[1]]
        auxiliar[1] += 1
        if avoidingRepeatStates(auxiliar2) != -1:
            #v1 += 1
            #arquivo.write(node.label + "->" + "N" + str(v1) + " [label=\"R3\"]\n")
            #arquivo.write("N" + str(v1) + "[label=\"" + str(auxiliar2) + "\"]\n")
            hashing[str(auxiliar2)] = True
            #insert(valueKey(auxiliar2), auxiliar2)
            opens.append(NODE(auxiliar2, node.cost + 1, node, list(auxiliar)))

    auxiliar = list(node.positionNull)        
    auxiliar2 = deepcopy(node.state)

    if auxiliar[1] > 0 and auxiliar[0] <= 2: # quarta regra, mover para esquerda posição nula
        auxiliar2[auxiliar[0]][auxiliar[1]], auxiliar2[auxiliar[0]][auxiliar[1]-1] = auxiliar2[auxiliar[0]][auxiliar[1] - 1], auxiliar2[auxiliar[0]][auxiliar[1]]
        auxiliar[1] -= 1
    if avoidingRepeatStates(auxiliar2) != -1:
            #v1 += 1
            #arquivo.write(node.label + "->" + "N" + str(v1) + " [label=\"R4\"]\n")
            #arquivo.write("N" + str(v1) + "[label=\"" + str(auxiliar2) + "\"]\n")
            hashing[str(auxiliar2)] = True
            #insert(valueKey(auxiliar2), auxiliar2)
            opens.append(NODE(auxiliar2, node.cost + 1, node, list(auxiliar)))


def indice(matriz, elemento = 0, ordem = 3):	#retorna uma lista com as coordenadas do elemento vazio

    k = [e for l in matriz for e in l].index(elemento)
    linha = int(k/ordem)
    coluna = k%ordem
    posicao = [linha, coluna]
    
    return posicao


def isSolvable(state, goalState):
    n = 9
    inversions = 0		
    aux = [x for y in state for x in y]
    for x in range(n-1):
        y = x+1
        if aux[x] != 0:
            while y < n:
                if aux[y] != 0:
                    if aux[x] > aux[y]:
                        inversions +=1
                y += 1
    goalNull = indice(goalState)
    value = goalNull[0]+1 # considerar contagem das linhas a partir de 1
    if value % 2 == 0: # Se a linha que a posicao vazia estiver for par
        
        if inversions % 2 == 0: 
            return False  
		
        return True # o numero de inversoes deve ser impar para ter solucao
	
    else: # Se a linha que a posicao vazia estiver for impar
        if inversions % 2 != 0: 
            return False  
		
        return True # o numero de inversoes deve ser par para ter solucao

def leMatriz(n_linhas, n_colunas):
    matriz = []
    linha = [] 
    while len(matriz) != n_linhas :
        n = int(input())
        linha.append(n)
        if len(linha) == n_colunas:
            matriz.append(linha)
            linha = []
    
    return matriz
                    

if __name__ == '__main__':

    print("8-PUZZLE")
    print("Informe estado inicial desejado: ")
    print("NOTA: Utilize o valor 0 para representar o espaço em branco")
    print("NOTA: Insira um elemento por vez")
    initialState = leMatriz(3, 3)
    print("Informe estado final: ")
    print("NOTA: Utilize o valor 0 para representar o espaço em branco")
    print("NOTA: Insira um elemento por vez")
    goalState = leMatriz(3, 3) 
    startTime = time.time()
    if isSolvable(initialState, goalState) == False :
        print("Não é possível chegar ao estado final !!")
        quit()
    else:	
        print("Solução Possivel de Ser encontrada !!")
    
    opens = deque([]) 
    closed = deque([])
    hashing = {}
    opens.append(NODE(initialState, 0, None, indice(initialState)))
    hashing[str(initialState)] = True
    

    aux = 1
    while aux == 1:
        if not opens:
            break
          
        else:
            node = opens.popleft()
            closed.append(node)
            if node.state == goalState:
                print("Solucao Encontrada")
                value = closed.pop()
                print("Profundidade: ",value.cost)
                print("Quantidade  de elementos: ", len(hashing))
                break
              
            else:
                rules(opens, closed, node)


    endTime = time.time()
#arquivo.write("\n}\n")
#arquivo.close()



print("tempo de execucao: ", endTime - startTime, "segundos")

