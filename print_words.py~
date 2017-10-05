import Code.LSA.loadSaveLsaData as loadSaveLsaData
import Code.Tools.compareTwoWords as comparer
import tool
import pickle
import os
from os import listdir
from os.path import isfile, join



def print_words(book_name):
	dictionary_folder = '/Lsaed books/Dictionaries/'
	current_dir = os.getcwd()
	book_path = current_dir + dictionary_folder + book_name

	dictionarie = loadSaveLsaData.load_lsa_dictionary( book_path )
	
	print 'Palabras del libro: ' + book_name

	for word in sorted(dictionarie.keys()):
		print word

def print_words_2(book_name):
	dictionary_folder = '/Lsaed books/Dictionaries/'
	current_dir = os.getcwd()
	book_path = current_dir + dictionary_folder + book_name

	dictionarie = loadSaveLsaData.load_lsa_dictionary( book_path )

	with open( current_dir + '/Lsaed books/ALLWORDS/' + book_name, "w+" ) as file_book:
		for word in sorted(dictionarie.keys()):
			file_book.write(word)
			file_book.write('\n')

def print_all_sorted_words(book):
	similarities_folder = '/Lsaed books/Dictionaries/'
	directorio = os.getcwd() + similarities_folder + book
	dictionary_of_similarities = loadSaveLsaData.load_lsa_dictionary( directorio)
	
	print book
	for word, value in dictionary_of_similarities.items():
		print(word)




print 'Elegir UN solo libro'
dictionary_folder = '/Lsaed books/Dictionaries/'
books = tool.pick_books( tool.get_books(dictionary_folder) )

print '****************************************************'
print '****************************************************'
print '****************************************************'
print '****************************************************'
print '****************************************************'
print '****************************************************'

respuesta = raw_input('Desea ver las palabras que contiene ( escriba r) o las similitudes (escriba s)?')
if (respuesta == 's'):
	for book in books:
		print_all_sorted_words(book)
else:
	for book in books:
		print_words_2(book)

	
	