# BeatWise
The purpose of BeatWise is to build a digital classifier of a user using heartbeat data from a Fitbit Charge HR and images taken from a Narrative Clip. By overlaying a spike in heart rate with images of what occurred during the spike, the team plans on classifying future spikes into a positive or negative event.

###HearBeat Clustering

For this part of the algorithm, we need to split the data into activities, or clusters, so we can compare the signals and classify them. I guess this branch should be call heartbeat clustering instead but I didn't want to go through the trouble of renaming the branch. I used k-means to cluster similar points together and then printed out the times when the activity starts and when the activity ends. 

####Running the Algorithm 
To run the code, simply type the following line of code into python command prompt where the code is located:
   
```
DEFAULT: 
python heartbeatClassifier.py foldername k precision

EXAMPLE:
python heartbeatClassifier.py data 5 5
```

 > Foldername is the folder where the test data is located which in this repository is called data, k is the number of clusters, and precision is the number of iterations you want the algorithm to do. 

This will basically read the files from the data folder, represent the information as points, put them in a dictionary, then cluster similar activities using k-means, and finally output the results. 



### Signal Comparison

Our initial comparison tool will use a weighted sum of three components; average heart rate, standard deviation, and rate of change. These factors were chosen for their time independance, so that we could compare activities of different lengths. We will continue to test the factors to determine the best weighting between them. It might be possible that we may need to out put three seperate similarity scores, so that we can take all three into consideration when classifying data.

Essentail Flow:
Two CSV files are specified at runtime and will be the segements of data being compared. The each file is parsed into a vector consisting of all the data points specified. The Scores are then calculated and combined to be returned to the classifier.
