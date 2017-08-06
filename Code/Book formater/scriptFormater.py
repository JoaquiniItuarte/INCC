#Importo las funciones
import formater
import os
from os import listdir
from os.path import isfile, join



#Genero la lista de paths posibles
def get_files(folder_name):
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

def analize_one_book(book):

	list_of_paragraph = formater.formateo_libro( book )
	#print(list_of_paragraph)
	formater.guardar_libro_formateado( list_of_paragraph, book + '_formateado.txt' )
	print('termine el libro')
	print(book)



files = get_files('')
books = pick_books(files)

for book in books:
	analize_one_book(book)

