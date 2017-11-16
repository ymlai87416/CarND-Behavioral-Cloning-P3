# Self-driving - Behavior cloning P3 train set editor

[//]: # (Image References)

[image1]: ./screenshots/Copy_data.png "Folk data points"
[image2]: ./screenshots/Remove_data.png "remove data points"
[image3]: ./screenshots/statistic.PNG "show train set steering statistics"
[image4]: ./screenshots/Utilities.png "Utilities screen"

## Background
Collecting data from the simulator is quite difficult because you have to focus on driving 2 to 3 perfect laps.
This editor helps you to remove unwanted data point in your dataset so that you don't have to drive again to get the desired data set.

## What can it do?
* Folk datapoint from one dataset to another (append at the end of the destination data set)
* Remove unwanted data points
* Fix image link
* and show you statistics on the steering across the dataset

## Screenshot 

To choose a source train set and destination train set, please click the "..." button to select the directory in the prompt dialog.

Specify the portion of source train set to be copied by using the sliding bars. (Start position & end position)

![alt text][image1]


Specify the portion of source train set to be removed by using the sliding bars. (Start position & end position)

![alt text][image2]


Here you can find the steering statistic of your training set, so you can think of how to process your dataset before feeding it to the neural network.
![alt text][image3]


You can also fix image link here if you copy dataset to another folder.
![alt text][image4]


## Support 
I hope this script helps you to understand the train dataset data more and give you insight on how to improve the dataset. If you find it hard to use, feel free to modify it to your heart's content.

@Copyleft by Tom, Nov 2017.