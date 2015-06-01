# Code for generating trainig file from the corpus of documents
#Each line in the trainig file corresponds to 1 document in the corpus


import os
import re
import codecs

def main():
	## create training file which contains 1 document per line
	with codecs.open('training.txt','w')as outputfile:
		##mtsample contains all the training files
		directory='mtsample'
		##find all files in that directory
		for root,dirs,files in os.walk(directory):
		##open individual file and paste contents
			for f in files:	
				##Open the file
				ip=root+"/"+f
				with open(ip,'r')as inputfile:
					line=inputfile.read()
					line=line.replace("\n"," ") ##replace new line with space
					outputfile.write(line) ##write to output file
					inputfile.closed	
					outputfile.write("\n")
	outputfile.closed	
	return
	
if __name__=="__main__":
	main()
