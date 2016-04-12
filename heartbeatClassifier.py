import sys, operator, glob, os, re, math, csv, datetime, random, math
from collections import OrderedDict
from datetime import datetime


class Cluster:
    def __init__(self, name, center, pointList):
        self.name = name
        self.center = center
        self.pointList = pointList

		
def random_centroid(minTime, maxTime, minBeat, maxBeat):
		randomTime = random.randrange(minTime, maxTime)
		randomBeat = random.randrange(minBeat, maxBeat)
		return [randomTime, randomBeat]
		
def avg_centroid (pointList):
	x = 0
	y = 0 
	for point in pointList:
		x += point[0]
		y += point[1]
		
	total = len(pointList)
	return [ x / total, y / total]


	
#read the file; return a string
def read_file(file):
	f = open(file, 'r')
	a = f.read()
	return a

	
def euclidean_distance (A, B):
	x1 = list(A)[0]
	y1 = list(A)[1]
	x2 = list(B)[0]
	y2 = list(B)[1]

	#return math.sqrt( (A[0]-B[0])**2 + (A[1]-B[1])**2 )
	return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
	

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r
	
#create dictionary with cvs data
def test(foldername, clusters, precision):
	FMT = '%H:%M:%S'
	os.chdir(foldername)	
	
	a = []
	for file in glob.glob("*.txt"):
		list = read_file(file)
		a = re.split('\s', list)
	
	o_dict = OrderedDict()
	dict = {}
	beatList = []
	timeList = []
	for line in a:
		b = re.split('[,]', line)
		#print b
		
		if len(b) == 2:
			
			timeList.append(b[0])
			beatList.append(int(b[1]))
			dict[b[0]] = b[1]			
			tdelta  = datetime.strptime(b[0], FMT) - datetime.strptime("00:00:00", FMT)
			#o_dict[b[0]] = int(b[1])
			o_dict[tdelta.seconds] = int(b[1])
	

	#get the max and mins of the data 
	maxTime = max(o_dict.keys(), key=int)
	minTime = min(o_dict.keys(), key=int)
	maxBeat = o_dict[max(o_dict, key=o_dict.get)]
	minBeat = o_dict[min(o_dict, key=o_dict.get)]
	
	
	#initialize clusterList
	k = clusters
	clusterList = [] 
	
	
	#for cluster in clusterList:	
	for num in range(0,k):
		#pick a random center
		randomTime = random.randrange(minTime, maxTime)
		randomBeat = random.randrange(minBeat, maxBeat)
		clusterList.append(Cluster(num,{randomTime, randomBeat},[]))
		print "Cluster%d with center (%d, %d)" % (num, randomTime, randomBeat)		
		
	print ""
	print "Forming Clusters..."
	

	print ""
	print ""
	
	
	
	
	for numb in range(1,precision + 1):
		
		for point in o_dict.items():
			
			closest = 0
			distance = 100000
			
			for index, cluster in enumerate(clusterList):
				
				if distance > euclidean_distance(cluster.center, point):
					distance = euclidean_distance(cluster.center, point)
					closest = index

			clusterList[closest].pointList.append(point)
		
		print "ITERATION %d " % numb
		for a in range(0,clusters):
			if not clusterList[a].pointList:
				clusterList[a].center = random_centroid(minTime, maxTime, minBeat, maxBeat)
				print "Bad centroid"
			else:
				print "Activity[%d]: %s to %s " % ( len(clusterList[a].pointList), min(clusterList[a].pointList)[0], max(clusterList[a].pointList)[0] ) 
				clusterList[a].center = avg_centroid(clusterList[a].pointList)
				clusterList[a].pointList = []
		
		print ""
		print ""
	
	return 0
	
# main function 
# run code by 
# python heartbeatClassifier.py data
def main():
	if len(sys.argv) != 4:
		print 'usage: ./heartbeatClassifier.py foldername k precision'
		sys.exit(1)
  
	
	foldername = sys.argv[1]
	clusters = int(sys.argv[2])
	precision = int(sys.argv[3])
	test(foldername, clusters, precision)
	

if __name__ == '__main__':
	main()