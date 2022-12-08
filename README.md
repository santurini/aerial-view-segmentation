# Drone Images Semantic Segmentation

## Dataset

|Image|Binary|5-classes|
|:-------------------------:|:-------------------------:|:-------------------------:|
|![594](https://user-images.githubusercontent.com/91251307/206544548-2b0853c4-dc8b-4297-ae6d-02fd6994dd15.png)|![594](https://user-images.githubusercontent.com/91251307/206544587-3924f5a2-82ca-4eed-9ee2-60b3cf7d6fe2.png)|![594](https://user-images.githubusercontent.com/91251307/206543843-ceee696c-0d99-4e93-bba4-6626261da18d.png)|

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


