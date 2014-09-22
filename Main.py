import csv
import tokenize 
import string
import math
from collections import Counter, defaultdict
from word import make_document, Document, calculate_term_frequency, calculate_document_frequency,calculate_tfidf
from sets import Set

csv.field_size_limit(1000000000)


with open('state-of-the-union.csv','rb') as csvfile:
	reader = csv.reader(csvfile)
	list1=[]
	document_list=[]
	num_of_doc = 0
	term_frequency=[]
	document_word =Set()
	document_term_frequency=[]
	document_frequency= {}
	d_f=[]

	word_tfidf={}
	tfidf = []
	document_tfidf=[]
	value=0
	for row in reader:
		num_of_doc+=1;
		lines = row[1]
		lines = lines.translate(None,'!@#$%^&*()-_,.?":;\'')
		lines = lines.lower()
		lines  = str.splitlines(lines)
		list1=[]
		for line in lines:
			line = line.split(" ")
			for l in line:
				if l == '':
					continue
				else:
					list1.append(l) #Returns the list of words in the document 'row'

		#Creating a new documents			
		Document1 =  Document(num_of_doc,row[0],list1) 

		#Creating a list of all the documents and words
		document_list.append(Document1)
	
	#Finding the Term Frequency of each word in each document
	for list in document_list:
		freq = calculate_term_frequency(list.words)
		term_frequency.append(freq)

	#Finding the Document Frequency of each word
	for list in document_list:
		for word in list.words:
					value = calculate_document_frequency(word, document_list,num_of_doc,document_word)
					if value != "-1":
						document_word.add(word)
						document_frequency.update({word: float(value)})
	

	#Calculating tfidf
	for list in term_frequency:
		word_tfidf={}
		for word, count in list.items():
			word_tfidf.update({word: float(calculate_tfidf(word,count,document_frequency))})
		document_tfidf.append(word_tfidf)

	#Normalising the tf vectors
	for list in document_tfidf:
		total=0
		for key,value in list.items():
			total += value*value
		for key,value in list.items():
			list[key] = value/math.sqrt(total)

	#Displaying the first 20 words
	text_file = open("Results.txt","w")
	i=0
	for list in document_tfidf:
		i+=1
		# text_file.write("Document : %s\n\n",i) 
	 	sorted_words = sorted(list.items(), key=lambda x: x[1], reverse=True)
	 	for word, score in sorted_words[:20]:
	 		text_file.write("\tWord: {}, TF-IDF: {}\n".format(word, round(score, 3)))
	 	text_file.write("\n\n")
	text_file.close()
