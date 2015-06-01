#Training file with a document per line is the first input .
#The corresponding dictionary and corpus for LDA is the output
#To see logging events
import sys,logging,gensim,bz2,codecs
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

from gensim import corpora,models,similarities
from collections import defaultdict

def vector(dictionary):
		for line in open(sys.argv[1]):
			yield dictionary.doc2bow(line.lower().split())

# load one vector into memory at a time and print it
#def print_corpus(corpus):
	#for vector in corpus: 
		#print(vector)

def main():
	if len(sys.argv) != 2:
		print ('usage: python TrainingFileToVector.py Training_InputFile')
		sys.exit(1)
	stoplistfile=open('E:\project\code\scripts\stopwords.txt',"r")
	documents=list()
	ip= open(sys.argv[1],'rb')
	for lines in ip.readlines():
		line=lines.decode(encoding='utf-8', errors='ignore')
		documents.append(line)
	stoplist = set()
	#stoplist=ip.read().splitlines()
	for stopword in stoplistfile:
		stopword=stopword[:-1]
		stoplist.add(stopword)
	print(len(stoplist))
	print(stoplist)
	texts=[[word for word in document.lower().split() if word not in stoplist]
		for document in documents]
	# remove words that appear only once

	frequency = defaultdict(int)
 	for text in texts:
 		for token in text:
 			frequency[token] += 1

	texts = [[token for token in text if frequency[token] > 1]
			for text in texts]

	dictionary = corpora.Dictionary(texts)
	
	dictionary.save('E:\project\code\scripts\Training.dict') 
# store the dictionary, for future reference
	#print(dictionary.token2id)

	corpus = [dictionary.doc2bow(text) for text in texts]
	corpora.MmCorpus.serialize('E:\project\code\scripts\Training.mm', corpus) # store to disk, for later use
	#print(corpus)
	
	print("***openend file successfully**")
	#dictionary = corpora.Dictionary(line.lower().split() for line in ip )
	
	#corpus = vector(dictionary)
	#print_corpus(corpus)


if __name__=="__main__":
	main()