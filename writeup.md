# **Behavioral Cloning** 

---

**Behavioral Cloning Project**

The goals / steps of this project are the following:
* Use the simulator to collect data of good driving behavior
* Build, a convolution neural network in Keras that predicts steering angles from images
* Train and validate the model with a training and validation set
* Test that the model successfully drives around track one without leaving the road
* Summarize the results with a written report


[//]: # (Image References)

[image1]: ./examples/placeholder.png "Model Visualization"
[image2]: ./examples/placeholder.png "Grayscaling"
[image3]: ./examples/placeholder_small.png "Recovery Image"
[image4]: ./examples/placeholder_small.png "Recovery Image"
[image5]: ./examples/placeholder_small.png "Recovery Image"
[image6]: ./examples/placeholder_small.png "Normal Image"
[image7]: ./examples/placeholder_small.png "Flipped Image"

[imageM1]: ./write_up_material/dropout.0_5.png "Dropout at 0%, 5 epochs"
[imageM2]: ./write_up_material/dropout.0.1_5.png "Dropout at 10%, 5 epochs"
[imageM3]: ./write_up_material/dropout.0.2_5.png "Dropout at 20%, 5 epochs"
[imageM4]: ./write_up_material/model_architecture.PNG "Model architecture"
[imageM5]: ./write_up_material/track_2_stat.PNG "Train dataset statistic"

[imageDS1]: ./write_up_material/center.jpg "center image"
[imageDS2]: ./write_up_material/left_to_center_1.jpg "recover to center 1"
[imageDS3]: ./write_up_material/left_to_center_2.jpg "recover to center 2"
[imageDS4]: ./write_up_material/left_to_center_3.jpg "recover to center 3"
[imageDS5]: ./write_up_material/steering_angle_dist.PNG "steering angle statistic"
[imageDS6]: ./write_up_material/flip_before.jpg "Before flipping"
[imageDS7]: ./write_up_material/flip_after.jpg "After flipping"
[imageDS8]: ./write_up_material/train_set_angle_dist.PNG "train set steering angle statistic"

[imageR1]: ./write_up_material/input_image.png "input image"
[imageR2]: ./write_up_material/feature_map_1.png "feature map layer 1"
[imageR3]: ./write_up_material/feature_map_2.png "feature map layer 2"

## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/432/view) individually and describe how I addressed each point in my implementation.  

---
### Files Submitted & Code Quality

#### 1. Submission includes all required files and can be used to run the simulator in autonomous mode

My project includes the following files:
* model.py containing the script to create and train the model
* drive.py for driving the car in autonomous mode
* model.h5 containing a trained convolution neural network 
* writeup.md summarizing the results
* track1_forward.mp4 is the recording to the car driving on track 1 (forward) in autonomous mode using the model submitted
* track1_backward.mp4 is the recording to the car driving on track 1 (backward) in autonomous mode using the model submitted
* track2_forward.mp4 is the recording to the car driving on track 2 (forward) in autonomous mode using the model submitted
* track2_backward.mp4 is the recording to the car driving on track 2 (backward) in autonomous mode using the model submitted

#### 2. Submission includes functional code
Using the Udacity provided simulator and my drive.py file, the car can be driven autonomously around the track by executing 
```sh
python drive.py model.h5
```

#### 3. Submission code is usable and readable

The model.py file contains the code for training and saving the convolution neural network. The file shows the pipeline I used for training and validating the model, and it contains comments to explain how the code works.

### Model Architecture and Training Strategy

#### 1. An appropriate model architecture has been employed

My model consists of a convolution neural network with 5x5 and 3x3 filter sizes and depths between 24 and 64 (model.py lines 113-138) 

The model includes RELU layers to introduce nonlinearity, and the data is normalized in the model using a Keras lambda layer (code line 114). 

#### 2. Attempts to reduce overfitting in the model

I have tried to place dropout layers to the proposed model, but it turned out that it reduces the ability for the car to 
turn around sharp corners. so I have set the dropout ratio to 0 (model.py lines 111).
 
The model was trained and validated on the same dataset and split in the ratio of 8:2 to ensure that the model was not overfitting (code line 141). The model was tested by running it through the simulator and ensuring that the vehicle could stay on the track.

To avoid overfitting, the car is to drive the track in another direction, and the model could stay on the track in this setting.

#### 3. Model parameter tuning

The model used an Adam optimizer, so the learning rate was not tuned manually (model.py line 140).

#### 4. Appropriate training data

Training data was chosen to keep the vehicle driving on the road. I used a combination of center lane driving, recovering from the left and right sides of the road.

For details about how I created the training data, see the next section. 

### Model Architecture and Training Strategy

#### 1. Solution Design Approach

The overall strategy for deriving a model architecture was 

1. The speed of the car is control by a PI controller to keep the speed stable.

2. Captured image from the car is processed by convolution layers, and then 5 dense layers to make decision 
based on the features extracted by the convolution neural network and output a steering angle.


My first step was to use a convolution neural network model similar to the model proposed by Bojarski, M. in the article
"End to End Learning for Self-Driving Cars"[1]. I thought this model might be appropriate because it has been used by the 
research team to control a real car driving in New Jersey with little intercepts from humans.

In order to gauge how well the model was working, I split my image and steering angle data into a training and validation set. 
I found that my first model had a low mean squared error on the training set but a high mean squared error on the validation set. 
This implied that the model was overfitting. 

![alt text][imageM1]


To combat the overfitting, I modified the model so that dropout layers are added between the dense layer.

Then I train the model using dropout rate = 0.1 and dropout rate = 0.2, the validation score is more or less the same, while
 only the mean squared error of training set increasing. Here is the result.

![alt text][imageM2] ![alt text][imageM3]

The final step was to run the simulator to see how well the car was driving around track one. The car kept on the track all
the time. To increase the difficulty, the car was driving around track two. This time there were a few spots where 
the vehicle fell off the track, the car usually failed to drive around the curve. To improve the driving behavior 
in these cases, I perform the following actions:

1. Reduce the number of very low steering example in the training set, because the neural network may try to return a small
steering angle to reduce the mean squared error, which may cause the car fails to drive around a sharp curve.

2. I use a game steering wheel in the simulator to collect train dataset. On track 2, there are many curves which force me to 
slow down so that I can have enough reaction time to turn my steering wheel. (The steering wheel is 1.5 circle in each direction)
As a result, in the dataset, there are incorrect steering angles (too less or too much) for each image captured.
Imagine at speed of 0mph, you can steer the car to the left or right without falling off the track, but this may not be 
the desired steering angle and the neural network learn the incorrect information and make the wrong decision.
To fix this, I reduce the range of steering angle so that I can reduce my reaction time and drive on track 2 at > 25mph. 

![alt text][imageM5]

3. Decreasing the dropout ratio. It works and makes the car stay on track even on track 2.

At the end of the process, the vehicle is able to drive autonomously around the track without leaving the road.

#### 2. Final Model Architecture

The final model architecture (model.py lines 113-138) consisted of a convolution neural network with the following layers and layer sizes

| Layer         		|     Description	        					            | 
|:---------------------:|:---------------------------------------------------------:| 
| Input         		| 160,320,3 YCrCb image   				                    | 
| Cropping layer        | remove the top 70 rows and last 25 rows of the image, output 65x320x3	    | 
| Convolution 5x5     	| 2x2 stride, valid padding, outputs 31x158x24          	|
| RELU					|											            	|
| Convolution 5x5     	| 2x2 stride, valid padding, outputs 14x77x36            	|
| RELU					|											            	|
| Convolution 5x5     	| 2x2 stride, valid padding, outputs 5x37x48            	|
| RELU					|											            	|
| Convolution 3x3     	| 2x2 stride, valid padding, outputs 3x35x64            	|
| RELU					|											            	|
| Convolution 3x3     	| 2x2 stride, valid padding, outputs 1x32x64             	|
| RELU					|											            	|
| Flatten       	    | 1x32x64 -> 2048                               	            |
| Fully connected		| input 2048, output 1164, dropout rate 0.0                 |
| RELU					|											            	|
| Fully connected		| input 1164, output 100, dropout rate 0.0                  |
| RELU					|											            	|
| Fully connected		| input 100, output 50, dropout rate 0.0                  |
| RELU					|											            	|
| Fully connected		| input 50, output 10, dropout rate 0.0                  |
| RELU					|											            	|
| Fully connected		| input 10, output 1, dropout rate 0.0                  |


Here is a visualization of the architecture copy from [1] 

![alt text][imageM4]

#### 3. Creation of the Training Set & Training Process

To capture good driving behavior, I first recorded two laps on track one using center lane driving. Here is an example image of center lane driving:

![alt text][imageDS1]

I then recorded the vehicle recovering from the left side and right sides of the road back to center so that the vehicle 
would learn to drive back to center from left and right sides, These images show what a recovery looks like starting 
from left side to the center of the track :

![alt text][imageDS2]
![alt text][imageDS3]
![alt text][imageDS4]

Then I repeated this process on track two in order to get more data points.

To augment the data sat, I also flipped images and angles thinking that this would help the model not only to drive left but 
also right. 

Here are the statistics for the track 1 dataset driving anti-clockwise.

![alt text][imageDS5]
 
For example, here is an image that has then been flipped:

![alt text][imageDS6] ![alt text][imageDS7]


After the collection process, I had 55809 data points. I then preprocessed this data by removing more than half of the
data points which the steering angles are between [-0.05, 0.05], and here is the final train dataset steering angle distribution. 

![alt text][imageDS8]


I finally randomly shuffled the dataset and put 20% of the data into a validation set. 

I used this training data for training the model. The validation set helped determine if the model was over or underfitting. 
The ideal number of epochs was 5 as evidenced by the following graph, the validation error did slightly go up on epoch 5. 
I used an Adam optimizer so that manually training the learning rate wasn't necessary.

![alt text][imageM1]


## Result and conclusion
The model is then tested to run the track 1, and track 2 (both clockwise and counter-clockwise), The model excels in 
driving on those 4 settings without falling off the tracks.

For details, please see 

* track1_forward.mp4: Car in autonomous mode driving on track 1 counter-clockwise at 25mph
* track1_backward.mp4: Car in autonomous mode driving on track 1 counter-clockwise at 25mph
* track2_forward.mp4: Car in autonomous mode driving on track 2 counter-clockwise at 20mph
* track2_backward.mp4: Car in autonomous mode driving on track 2 counter-clockwise at 20mph

#### Internal CNN state

Below figures show the activations of the first two feature map layers for an example input

Example input image

![alt text][imageR1]

Feature map layers 1 and 2

![alt text][imageR2] 

![alt text][imageR3]


## Reference
[1] Bojarski, M., Testa, D. D., Dworakowski, D., Firner, B., Flepp, B., Goyal, P., Jackel, L. D., Monfort, M., Muller, U., Zhang, J., Zhang, X., Zhao, J. & Zieba, K. (2016). End to End Learning for Self-Driving Cars.. CoRR, abs/1604.07316. 
