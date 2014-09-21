import csv
import tokenize 
import string
import re
from collections import Counter

csv.field_size_limit(1000000000)

with open('state-of-the-union.csv','rb') as myfile:
	filtered = (line.replace('\r', '') for line in myfile)
	reader = csv.reader(filtered)
	colnum = 2
	t=0
	token2 =""
	list1 =[]
	list2 = []
	dict = {}
	for row in reader:
		header = row[1]
		lines = str.splitlines(header)
		# print lines
		for line in lines:
			# print line
			value = line
			out = value.translate(None,'?.([]),:";-\'\n')
			out = out.lower()
			out = str.splitlines(out)

			for o in out:
				# out = str.splitlines(o)
				out = o.split(" ")
				for i in out:
					if i == '':
						continue
					else:
						count = Counter(i)
						list1.append(i)
						
	print list 
		


	


		