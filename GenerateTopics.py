#Definition:
#class gensim.models.ldamodel.LdaModel(corpus=None, num_topics=100, id2word=None, distributed=False, 
	#chunksize=2000, passes=1, update_every=1, alpha='symmetric', eta=None, decay=0.5, offset=1.0, eval_every=10, iterations=50, gamma_threshold=0.001)


'''
show_topics(num_topics=10, num_words=10, log=False, formatted=True)
'''
import sys,logging,gensim,bz2,codecs
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def main():
	if len(sys.argv) != 3:
		print ('usage: python GenerateTopics.py TrainingDict TrainingCorpora')
		sys.exit(1)
	corpus=gensim.corpora.MmCorpus(sys.argv[2])
	dictionary=gensim.corpora.Dictionary.load(sys.argv[1])
	from gensim import corpora,models,similarities
	model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=45,passes=8,iterations=80,chunksize=1000)
		#print(model)
	#model.print_topics(40)
	#print("**************************")
	model.show_topics(num_topics=45, num_words=6, log=True, formatted=True)
	#print(model[doc_bow]) # get topic probability distribution for a document
if __name__=="__main__":
	main()
