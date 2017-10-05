import Code.LSA.loadSaveLsaData as loadSaveLsaData
import Code.Tools.compareTwoWords as comparer
import tool
import pickle
import os
from os import listdir
from os.path import isfile, join







def obtain_seed(book):
		
	
def obtain_general_seed():

#se puede ver si la palabra esta en las seeds resaltarlas o ponerle algun caracter al final para reconocer al mas facil
def save_similarities_fow_word(word, value, top_limit):
	print word,
	print ' : '
	for idx in range(top_limit):
		data_in_array = value[idx]
		current_similar_word = data_in_array[2]
		current_similar_index = data_in_array[1]
		current_similar_value = data_in_array[0]
		print current_similar_word,
		print ' ',
		print current_similar_value,
		print ' ',
		print current_similar_index


def print_top_similar_words(book, seed_of_words, top_limit):
	similarities_folder = '/Lsaed books/Dictionaries/'
	directorio = os.getcwd() + similarities_folder + book
	dictionary_of_similarities = loadSaveLsaData.load_lsa_dictionary( directorio)

	print '##########################################################################################################'	
	print 'Imprimiento libro: ',
	print book
	print 'Para la palabra: ',
	print(word)
	respuesta = raw_input('Desea imprimir el top de la palabra? (y/n)')
			
	for word, value in dictionary_of_similarities.items():		
		if word in seed_of_words:
			save_similarities_fow_word(word, value, top_limit)
			




dictionary_folder = '/Lsaed books/Dictionaries/'

top_limit = 50
general_seed = true
seed_of_words = obtain_general_seed()
for book in books:
	if general_seed:	
		seed_of_words = obtain_seed(book)
	print_top_similar_words(book, seed_of_words, top_limit):


