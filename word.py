from collections import Counter

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

def calculate_term_frequency(document):
	count = Counter(document)
	return count

def calculate_document_frequency(word,Document_list,num_of_doc):
	count =0
	for list in Document_list:
		if word in list.words:
			count+=1
	return math.log10(num_of_doc/count)

def calculate_tfidf(word,count,document_frequency):
	value = document_frequency.get(word)
	tfidf = value*count
	return tfidf



