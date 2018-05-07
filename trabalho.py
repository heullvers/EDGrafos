from funcoes import *
from classes import *

'''
matriz = []
for i in range(x):
	linha = []
	for j in range(x):
		linha.append(valor)
	matriz.append(linha)

'''


'''
#IMPRESSÃO
for i in matriz:
	for j in i:
		print(j, end = ' ')
	print("\n")
'''

nomeArquivo = input("Digite o nome do arquivo: ")
direcionado = ehDirecionado(nomeArquivo)
#lista = listarLigacoes(nomeArquivo)
#print(lista)

ponderado = ehPonderado(nomeArquivo)
listaA = listarArestas(nomeArquivo)
#print(listaA)
listaV = listarVertices(nomeArquivo)
grafo = Grafo(listaV, listaA, direcionado, ponderado)
print('Vertices: ', grafo.vertices)
print('Arestas: ', grafo.arestas)
imprimirMatriz(geraMA(grafo))
imprimirMatriz(geraMI(grafo))


'''
matrizMA = geraMA(grafo)
imprimirMatriz(matrizMA)
print()
matrizMI = converteMAParaMI(matrizMA,grafo.direcionado, grafo.ponderado)
imprimirMatriz(matrizMI)

#print(ehPonderado(nomeArquivo))
#print("Matriz:\n")
#matriz = geraMI(grafo)
#imprimirMatriz(matriz)

#n5_dir_unwgt_comb0.txt
#n10_dir_wgt_comb3.txt
