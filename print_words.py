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


print 'Elegir UN solo libro'
dictionary_folder = '/Lsaed books/Dictionaries/'
book = tool.pick_books( tool.get_books(dictionary_folder) ) [0]

respuesta = raw_input('Desea ver las palabras que contiene ( escriba r) o las similitudes (escriba s)?')
if (respuesta == 'r'):
	print_words(book)
else: 
	print_all_sorted_words(book)