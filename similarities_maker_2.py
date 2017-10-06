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


def generate_similarities():
	dictionary_folder = '/Lsaed books/Dictionaries/'
	matrices_folder = '/Lsaed books/Matrices/'
	similarities_folder = '/Lsaed books/Similarities/'
	current_dir = os.getcwd()

	#Para un libro diccionario y matriz tienen el mismo nombre de archivo, el nombre del libro
	dictionaries = tool.get_books(dictionary_folder)
	dictionaries = tool.pick_books(dictionaries)
	matrices = tool.get_books(matrices_folder)
	matrices = tool.pick_books(matrices)


	sorted_results_for_book = {}

	for book in matrices:
		dictionary_of_book = loadSaveLsaData.load_lsa_dictionary( current_dir+dictionary_folder + book)
		dictionary_of_book_keys = dictionary_of_book.keys()
		dictionary_of_book_values = dictionary_of_book.values()
		matrix = loadSaveLsaData.load_lsa_matrix(current_dir+matrices_folder + book)

		print 'Haciendo similarities para un libro'
		print len(dictionary_of_book_keys)
		dictionary = {}
		for word, word_index in dictionary_of_book.items():

			print 'palabra: ',
			print word
			similarities_for_word = comparer.neighbourhood_of_word(dictionary_of_book, matrix, word)
			
			similarities_for_word_with_index = []
			for index in range(len(similarities_for_word)):
				similarities_for_word_with_index.append( [similarities_for_word[index], index, dictionary_of_book_keys[dictionary_of_book_values.index(index)]])

			sorted_similarities_for_word_with_index = list(reversed( sorted(similarities_for_word_with_index, key=lambda x: x[0] ) ))
			dictionary[word] = sorted_similarities_for_word_with_index

		print 'holaaaa'
		print dictionary
		save_book_words_similarity(dictionary, current_dir + similarities_folder + book)


def get_word_similars(similarities, word):
	return similarities[word]

def get_similarities_of_book(book_name):
	similarities_folder = '/Lsaed books/Similarities/'
	current_dir = os.getcwd()
	file_name = current_dir + similarities_folder + book_name

	return load_book_words_similarity(file_name)


def get_ranking(book_name, words, top_limit):
	dictionary_folder = '/Lsaed books/Dictionaries/'
	matrices_folder = '/Lsaed books/Matrices/'
	similarities_folder = '/Lsaed books/Similarities/'
	current_dir = os.getcwd()

	

	dictionary_of_book = loadSaveLsaData.load_lsa_dictionary( current_dir+dictionary_folder + book_name)
	dictionary_of_book_keys = dictionary_of_book.keys()
	dictionary_of_book_values = dictionary_of_book.values()
	matrix = loadSaveLsaData.load_lsa_matrix(current_dir+matrices_folder + book_name)

	with open( current_dir + similarities_folder + book_name + '_Familias', 'w+' ) as file_book:

		print 'Haciendo similarities para un libro'
		print book_name
		#dictionary = {}
		for word in words:
			file_book.write( '***************************************************************************************************')
			file_book.write('PALABRA: ' + word)
			file_book.write( ' Top similares: \n')

			print 'palabra actual: ',
			print word
			similarities_for_word = comparer.neighbourhood_of_word(dictionary_of_book, matrix, word)
			
			similarities_for_word_with_index = []
			for index in range(top_limit): #range(len(similarities_for_word)):
				similarities_for_word_with_index.append( [similarities_for_word[index], dictionary_of_book_values.index(index), dictionary_of_book_keys[dictionary_of_book_values.index(index)]])

			sorted_similarities_for_word_with_index = list(reversed( sorted(similarities_for_word_with_index, key=lambda x: x[0] ) ))

			for index in range(len(sorted_similarities_for_word_with_index)):
				word2 = str( sorted_similarities_for_word_with_index[index][2] )
				word2_index = str( sorted_similarities_for_word_with_index[index][1] )
				similitude_between_both_words = str( sorted_similarities_for_word_with_index[index][0] )
				
				file_book.write( str(index) + ': ')
				file_book.write(word2 + ' ')
				file_book.write(similitude_between_both_words)
				if word2 in words:
					file_book.write(' *************')
				file_book.write('\n ')




			#dictionary[word] = sorted_similarities_for_word_with_index
			

		#save_book_words_similarity(dictionary, current_dir + similarities_folder + book_name)

	#return dictionary

def print_top_words(top_amount, book):
	similarities_folder = '/Lsaed books/Similarities/'
	directorio = os.getcwd() + similarities_folder + book
	dictionary_of_similarities = loadSaveLsaData.load_lsa_dictionary( directorio)
	
	for word, value in dictionary_of_similarities.items():
		
		print('Palabra: '),
		print(word)

		print('Top relacionadas: ')		
		
		for i in range( top_amount):
			print(i),
			print(value[i])



def print_all_sorted_words(book):
	similarities_folder = '/Lsaed books/Similarities/'
	directorio = os.getcwd() + similarities_folder + book
	dictionary_of_similarities = loadSaveLsaData.load_lsa_dictionary( directorio)
	
	for word, value in dictionary_of_similarities.items():
		
		print('Palabra: '),
		print(word)

		print('Top relacionadas: ')		
		
		for i in range( len(value) ):
			print(i),
			print(value[i])


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
top_limit = 30

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



