import sys, operator, glob, os, re, math, csv, datetime, random, math, time, json
from collections import OrderedDict
from datetime import datetime
from math import floor

class Cluster:
    def __init__(self, name, center, pointList):
        self.name = name
        self.center = center
        self.pointList = pointList

		
def random_centroid(minTime, maxTime, minBeat, maxBeat):
		randomTime = random.randrange(int(minTime), int(maxTime))
		randomBeat = random.randrange(int(minBeat), int(maxBeat) + 1) if int(maxBeat) == int(minBeat) else random.randrange(int(minBeat), int(maxBeat))
		return [randomTime, randomBeat]
		
		
def avg_centroid (pointList):
	x = 0
	y = 0 
	for point in pointList:
		x += point[0]
		y += point[1]
		
	total = len(pointList)
	return [ x / total, y / total]
	

def floored_percentage(val, digits):
    val *= 10 ** (digits + 2)
    return '{1:.{0}f}%'.format(digits, floor(val) / 10 ** digits)


	
#read the file; return a string
def read_file(file):
	f = open(file, 'r')
	a = f.read()
	return a


#read example json file from directory
def read_json(file):
	with open(file) as json_data:
		d = json.load(json_data)
		json_data.close()
	
	return d['activities-heart-intraday']['dataset']

	
def euclidean_distance (A, B):
	x1 = list(A)[0]
	y1 = list(A)[1]
	x2 = list(B)[0]
	y2 = list(B)[1]

	return math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
	

#create dictionary with cvs data
def test(foldername, clusters, precision):
	
	#change directory where data is located
	os.chdir(foldername)	
	
	#initialize variables
	FMT = '%H:%M:%S'
	o_dict = OrderedDict()
	o_dict2 = OrderedDict()
	beatList = []
	timeList = []
	
	#read json data
	data = read_json('March28.json')

	#populate heartbeat, time, and ordered dictionary
	for heartbeat in data:
		tdelta  = datetime.strptime(heartbeat.get('time'), FMT) - datetime.strptime("00:00:00", FMT)
		timeList.append(tdelta.seconds)
		
		beatList.append(float(heartbeat.get('value')))
		
		o_dict[tdelta.seconds] = int(heartbeat.get('value'))
		o_dict2[heartbeat.get('time')] = int(heartbeat.get('value'))
		


		
	#populate dictionary based on rate of change
	i = 0
	for index,val in o_dict.items():
		
		val = beatList[i] - beatList[i-1] / timeList[i] - timeList[i-1]
		beats = beatList[i] - beatList[i-1]
		times = float(timeList[i]) - float(timeList[i-1])
		o_dict[index] =  beats / float(times)		
		i += 1
		
	o_dict[timeList[0]] = 0
		
		
	#debuggin
	#for point,val in o_dict.items():
	#	print val
	

	
	#get the max and mins of the data 
	maxTime = max(o_dict.keys(), key=int)
	minTime = min(o_dict.keys(), key=int)
	maxBeat = o_dict[max(o_dict, key=o_dict.get)]
	minBeat = o_dict[min(o_dict, key=o_dict.get)]
	total   = len(o_dict)
	

	
	#initialize clusterList
	k = clusters
	clusterList = [] 
	
	

	
	#for cluster in clusterList:	
	for num in range(0,k):
		#pick a random center
		randomTime = random.randrange(int(minTime), int(maxTime))
		randomBeat = random.randrange(int(minBeat), int(maxBeat) + 1) if int(maxBeat) == int(minBeat) else random.randrange(int(minBeat), int(maxBeat)) 
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
		
		
		b = []
		
		for a in range(0,clusters):
			if not clusterList[a].pointList:
				clusterList[a].center = random_centroid(minTime, maxTime, minBeat, maxBeat)
				print "Bad centroid"
			else:
				#print "Activity[%d]: %s to %s " % ( len(clusterList[a].pointList), min(clusterList[a].pointList)[0], max(clusterList[a].pointList)[0] ) 
				b.append((int(min(clusterList[a].pointList)[0]), int(max(clusterList[a].pointList)[0]) , len(clusterList[a].pointList)) )
				clusterList[a].center = avg_centroid(clusterList[a].pointList)
				clusterList[a].pointList = []
		
		print "ITERATION %d " % numb
		results =  sorted(b, key=lambda activity: activity[0])
		print results
		
		
		
		#export results to json file
		
		result = []
		for activity in results:

			start = time.strftime("%H:%M:%S", time.gmtime(int(activity[0])))
			end = time.strftime("%H:%M:%S", time.gmtime(int(activity[1])))
			
			test = False 
			dict = {}
			for point,val in o_dict2.items():
				
				if start == point:
					test = True
					
				if test:
					dict[point] = val
					
				if end == point:
					test = False
			
			result.append(dict)
			
		with open('results.json', 'w') as outfile:
			json.dump(result, outfile)
					
		print ""
		print ""
		print "see results.json for json clusters"
	
	return 0
	
# main function 
# run code by 
# python heartbeatClassifier.py data 5 10
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