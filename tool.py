import os
from os import listdir
from os.path import isfile, join

#Genero la lista de paths posibles
def get_books(folder_name):
	directorio = os.getcwd() + folder_name
	paths = [f for f in listdir(directorio) if isfile(join(directorio, f))]
	lista_a_devolver = []
	for book_name in paths:
		lista_a_devolver.append(book_name)
	
	return lista_a_devolver

def pick_books(books):

	lista_a_devolver = []
	for book in books:
		respuesta = raw_input('Desea usar el siguiente libro? (y/n): '+ book +':  ')
		if(respuesta=='y'):
			lista_a_devolver.append(book)

	return lista_a_devolver