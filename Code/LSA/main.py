import lsa
import printDic
import loadSaveLsaData

apply_lsa = lsa.apply_lsa

#Los libros son los nombres del libro y despues se encarga solo de buscar el libro ya formateado.
#Escribir la ruta del libro, asegurarse que el libro fue formateado, y luego ejecutar esta funcion



libro1 = '../Books/Alice in wonderland _ Lewis Carroll.txt'
libro2 = '../Books/Factotum.txt'
libro3 = '../Books/Ham on rye.txt'
libro4 = '../Books/Post Office.txt'
libro5 = '../Books/South of No North  Stories of the Buried Life.txt'
libro6 = '../Books/women.txt'


apply_lsa(libro1, 300)
apply_lsa(libro2, 300)
apply_lsa(libro3, 300)
apply_lsa(libro4, 300)
apply_lsa(libro5, 300)
apply_lsa(libro6, 300)


