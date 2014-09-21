# from __future__ import division, unicode_literals
import math
import csv
import tokenize 
import string
from collections import Counter, defaultdict

from textblob import TextBlob as tb

csv.field_size_limit(1000000000)


def tf(word, blob):
	return blob.words.count(word)/math.sqrt(len(blob))

def n_containing(word, bloblist):
	return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
	return math.log10(len(bloblist) / (n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
	return tf(word,blob)*idf(word, bloblist)

# def idf1(word,blob,bloblist,num_of_blobs):
# 	count=0;
# 	for blob in bloblist:
# 		if word in blob:
# 			count+=1
# 	dict.update(word,math.log10(num_of_blobs/count))

# def tf1(word,blob):
# 	total = base(blob)
# 	freq.update(word,blob.words.count(word)/math.sqrt(len(blob.length))



# def tfidf1(word,blob,bloblist):
# 	c = dict.get(word);
# 	return tf(word,blob)

with open('state-of-the-union.csv','rb') as csvfile:
	reader = csv.reader(csvfile)
	bloblist=[]
	a = ""
	i=0
	length =0
	for row in reader:
		i+=1
		lines = row[1]
		lines = lines.translate(None,'!@#$%^&*()-_,.?":;\'')
		lines = lines.lower()
		lines = lines.strip('\n')
		lines = str.splitlines(lines)
		for line in lines:
			a += " "+line
		bloblist.append(tb(a))
		a=""
	length = i

text_file = open("Results.txt","w")
num_of_blobs = len(bloblist)
for i, blob in enumerate(bloblist):
	print("Top words in document {}\n".format(i + 1))
	text_file.write("Top words in document {}\n".format(i + 1))
	# for word in blob.words:
	# 	idf1(word,blob,bloblist,num_of_blobs)
	scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
	sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
	
	for word, score in sorted_words[:20]:
		text_file.write("Word: {}, TF-IDF: {} \n".format(word, round(score, 5)))
text_file.close()
print "The program has terminated"

