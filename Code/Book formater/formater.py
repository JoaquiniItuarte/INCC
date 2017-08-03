import stemming.porter2 #Para "normalizar" palabras
import pickle #Para guardar objetos
from string import maketrans #Para limpiar los strings de puntuaciones


#String con todos los simbolos que se sacan del texto
def get_punctuation_list():
	return '.,!?:-();'

	
#Obtener todas las stopwords
def get_stopwords():
	stopwords = []
	file_name = "stopwords.txt"
	with open( file_name,'r') as f:
		for line in f:
			stopwords.append( line.split() )
	
	return stopwords


#Elimina las palabras sin sentido: articulos, proposiciones y esas cosas
def remove_stopwords_from_string(list_str, stopwords):
	return [word for word in list_str if word not in stopwords ]


#"Normaliza" las palabras: las transforma en su palabra raiz
def word_rooter(str):
	return [stemming.porter2.stem(word) for word in str]


#Pone todo el string en minusculas
def lowercaser(str):
	return str.lower()


#Saco todos los simbolos de las palabras
def clean_punctuation_from_list_of_words(list_of_words, punctuation_list):
	list = [ word.strip(punctuation_list) for word in list_of_words ]
	return list


def clean_punctuation_from_string(str, punctuation_list):
	intab = ""
	outtab = ""
	trantab = maketrans(intab, outtab)
	str2 = str.translate(trantab, punctuation_list)
	return str2


#Rootea y pone todo el string en minusculas
def paragraph_normalizer(str, stopwords, punctuation_list):
	str2 = lowercaser(str)
	str2 = clean_punctuation_from_string(str2, punctuation_list)
	list_str = str2.split()
	list_str = remove_stopwords_from_string(list_str, stopwords)
	list_str = word_rooter(list_str)
	return list_str


#Formateo el libro directamente. Book es el path del libro
def formateo_libro(book):
	list_of_paragraph = []
	stopwords = get_stopwords()
	with open(book,'r') as f:
		list_of_paragraph = [paragraph_normalizer(line, stopwords, get_punctuation_list() ) for line in f]

	return list_of_paragraph


#Guardo el libro en formato pickle
def guardar_libro_formateado(list_of_paragraph, file_name):
	pickle.dump( list_of_paragraph, open( file_name, "wb" ) )


	
'''
	#Guardo el libro formateado en txt para ya no tener que hacerlo de nuevo
	def guardar_libro_formateado(list_of_paragraph, file_name):
		with open(file_name,'w') as f:
			for par in list_of_paragraph:
				guardar_parrafo_formateado(par, f)


	#Guardo el parrafo en el txt
	def guardar_parrafo_formateado(paragraph, file):
		str = ''
		for word in paragraph:
			str = str + ' ' + word
		file.write(str + '\n')
'''



