import Code.LSA.lsa as lsa
import os
import tool
from os import listdir
from os.path import isfile, join

def make_lsa_for_all_books():
	print '****************** MAKING LSA FOR ALL BOOKS ********************************+'
	books_folder = '/Formated books'
	lsa_folder = '/Lsaed books'
	current_dir = os.getcwd()


	books = tool.get_books(books_folder)
	print 'Elegir libros: '
	books = tool.pick_books(books)

	for book in books:

		book_full_path = current_dir + books_folder + '/' + book
		where_to_save_data = current_dir + lsa_folder
		print where_to_save_data
		lsa.apply_lsa(book_full_path, book, where_to_save_data)



make_lsa_for_all_books()




