### Title

* Pytorch GCP Colab Deep Learning Model for Driver's License Detection using GPU (CUDA)

### About / Synopsis

* The purpose of this project is to demonstrate the ability to set up a neural network using Pytorch within an IPython notebook in GCP Colaboratory that ingests a set of mock images of US driver's licenses and attempts to identify the US state to which the corresponding license is associated to. The neural network is run on both CPU and a free CUDA GPU available in GCP Colaboratory. This is a multi-class classification problem.

### Detailed Description 

* This Colaboratory notebook available as both a Python file (.py) or as a IPython notebook (.ipynb)

* 50 mock driver's license images were downloaded from the Internet and flattened to be of the same pixel size (450x450) using the Python_Image_Flattener_Pillow.py file. 27 images were loaded as the training dataset.

  * Training Data:
  
  ![image](https://user-images.githubusercontent.com/46364751/180013560-4cc2e317-73e1-4c1c-8ad4-ea89e810c7de.png)

  * Test Data:
  
  ![image](https://user-images.githubusercontent.com/46364751/180014062-b610ae4e-250c-4cf1-a05b-d8db2a534683.png)


* 5 classes (US states) have been set up for the neural network to classify the unstructured data i.e. images
	* California
	* Virginia
	* Alabama
	* Massachusetts
	* Other (i.e. all other US states)

* A labels file is included for labeling the training and allowing the neural network to learn

* Relevant Python libraries including Pytorch (torch), Torchvision and Pillow (PIL) are loaded into the GCP Colaboratory notebook along with allocation of resources to perform computing operations

![image](https://user-images.githubusercontent.com/46364751/180016456-32c06e70-26cc-4f19-a3a2-d40aa87909d0.png)

* At first, with a small image dataset of 20 images, upon completion of the first neural network run, it has a large error rate and is incorrectly classifying test images

![image](https://user-images.githubusercontent.com/46364751/180016004-c1dbc70e-b51c-4da7-aad1-af6c3d1d75be.png)


* After increasing the training image dataset, conducting more on the neural network and adjusting epochs, the model begins to improve its classification. 

	* The example below is when the neural network, at first, incorrecly identifies a West Virginia ID as a Virginia ID. 
	
	![image](https://user-images.githubusercontent.com/46364751/180016318-78903d77-9d05-4c7f-891d-03fbf2d25987.png)

	
	* Upon more training images being loaded to increase the sample size to 50, we observe the neural network now correctly classifies the West Virginia ID as "Other"
	
	![image](https://user-images.githubusercontent.com/46364751/180016895-a338cd67-7b9c-41ef-95e6-eea186d27996.png)
	
	
* Other examples of improved identification over time is given below:

![image](https://user-images.githubusercontent.com/46364751/180017229-b0972f56-d7c7-42e0-8d99-55f5e69abb8d.png)

![image](https://user-images.githubusercontent.com/46364751/180017315-e3cdaedf-2b02-4367-bb30-571a968fde9b.png)

* The neural network and its outputs are now transferred over to a CUDA GPU available in Google Colaboratory

![image](https://user-images.githubusercontent.com/46364751/180017549-f60084ab-00cc-4935-92a0-4d929e0c4e77.png)

![image](https://user-images.githubusercontent.com/46364751/180018555-f7685dbb-cc48-47f3-b3ec-793d7513ef4d.png)


* For testing purposes the model is brought back onto CPU with the test image as the new inputs

![image](https://user-images.githubusercontent.com/46364751/180017688-cbd320ba-3b82-4f27-948f-a70cebd40583.png)


### Findings

* There continues to be bias in the model as it learns - currently it is biased towards the "Virginia" class

* Options to reduce ML false positives are:

	* Increase training data and add more images beyond just 50 images/samples
	* Change the picture size to reduce square pixels
	* Potentially not train in Grayscale 
	* Increase/decrease epochs
	* Increase/decrease nodes in each layer of neural network/perceptron
	* Increase/decrease layers in neural network/perceptron


### Installation / Software Requirements

* No software installation was required for this project. A Gmail account is required to access Google Colaboratory's free instance.

### License / Citation

* Python GPU License: https://docs.python.org/3.7/license.html
* Colaboratory Release 2022/7/1: https://colab.research.google.com/notebooks/relnotes.ipynb

### Support

* This project is a standalone development initiative without any ongoing support

