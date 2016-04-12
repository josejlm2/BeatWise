# BeatWise
The purpose of BeatWise is to build a digital classifier of a user using heartbeat data from a Fitbit Charge HR and images taken from a Narrative Clip. By overlaying a spike in heart rate with images of what occurred during the spike, the team plans on classifying future spikes into a positive or negative event.

###HearBeat Clustering

For this part of the algorithm, we need to split the data into activities, or clusters, so we can compare the signals and classify them. I guess this branch should be call heartbeat clustering instead but I didn't want to go through the trouble of renaming the branch. I used k-means to cluster similar points together and then printed out the times when the activity starts and when the activity ends. 

####Running the Algorithm 
To run the code, simply type the following line of code into python command prompt where the code is located:
   
```
python heartbeatClassifier.py data
```

This will basically read the files from the data folder, represent the information as points, put them in a dictionary, then cluster similar activities using k-means, and finally output the results. 


