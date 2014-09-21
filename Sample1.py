import csv
import tokenize 
import string
import math
from collections import Counter, defaultdict

csv.field_size_limit(1000000000)

def tf ()
with open('state-of-the-union.csv','rb') as csvfile:
	reader = csv.reader(csvfile)
	list1 = []
	document = []
	tf_document_list = []
	documents = []
	dict_single ={}
	s =set()
	st=[]

	
	count_copy1={}
	dict_whole = {}
	normal_vector = {}
	j = 0
	total = 0
	total1 = 0
	num_of_docs= 0

	for row in reader:
		lines = row[1]
		lines = lines.translate(None,'!@#$%^&*()-_,.?":;\'')
		lines = lines.lower()
		lines  = str.splitlines(lines)
		
		# for line in lines:
			Speech(lines)
			line = line.split(" ")
			# print line
			for l in line:
				if l == '':
					continue
				else:
					list1.append(l)
					#  Creating a master list with all the words
					documents.append(l)
					Speech
		# Creating the tf vectors of each document
		document.append(list1)
		term_frequency = Counter(list1) #Calculating the Term Frequency (TF)
		copy_term_frequency = term_frequency;
		print copy_term_frequency

		for key,value in term_frequency.items(): #For normalisation
			# total+=value
			total+= value*value
		for key,value in term_frequency.items():
			copy_term_frequency[key] = value/total #I don't want to mess with the original term_frequency list
		
		# a = list(count)
		tf_document_list.append(term_frequency) #Appending the term frequencues of each document into a list 'd'
		# d_copy = dict(d)
		# count_copy1.update(count_copy)
		
		# Finding the Document Frequency (DF)

	
	s = set (list1) #Converting the list  to a set to eliminate duplication
		print s

		for i in s:
			st.append(i) #Creating a new list of the terms from the set
		j+=1
		num_of_docs+=1
		# To start over - making the list none
		list1 = []
	#Counting the words in each document for calculating the Document Frequency DF	
	count = Counter(st)
	dict_single.update(count)

	for key, value in dict_single.items():
		dict_single[key] = (math.log10(num_of_docs/value))
	# print count_copy1

	# print d
	total2 = 0

# 	# print len(dict_single)
# 	for value in d:
# 		s = dict(value)
# 		# print len(s)
# 		for key1,value1 in s.items():
# 			for key2,value2 in dict_single.items():
# 				if key1 == key2:
# 					value1 = value1 * value2
# 					total2 += value1*value1
# 					break
# 					# print value2
# 		for key1,value1 in s.items():
# 			value1 = value1/math.sqrt(total2)
# 		total2 = 0
# 		value = s

# print d
			
	


		

	
	# for key1, value1 in d.items():
	# 	# print value1
	# 	# p_list = value1s
	# 	# sprint p_list
	# 	for value in value1:
	# 		# print value
	# 		for key  in value:
	# 			print key
	# 		# print value
	# 			for key2, value2 in dict_single.items():
	# 				# print value2
	# 				if key == value2:
	# 					key = key * value2
						# print val
		# value1 = p_list
	# print p_list

	



	# The number of occurences of each word in all the documents combined
	# count = Counter(documents)
	# dict_whole.update(count)
# for i in document:
	# for j in range(i,10):
		# if s 
	# print d[2]
			
