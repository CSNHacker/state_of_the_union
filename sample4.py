import csv
import tokenize 
import string
import math
from collections import Counter, defaultdict
from word import make_document, Document, calculate_term_frequency, calculate_document_frequency
from sets import Set

csv.field_size_limit(1000000000)


with open('state-of-the-union.csv','rb') as csvfile:
	reader = csv.reader(csvfile)
	list1=[]
	document_list=[]
	num_of_doc = 0
	term_frequency=[]
	document_term_frequency=[]
	document_frequency= Set()

	word_tfidf=[]
	document_tfidf=[]

	for row in reader:
		num_of_doc+=1;
		lines = row[1]
		lines = lines.translate(None,'!@#$%^&*()-_,.?":;\'')
		lines = lines.lower()
		lines  = str.splitlines(lines)
		
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
			for word in list.words:
				term_frequency.append([word,calculate_term_frequency(word,list)])
			document_term_frequency.append(term_frequency)
			term_frequency=[]

	#Finding the Document Frequency of each word
	for list in document_list:
		for word in list.words:
			document_frequency.add(calculate_document_frequency(word, document_list,num_of_doc))

	print document_frequency

	for list in document_term_frequency:
		for word,count in list:
			word_tfdif.append([word,calculate_tfidf(word,list,count, document_frequency)])
	document_tfidf.append(word_tfidf)
