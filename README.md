# Drone Images Semantic Segmentation

## Dataset

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
### Binary Sample
![ao](https://user-images.githubusercontent.com/91251307/206537000-19647dab-c9df-4352-b41f-c83f953c679a.png)

### 5-class Sample
![cacca](https://user-images.githubusercontent.com/91251307/206538631-23e6ff7e-190a-4ede-b390-68a0176ea56c.png)

### Original Sample
![image](https://user-images.githubusercontent.com/91251307/206538927-79bb7e72-4972-4ffa-83b0-3f1b59b86fa5.png)


