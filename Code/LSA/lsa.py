# coding=utf-8

import scipy #Para SVD
import scipy.linalg
import numpy
import vectorspace
import loadSaveLsaData #Para guardar el lsa una vez hecho y poder analizarlo despues
import os



#Funcion para hacer lsa y devuelve la matriz M*N; m = docs // n = terms.
# k = dimension reduccion. Default 300
#Retorna matriz, mapeo de palabra a indice
def apply_lsa(book_full_path, book_name, folder_to_save_data, k=300):

	print( 'Obteniendo matriz que representa al libro...\n' )
	list_of_list_of_words = loadSaveLsaData.load_book(book_full_path)

	#Obtengo un mapeo de palabra a indice de la fila de la matriz
	print( 'Generando diccionario de terminos...\n' )
	word_index_vector = vectorspace.get_vector_keyword_index(list_of_list_of_words)
	
	#Hago la matriz de concurrencias del libro. Cada columna es un parrafo del libro.
	#Cada fila es una palabra
	print( 'Generando matriz de concurrencia...\n' )
	concurrence_matrix = vectorspace.make_matrix(list_of_list_of_words, word_index_vector)

	#Aplico la trasnformacion tfidf (Term frequency, inverse document frequency) para mejorar
	#los resultados que puedo obtener con LSA
	print( 'Aplicando tfidf a la matriz de concurrencia...\n' )
	tfidf_matrix = vectorspace.tfidfTransform(concurrence_matrix)

	#Calculo SVD (Single Value Decomposition)
	#u*sigma,*vt = matrix
	print( 'Aplicando SVD...\n' )
	u,sigma,vt = numpy.linalg.svd( tfidf_matrix )

	#Reduzco las dimenciones de sigma hasta K dimensiones
	print( 'Reduciendo dimenciones de sigma...\n' )
	vectorspace.reduce_dimensions(sigma, k)

	#Calculo la nueva matriz a partir de sigma2
	#Reconstruct MATRIX'
	print( 'Reconstruyendo la matriz...\n' )
	tfidf_matrix = numpy.dot(numpy.dot(u, scipy.linalg.diagsvd(sigma, len(tfidf_matrix), len(vt))) ,vt)

	print( 'Guardando resultados obtenidos...\n' )
	loadSaveLsaData.save_data_lsa(tfidf_matrix, word_index_vector, book_full_path, book_name, folder_to_save_data)


	print('Termine libro')
	print(book_name)
	
	print( 'Retornada matriz y diccionario obtenidos. \n' )
	return tfidf_matrix, word_index_vector

	