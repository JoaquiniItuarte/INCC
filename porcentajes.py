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
	dictionary = pickle.load( open( file_name , "rb" ) )
	return dictionary

def reset_summary(top_limit):
	porcentajes_folder = '/Lsaed books/Porcentajes/'
	current_dir = os.getcwd()

	with open( current_dir + porcentajes_folder +'summary_' + str(top_limit), 'w+' ) as file_summary:
		print 'Reseteando summary'

def add_to_summary(strings, top_limit):
	porcentajes_folder = '/Lsaed books/Porcentajes/'
	current_dir = os.getcwd()

	with open( current_dir + porcentajes_folder +'summary_' + str(top_limit), 'a' ) as file_summary:
		file_summary.write('*********************\n')
		for string in strings:
			file_summary.write( string )
			#file_summary.write('\n')



def get_ranking(book_name, words, top_limit):
	dictionary_folder = '/Lsaed books/Dictionaries/'
	matrices_folder = '/Lsaed books/Matrices/'
	ranking_folder = '/Lsaed books/AllWordsFullRank/'
	similarities_folder = '/Lsaed books/Porcentajes/'
	current_dir = os.getcwd()

	with open( current_dir + similarities_folder + book_name + '_porcentajes', 'w+' ) as file_book:

		print 'Haciendo porcentaje para libro ', 
		print book_name
		dictionary = load_book_words_similarity (current_dir + ranking_folder + book_name)

		porcentaje_libro = 0
		for word in dictionary:

			file_book.write( '***************************************************************************************************')
			file_book.write('PALABRA ACTUAL: ' + word)
			file_book.write( ' \n')

			sorted_similarities_for_word_with_index = dictionary[word]
			palabras_elegidas = 0

			for index in range(top_limit):
				word2_raw = sorted_similarities_for_word_with_index[index][2]
				word2 = str( word2_raw )
				word2_index = str( sorted_similarities_for_word_with_index[index][1] )
				similitude_between_both_words = str( sorted_similarities_for_word_with_index[index][0] )
				
				#file_book.write( str(index) + ': ')
				file_book.write(', ' + word2)
				#file_book.write(similitude_between_both_words)
				if word2 in words:
					palabras_elegidas += 1
					file_book.write('*')
				#file_book.write('\n ')

			file_book.write('\n ')
			porcentaje_resultado = ( float(palabras_elegidas) /top_limit) * 100
			porcentaje_libro += porcentaje_resultado
			file_book.write('Relacion elegidas/totaldeltop: ' + str(palabras_elegidas) + '/' + str(top_limit)  + ' \n ')
			file_book.write('Relacion en %: ' + str(porcentaje_resultado)  + ' \n ')
			file_book.write('\n ')

		cantidad_de_palabras = len(dictionary.keys())
		string_fraccion_libro = 'Promedio total en libro (sumporcentajes/totaldelpalabras): ' + str(porcentaje_libro) + '/' + str(cantidad_de_palabras)  + ' \n '
		file_book.write( string_fraccion_libro)
		string_promedio_libro = 'Relacion en %: ' + str(porcentaje_libro/cantidad_de_palabras)  + ' \n '
		file_book.write(string_promedio_libro)
		file_book.write('\n ')

		strings = [ book_name+'\n' ,string_fraccion_libro, string_promedio_libro]
		add_to_summary(strings, top_limit)

		return porcentaje_libro/cantidad_de_palabras
			


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



def doshit(books, top_limit):
	reset_summary(top_limit)

	promedio_total_todos_libros = 0
	for book in books:
		print '***********************************************************************************************************'
		try:
			print 'Trying format 1'
			list_of_words = pick_up_words_from_file_try_1(book)
			promedio_total_todos_libros +=  get_ranking(book, list_of_words, top_limit)
		
		except Exception as e:
			print 'Error: ',
			print(e),
			print ' En libro: ' + book

			try:
				print 'Trying format 2'
				list_of_words = pick_up_words_from_file_try_2(book)
				promedio_total_todos_libros += get_ranking(book, list_of_words, top_limit)
			
			except Exception as e:
				print 'Error: ',
				print(e),
				print ' En libro: ' + book

				try:
					print 'Trying format 3'
					list_of_words = pick_up_words_from_file_try_3(book)
					promedio_total_todos_libros += get_ranking(book, list_of_words, top_limit)
						
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

	promedio_total_todos_libros = promedio_total_todos_libros / len(books)
	string_promedio_todos = 'PROMEDIO DE TODOS LOS LIBROS: ' + str( promedio_total_todos_libros)
	add_to_summary( [string_promedio_todos], top_limit )



print 'Elegir libros para hacer los rankings de cercania de palabras'
books = tool.pick_books ( tool.get_books('/Lsaed books/Words/') )

doshit(books, 30)
doshit(books, 40)
doshit(books, 50)
doshit(books, 60)
