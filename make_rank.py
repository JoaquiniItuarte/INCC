import Code.LSA.loadSaveLsaData as loadSaveLsaData
import Code.Tools.compareTwoWords as comparer
import tool
import pickle
import os
from os import listdir
from os.path import isfile, join

def save_book_words_similarity(similarities, file_name):
	pickle.dump( similarities, open( file_name, "wb" ) )

def load_book_words_similarity(file_name):
	return pickle.load( open( file_name , "rb" ) )





def get_ranking(book_name, words, top_limit):
	dictionary_folder = '/Lsaed books/Dictionaries/'
	matrices_folder = '/Lsaed books/Matrices/'
	similarities_folder = '/Lsaed books/AllWordsFullRank/'
	current_dir = os.getcwd()

	

	dictionary_of_book = loadSaveLsaData.load_lsa_dictionary( current_dir+dictionary_folder + book_name)
	dictionary_of_book_keys = dictionary_of_book.keys()
	dictionary_of_book_values = dictionary_of_book.values()
	matrix = loadSaveLsaData.load_lsa_matrix(current_dir+matrices_folder + book_name)



	print 'Haciendo similarities para un libro'
	print book_name
	dictionary = {}
	for word in words:

		print 'palabra actual: ',
		print word
		
		similarities_for_word = comparer.neighbourhood_of_word(dictionary_of_book, matrix, word)
		
		similarities_for_word_with_index = []
		for index in range(len(similarities_for_word)):
			similarities_for_word_with_index.append( [similarities_for_word[index], dictionary_of_book_values.index(index), dictionary_of_book_keys[dictionary_of_book_values.index(index)]])

		sorted_similarities_for_word_with_index = list(reversed( sorted(similarities_for_word_with_index, key=lambda x: x[0] ) ))
		dictionary[word] = sorted_similarities_for_word_with_index
	
	save_book_words_similarity(dictionary, current_dir + similarities_folder + book_name)



def pick_up_words_from_file_try_1(book_name):
	similarities_folder = '/Lsaed books/Words/'
	directorio = os.getcwd() + similarities_folder + book_name
	words = []
	file_opened = open( directorio )
	for line in file_opened.readlines():
		#words_list = line.decode("utf-8-sig").encode("utf-8").split()
		#words_list = line.decode('cp1250').encode("utf-8").split() #the hand - more notes -
		words_list = line.split() #factotum - shortstory
		if len(words_list) > 0:
			word = words_list[0]
			words.append(word)
	return words

def pick_up_words_from_file_try_2(book_name):
	similarities_folder = '/Lsaed books/Words/'
	directorio = os.getcwd() + similarities_folder + book_name
	words = []
	file_opened = open( directorio )
	for line in file_opened.readlines():
		#words_list = line.decode("utf-8-sig").encode("utf-8").split()
		words_list = line.decode('cp1250').encode("utf-8").split() #the hand - more notes -
		#words_list = line.split() #factotum - shortstory
		if len(words_list) > 0:
			word = words_list[0]
			words.append(word)

	return words

def pick_up_words_from_file_try_3(book_name):
	similarities_folder = '/Lsaed books/Words/'
	directorio = os.getcwd() + similarities_folder + book_name
	words = []
	file_opened = open( directorio )
	for line in file_opened.readlines():
		words_list = line.decode("utf-8-sig").encode("utf-8").split()
		#words_list = line.decode('cp1250').encode("utf-8").split() #the hand - more notes -
		#words_list = line.split() #factotum - shortstory
		if len(words_list) > 0:
			word = words_list[0]
			words.append(word)	

	return words


print 'Elegir libros para hacer los rankings de cercania de palabras'
books = tool.pick_books ( tool.get_books('/Lsaed books/Words/') )
top_limit = 50

for book in books:
	print '***********************************************************************************************************'
	try:
		print 'Trying format 1'
		list_of_words = pick_up_words_from_file_try_1(book)
		get_ranking(book, list_of_words, top_limit)
	
	except Exception as e:
		print 'Error: ',
		print(e),
		print ' En libro: ' + book

		try:
			print 'Trying format 2'
			list_of_words = pick_up_words_from_file_try_2(book)
			get_ranking(book, list_of_words, top_limit)
		
		except Exception as e:
			print 'Error: ',
			print(e),
			print ' En libro: ' + book

			try:
				print 'Trying format 3'
				list_of_words = pick_up_words_from_file_try_3(book)
				get_ranking(book, list_of_words, top_limit)
					
			except Exception as e:
				print '############################################################################################################'
				print '############################################################################################################'
				print '############################################################################################################'
				print 'Error: ',
				print(e),
				print ' En libro: ' + book

	''' para probar que puedo leer lo guardado
	similarities_folder = '/Lsaed books/AllWordsFullRank/'
	rank = load_book_words_similarity( os.getcwd() + similarities_folder + book)
	print rank
	'''


