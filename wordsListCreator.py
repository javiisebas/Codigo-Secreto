import io
import os
import random as rd


def wordsList():
	
	lista = io.open('palabras.txt', mode="r", encoding="utf-8")
	palabras = lista.read().split('\n')[:-1]
	tam = len(palabras) - 1
	palabras_juego = []

	for i in range(30):
		palabra_aleatoria = palabras[rd.randint(0,tam)]
		while palabra_aleatoria in palabras_juego:
			palabra_aleatoria = palabras[rd.randint(0,tam)]
		palabras_juego.append(palabra_aleatoria) 

	return palabras_juego



