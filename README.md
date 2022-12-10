# Drone Images Semantic Segmentation

## Repository Structure

The repository is structured as follows:
	- _code_ folder: contains the notebook for image preprocessing, Binary segmentation and Multi-class segmentation
	- _plots_ folder: contains two subfolders _binary_ and _multiclass_ with the respective plots

The dataset used is called **Semantic Segmentation Drone Dataset** and can be downloaded already processed at the following [link](https://www.kaggle.com/datasets/santurini/semantic-segmentation-drone-dataset).

From the original dataset the images were processed in such a way as to reduce the resolution and rename the labels to perform both Binary and Multi-class Classification; in the second case instead of using the original 24 classes they were grouped into 5 macro-classes as follows:

```
binary_classes = {
	0: {0, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}, # obstacles
	1: {1, 2, 3, 4, 9} # landing zones
}

grouped_classes = {
         0: {0, 6, 10, 11, 12, 13, 14, 21, 22, 23}, # obstacles
         1: {5, 7}, # water
         2: {2, 3, 8, 19, 20}, # soft-surfaces
         3: {15, 16, 17, 18}, # moving objects
         4: {1, 4, 9} # landable
}
```
|Image|Binary|5-classes|
|:-------------------------:|:-------------------------:|:-------------------------:|
|![594](https://user-images.githubusercontent.com/91251307/206544548-2b0853c4-dc8b-4297-ae6d-02fd6994dd15.png)|![594](https://user-images.githubusercontent.com/91251307/206544587-3924f5a2-82ca-4eed-9ee2-60b3cf7d6fe2.png)|![594](https://user-images.githubusercontent.com/91251307/206543843-ceee696c-0d99-4e93-bba4-6626261da18d.png)|

## Models and Training
The performance of 3 different Image segmentation models, each with its own particular characteristic, considered the state of the art were compared just to go to show how the different underlying concepts differed.

The models all had as their backbone an _efficient-b0_ pretrained on imagenet, while the decoders were trained for 25 epochs on the augmented train set. Given the limited number of images (just 400) augmentation was crucial in order to train better the models.

The criterion used for the backpropagation was the Dice Loss (Binary and Multi-class) and the model was evaluated with Recall, False Positive Rate and image-wise IoU (in the Multi-class case all the metrics beside IoU were computed per-class).

|Model|Charachteristic|Paper|
|:-------------------------:|:-------------------------:|:-------------------------:|
|**U-Net**|Fully Convolutional|[paper](https://arxiv.org/pdf/1505.04597.pdf)|
|**DeepLabV3**|Dilated Convolutions|[paper](https://arxiv.org/pdf/1706.05587v3.pdf)|
|**MAnet**|Attention Mechanism|[paper](https://arxiv.org/pdf/2009.02130.pdf)|

## Binary Segmentation
We leave here some mask predictions and results from the binary segmentation task.

|Images|Groundtruth|U-Net|DeepLabV3|MAnet|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img src="https://user-images.githubusercontent.com/91251307/206849683-1d5add75-6144-4a77-8307-ac33529e2e2a.png">|<img src="https://user-images.githubusercontent.com/91251307/206849703-3817de45-cdf3-4b30-9a6a-527c3968b5ed.png">|<img src="https://user-images.githubusercontent.com/91251307/206849709-7ca86dcc-1c12-41ce-9ccd-6b6715988266.png">|<img src="https://user-images.githubusercontent.com/91251307/206849717-cffa3c84-1f59-4e18-ad9e-6570b1f975eb.png">|<img src="https://user-images.githubusercontent.com/91251307/206849733-72783a38-68e6-402f-bc0b-a295ee7ed389.png">|

|Models|Recall|FPR|IoU|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|U-Net|0.971|0.222|0.923|
|DeepLabV3|0.971|0.251|0.919|
|MAnet|0.973|0.249|0.918|

## Multi-class Segmentation
This are the results for the 5-class segmentation:
|Images|Groundtruth|U-Net|DeepLabV3|MAnet|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|<img src="https://user-images.githubusercontent.com/91251307/206851005-eb5af95c-1360-4a36-8619-9593c21fc00d.png">|<img src="https://user-images.githubusercontent.com/91251307/206851033-5df0bd2e-0496-4e8d-918d-55062b4dc199.png">|<img src="https://user-images.githubusercontent.com/91251307/206851054-b16271a5-90a8-425c-80e1-5234623ddd5b.png">|<img src="https://user-images.githubusercontent.com/91251307/206851067-a6acd522-3f7b-4218-8054-1f8c03e8cbbc.png">|<img src="https://user-images.githubusercontent.com/91251307/206851078-6a1cbb4f-eb95-486e-b2c9-09e5e56263fd.png">|

|U-Net|Obstacles|Water|Nature|Moving|Landing|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|Recall|0.67|0.96|0.882|0.657|0.955|
|FPR|0.022|0.001|0.029|0.002|0.123|
|IoU|0.518|0.903|0.843|0.581|0.842|

|DeepLabV3|Obstacles|Water|Nature|Moving|Landing|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|Recall|0.633|0.955|0.905|0.672|0.94|
|FPR|0.022|0.001|0.062|0.004|0.107|
|IoU|0.503|0.883|0.814|0.563|0.896|

|MAnet|Obstacles|Water|Nature|Moving|Landing|
|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:|
|Recall|0.492|0.921|0.891|0.682|0.95|
|FPR|0.012|0.001|0.048|0.004|0.162|
|IoU|0.431|0.83|0.82|0.566|0.825|
