from collections import Counter
import math

class word(object):
	def __init__(self, string):
		self.string = string

class Document(object):
	def __init__(self,id,year,words):
		self.id = id
		self.year = year
		self.words = words

def make_document(id, year, words):
	document1 = Document(id, year, words)
	return document1

def calculate_term_frequency(doc):
	count = Counter(doc)
	return count

def calculate_document_frequency(word,Document_list,num_of_doc,document_word):
	count=0
	if word not in document_word:
		count = sum(1 for list in Document_list if word in list.words)
		val = '{0:.3f}'.format(math.log(num_of_doc/count))
		return val
	else:
		return "-1"	

def calculate_tfidf(word,count,document_frequency):
	value = document_frequency.get(word)
	tfidf = value *count
	return tfidf


