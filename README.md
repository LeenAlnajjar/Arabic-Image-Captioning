# Arabic-Image-Captioning
Image captioning is to generate a natural language description of the contents of an image using both a system that can understand visual information and a language model that can generate grammatically correct sentences. This requires the use of a visual understanding system and a language model.

<p align="center">
<img src="https://user-images.githubusercontent.com/113424173/215345176-86dee413-2c28-4d55-b185-ea34c99ea111.png" width="400" height="400">
</p>

# Abstract
The process of generating content from images is considered to be a very difficult and challenging task, but at the same time, it is very impressive because it helps blind people to have a better understanding of their surroundings. The importance of automatic image caption generator for children with learning difficulties come from the visibility of transferring the captions later on to voice by using text-to-speech technology in order to describe the whole image for those people. Although it is considered a critical mission, the resources and projects regarding automatic Arabic image captioning are rare and need further improvements. According to that, this work aims to build an Automated Arabic Image Caption Generator model to give a short explanation of the images in the Arabic language. The model will be constructed from both CNN which aims to figure out features from figures and the LSTM which will take the features from the CNN and provide suitable descriptions for these features.  The data itself is constructed from images and text or description for each image.
# Project Associated Challenges
Although there are around 400 million Arabic speakers globally , and significant importance of the Arabic image captioning, but there were only few resources studied it, and they still need for further improvement. In addition to the lack of dataset, there are many reasons behind the deficiency of Arabic image captioning models, and these reasons are listed below :
* lack of interest of using Arabic image captioning techniques either globally or regionally. For example, in 2020 there were only 3 papers studied the Arabic image captioning, despite the fact that the image captioning was firstly introduced in early 2000s.
* Arabic language is very difficult, this because unlike most of other languages it requires unique writing system from the right to the left. Furthermore, the grammar and the lexical/morphological sparsity in the Arabic language is considered to be demanding task for those who want to build an Arabic image captioning model.
* The availability of high-quality Arabic language data may be more limited compared to other languages, which can also make it more difficult to develop and train effective image captioning models.
# Data 
As mentioned previously, there are lack of sources regarding Arabic Image Captioning, but at the end Arabic Flickr 8k dataset was selected.
## Data source:

* Arabic captions dataset:https://github.com/aub-mind/Arabic-Image-Captioning/tree/master/data/Flickr8k_text

* Images dataset:https://www.kaggle.com/datasets/adityajn105/flickr8k?select=Images

## Data visualization:
Flickr8k dataset contains 8000 images with 3 captions for each images, which can be visualized as following:

<p align="center">
<img src="https://user-images.githubusercontent.com/113424173/215352444-0693f0bd-e73a-4b2f-8b3c-55d05315fb49.png">
</p>

# Methodology

Sequance-to-sequance encoder decoder was used to build the AIC , the MobileNetV2 was used to extract the features from the images, the NLP was used to prepare the captions and the RNN-LSTM was used to obtain the captions for each image.

<p align="center">
<img src="https://user-images.githubusercontent.com/113424173/215356547-7423b6ab-28f5-45f1-bf62-7d83f30be45d.png">
</p>

## Model overview
The model is constructed from three main stages, each stage play major role in the project, these are mentioned bellow:

* **Feature Extraction:**

Each image should be converted into a fixed size vector in order to feed it into the neural network model. Hence, the classification process occurs at the last two layers, which were dropped to ensure that the output will only be the features instead of classes. The process of selecting the approperiate CNN model is illustrated below:

<p align="center">
<img src="https://user-images.githubusercontent.com/113424173/215357080-c3f6e7bf-443a-4963-8940-cb1b1011fea7.png">
</p>



