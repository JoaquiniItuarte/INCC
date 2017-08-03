import pickle

#Guarda los datos pasados como parametros a un archivo de nombre "book_name"
def save_data_lsa(lsa_matrix, lsa_word_to_index_dictionary, book_full_path, book_name, folder_to_save_data):
	save_lsa_matrix(lsa_matrix, folder_to_save_data + '/Matrices/' + book_name )
	save_lsa_dictionary(lsa_word_to_index_dictionary, folder_to_save_data + '/Dictionaries/' + book_name )


#Guardar matrix al archivo nuevo file_name
def save_lsa_matrix(lsa_matrix, file_name):
	pickle.dump( lsa_matrix, open( file_name, "wb" ) )

'''
	rows = len( lsa_matrix ) #Cantidad de documentos
	cols = len( lsa_matrix[0] ) #Cantidad de terminos

	with open(file_name, 'w') as file:
		file.write( 'Docs: ' + rows + '\n' )
		file.write( 'Terms: ' + cols + '\n' )

		for lista in lsa_matrix:
			for word in lista:
				file.write( word + ' ')

			file.write( '\n' )
'''

#Guardar dictionary al archivo nuevo file_name
def save_lsa_dictionary(lsa_word_to_index_dictionary, file_name):
	pickle.dump( lsa_word_to_index_dictionary, open( file_name, "wb" ) )


#Carga la matriz de lsa
def load_lsa_matrix(file_name):
	return pickle.load( open( file_name , "rb" ) )


#Carga el diccionario del lsa
def load_lsa_dictionary(file_name):
	return pickle.load( open( file_name , "rb" ) )


#Carga la matriz del lsa y el diccionario y los devuelve en ese orden
def load_data_lsa(book_name):
	lsa_matrix = load_lsa_matrix(book_name + '/' + book_name + '_matrix.txt') 
	lsa_dictionary = load_lsa_dictionary(book_name + '/' +  book_name + '_dictionary.txt')
	

#Carga el libro formateado y devuelve una lista de lista de terminos (lista de parrafos)
def load_book(file_name):
	return pickle.load( open( file_name , "rb" ) )