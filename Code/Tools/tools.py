import numpy as np

#Obtengo indice de la palabra en el diccionario
def get_index_of_word(dictionary, word):
	return dictionary[word]


#Devuelve la matriz transpuesta
def transpose_matrix(matrix):
	return [list(x) for x in zip(*matrix)]


#Similitud coseno entre dos vectores
def cosine_term_x_term(vector1, vector2):
	return float(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))


#matrix es la traspuesta, #terms = len(matrix), #docs = len( matrix[0] )
#Devuelve un vector donde el i esimo elemento es la similtud coseno de i con index_term
def cosine_term_x_matrix(index_term, matrix):
	vector_res = []
	
	for idx in range(len (matrix) ): #Por cada termino
		vector_res.append( cosine_term_x_term( matrix[index_term], matrix[idx] ) )

	return vector_res


#matrix es la transpuesta. devuelve una matriz de #terms_x_#terms
#donde se relacionan los terminos col-esimos con los row-esimos
def cosine_matrix_x_matrix(matrix):
	matrix_res = []

	for idx in range( len(matrix) ):
		matrix_res.append( cosine_term_x_matrix( idx, matrix ) )


	return matrix_res

