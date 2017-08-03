def print_dictionary(dictionary):
	list_of_words = []
	for key in dictionary:
		list_of_words.append(key)
	
	list_of_words.sort()

	with open( "wordsused",'w') as f:
		for word in list_of_words:
			f.write(word+'\n')
