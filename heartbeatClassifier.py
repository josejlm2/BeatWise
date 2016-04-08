import sys, operator, glob, os, re, math, csv

#read the file; return a string
def read_file(file):
	f = open(file, 'r')
	a = f.read()
	return a

def split_words(string):
	s_string = re.split('\s|\d|\W|[_*]',string)
	filtered_s_string = filter(None, s_string)
	return filtered_s_string

	
#create dictionary with cvs data
def test(foldername):
	os.chdir(foldername)	
	list = ""
	a = []
	for file in glob.glob("*.txt"):
		
		list = read_file(file)
		a = re.split('\s', list)
	
	dict = {}
	for line in a:
		b = re.split('[,]', line)
		#print b
		
		if len(b) == 2:
			dict[b[0]] = b[1]
	
	#print dict
	return 0
	
# main function 
# run code by 
# python heartbeatClassifier.py data
def main():
	if len(sys.argv) != 2:
		print 'usage: ./heartbeatClassifier.py foldername'
		sys.exit(1)
  
	
	foldername = sys.argv[1]
	test(foldername)
	
	#with open('data/March28.csv', 'rb') as csvfile:
	#	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	#	for row in spamreader:
	#		print ', '.join(row)
	
	#query = sys.argv[2]
	#top_five_scores(foldername, query)

if __name__ == '__main__':
	main()