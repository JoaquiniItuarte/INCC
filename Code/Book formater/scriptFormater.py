#Importo las funciones
import formater


def analize_one_book(book):

	list_of_paragraph = formater.formateo_libro( book )
	#print(list_of_paragraph)
	formater.guardar_libro_formateado( list_of_paragraph, book + '_formateado.txt' )
	print('termine el libro')
	print(book)



books = [ 'libro1.txt', 'libro2.txt']

for book in books:
	analize_one_book(libro1)

