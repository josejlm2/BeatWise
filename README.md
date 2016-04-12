# BeatWise
The purpose of BeatWise is to build a digital classifier of a user using heartbeat data from a Fitbit Charge HR and images taken from a Narrative Clip. By overlaying a spike in heart rate with images of what occurred during the spike, the team plans on classifying future spikes into a positive or negative event.


### Signal Comparison

Our initial comparison tool will use a weighted sum of three components; average heart rate, standard deviation, and rate of change. These factors were chosen for their time independance, so that we could compare activities of different lengths. We will continue to test the factors to determine the best weighting between them. It might be possible that we may need to out put three seperate similarity scores, so that we can take all three into consideration when classifying data.

Essentail Flow:
Two CSV files are specified at runtime and will be the segements of data being compared. The each file is parsed into a vector consisting of all the data points specified. The Scores are then calculated and combined to be returned to the classifier.
