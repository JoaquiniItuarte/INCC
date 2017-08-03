import compateTwoWords as comparer


def neighbourhood_of_word(dictionary, matrix, word):
	index = get_index_of_word(dictionary, word)
	amount_of_words = len(matrix[0])
	similarity_results = []

	for index2 in range(amount_of_words):
		similarity_results.append( comparer.compare_two_indexes(dictionary, matrix, index1, index2) )

	return similarity_results