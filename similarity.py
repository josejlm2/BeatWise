import csv, sys, datetime, time, math

f = open(sys.argv[1], 'rt')
g = open(sys.argv[2], 'rt')

a = []
b = []

h1 = []
h2 = []

def error(x, y): return (abs(x-y)/(max(x,y)))

def slope(x1, y1, x2, y2):
    return (y1 - y2) / (x1 - x2)

def average (s): return (sum(s) /len(s))
def std (s):
 z = []
 for r in s:
  z.append((r - average(s))**2)
 return math.sqrt(average(z))

def avgrate (s):
 n = 0.0
 for x in range(0,len(s)-2):
  n += abs(slope(s[x][0],s[x][1],s[x+1][0],s[x+1][1]))
 return (n/len(s))
 
try:
 reader = csv.reader(f)
 for row in reader:
  x = time.strptime(row[0],'%H:%M:%S')
  a.append ([datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds() , int(row[1])])
  h1.append(int(row[1]))
  
 reader2 = csv.reader(g)
 for row in reader2:
  x = time.strptime(row[0],'%H:%M:%S')
  b.append ([datetime.timedelta(hours=x.tm_hour,minutes=x.tm_min,seconds=x.tm_sec).total_seconds() , int(row[1])])
  h2.append(int(row[1]))
  avg = average(h1)

 print ("Average of first   : ", average(h1))
 print ("Average of Second  : ", average(h2))
 print ("Standard of first  : ", std(h1))
 print ("Standard of Second : ", std(h2))
 print ("Average Slope first: ", avgrate(a))
 print ("Average Slope first: ", avgrate(b))
 #adjust weights here!
 ascore = (1 - error(average(h1), average(h2)))
 bscore = (1 - error(std(h1), std(h2)))
 cscore = (1 - error(avgrate(a), avgrate(b)))
 
 print ("Mean Correlation           - ", ascore)
 print ("Stddev Correlation         - ", bscore)
 print ("Rate of Change Correlation - ", cscore)
 
 print ("Total Correlation Score    - ",(.5 * ascore + .2 * bscore + .3 * cscore))
 
  
finally:
 f.close()
 g.close()

# Similarity Factors
	# - Avg Heart Rate 50%
	# - Standard Deviation 20%
	# - Rate of Inclination 30&