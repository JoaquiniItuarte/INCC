import copy
import scipy


def remove_duplicates(list_of_list_of_words):
	""" remove duplicates from a list """

	return set((item for list_of_words in list_of_list_of_words for item in list_of_words))


#Crea un vector de indices mapeado a las palabras de la lista de parrafos
def get_vector_keyword_index(documentList):

	#Remove common words which have no search value
	uniqueVocabularyList = remove_duplicates(documentList)

	vectorIndex={}
	offset=0

	#Associate a position with the keywords which maps to the dimension on the vector used to represent this word
	for word in uniqueVocabularyList:
		vectorIndex[word]=offset
		offset+=1

	return vectorIndex  #(keyword:position)


#hace el vector contador de palabras de un parrafo
def make_vector(paragraph, vectorKeywordIndex):
	#Initialise vector with 0's
	vector = [0] * len(vectorKeywordIndex)
	
	for word in paragraph:
		vector[vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
	
	return vector


#Hago la matriz ([ [col1] [col2] ... [...] ]). Matrix = [paragraph][term]
def make_matrix(book, vectorKeywordIndex):
	#Creo una matriz vacia
	matrix = []

	#Me genera la matriz docs*terminos y necesito terminos*docs
	for paragraph in book:
		#Creo una nueva columna
		matrix.append( make_vector(paragraph, vectorKeywordIndex) )

	return matrix


#Aplico la transformacion tfidf (crea una nueva)
def tfidfTransform(matrix):
	""" Apply TermFrequency(tf)*inverseDocumentFrequency(idf) for each matrix element.
	This evaluates how important a word is to a document in a corpus

	With a document-term matrix: matrix[x][y]
	tf[y][x] = frequency of term y in document x / frequency of all terms in document x
	idf[y][x] = log( abs(total number of documents in corpus) / abs(number of documents with term y)  )
	Note: This is not the only way to calculate tf*idf
	"""

	tfid_matrix = copy.deepcopy(matrix)
	document_total = len(matrix) 
	rows = document_total #Cantidad de documentos
	cols = len( matrix[0] ) #Cantidad de terminos

	
	for row in xrange(0, rows):
		#Por cada documento obtengo el total de palabras.
		word_total= reduce(lambda x, y: x+y, matrix[row] )


		for col in xrange(0, cols): #For each term

			#For consistency ensure all self.matrix values are floats
			tfid_matrix[row][col] = float(tfid_matrix[row][col])

			if matrix[row][col]!=0:
				tfid_matrix[row][col] = hacer_tf_idf(row, col, word_total, matrix, document_total, cols, rows)

	return tfid_matrix


def hacer_tf_idf(row, col, word_total, matrix, document_total, cols, rows):
	term_frequency = matrix[row][col] / float(word_total)
	inverse_document_frequency = scipy.log(abs(document_total / float(get_term_document_occurences(col, cols, rows, matrix))))
	return term_frequency * inverse_document_frequency


def get_term_document_occurences(col, cols, rows, matrix):
	""" Find how many documents a term occurs in"""

	term_document_occurrences = 0

	for n in xrange(0,rows):
		if matrix[n][col] > 0: #Term appears in document
			term_document_occurrences +=1
	return term_document_occurrences


#Reduzco las dimensiones de sigma (sigma siendo una lista. Modifico sigma)
def reduce_dimensions(sigma, k):
	for index in xrange(k, len(sigma)):
		sigma[index] = 0


