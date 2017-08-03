import tools

#Obtengo el vector de la matriz
def get_vector_from_matrix(matrix, index):
	return [matrix[i][index] for i in range(len(matrix))]



#Comparo dos palabras entre si
def compare_two_words(dictionary, matrix, word1, word2):
	index1 = tools.get_index_of_word(dictionary, word1)
	index2 = tools.get_index_of_word(dictionary, word2)
	
	

	return compare_two_indexes(dictionary, matrix, index1, index2)


def compare_two_indexes(dictionary, matrix, index1, index2):
	vector1 = get_vector_from_matrix(matrix, index1)
	vector2 = get_vector_from_matrix(matrix, index2)

	similitud = tools.cosine_term_x_term(vector1, vector2)
	return similitud


def neighbourhood_of_word(dictionary, matrix, word):
	index1 = tools.get_index_of_word(dictionary, word)
	amount_of_words = len(matrix[0])
	similarity_results = []

	for index2 in range(amount_of_words):
		similarity_results.append( compare_two_indexes(dictionary, matrix, index1, index2) )

	return similarity_results