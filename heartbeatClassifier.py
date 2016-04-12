import sys, operator, glob, os, re, math, csv, datetime, random, math
from collections import OrderedDict
from datetime import datetime


class Cluster:
    def __init__(self, center, pointList):
        self.name = ""
        self.center = center
        self.pointList = pointList

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
def test(foldername, clusters):
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
	
	#print maxTime
	#print minTime
	#print maxBeat
	#print minBeat
	
	
	#initialize clusterList
	k = clusters
	i = 1
	clusterList = [] 
	
	#make a copy
	points = OrderedDict()
	points = o_dict
	
	i = 1
	#for cluster in clusterList:	
	for num in range(1,k+1):
		#pick a random center
		randomTime = random.randrange(minTime, maxTime)
		randomBeat = random.randrange(minBeat, maxBeat)
		
		cluster = Cluster([],[])
		cluster.name = i
		cluster.center = {randomTime, randomBeat}
		cluster.pointList = []
		print "Cluster%d with center (%d, %d)" % (i, randomTime, randomBeat)
		i += 1
		clusterList.append(cluster)
	
	
	
	
	
	print ""
	print "Forming Clusters..."
	

	print ""
	print ""
	print "Give it a second...."
	
	
	while (len(points) > 0):
		for cluster in clusterList:	
			distance = 100000
			center = cluster.center
			closest = [0,0]
			for point in points.items():
				if distance > euclidean_distance(center, point):
					distance = euclidean_distance(center, point)
					closest = point
			
			cluster.pointList.append(closest)	
			
			if not closest:
				break
			else:
				del points[closest[0]]
			
			
			#print "Cluster%s" % cluster.name
			#print "Closest Point:"
			#print closest
			#print "size %d" % len(points)
			

	
	
	print "Clustering Complete"
	
	for cluster in clusterList:
		#print len(cluster.pointList)
		print "Activity: %s to %s " % (min(cluster.pointList), max(cluster.pointList) )
	
	return 0
	
# main function 
# run code by 
# python heartbeatClassifier.py data
def main():
	if len(sys.argv) != 3:
		print 'usage: ./heartbeatClassifier.py foldername k'
		sys.exit(1)
  
	
	foldername = sys.argv[1]
	clusters = int(sys.argv[2])
	test(foldername, clusters)
	

if __name__ == '__main__':
	main()