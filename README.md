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
**Data source:**
Arabic captions:https://github.com/aub-mind/Arabic-Image-Captioning/tree/master/data/Flickr8k_text

Images:https://www.kaggle.com/datasets/adityajn105/flickr8k?select=Images

![image](https://user-images.githubusercontent.com/113424173/215351243-a13d7312-c3c6-41a9-b16e-1740e299e7b9.png)
