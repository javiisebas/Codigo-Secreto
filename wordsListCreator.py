import io
import os
import random as rd


def wordsList(palabras_repetidas):
	
	lista = io.open(os.getcwd() + "/data/palabras.txt", mode="r", encoding="utf-8")
	palabras = lista.read().split('\n')[:-1]
	tam = len(palabras) - 1
	palabras_juego = []

	for i in range(25):
		palabra_aleatoria = palabras[rd.randint(0,tam)]
		while palabra_aleatoria in palabras_juego or palabra_aleatoria in palabras_repetidas:
			palabra_aleatoria = palabras[rd.randint(0,tam)]
		palabras_juego.append(palabra_aleatoria) 

	return palabras_juego
	
