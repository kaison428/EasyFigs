# EasyFigs: A Convolutional Neural Network Approach for Extracting Figures from PDFs

## Overview
EasyFigs is a machine learning project aimed at detecting figures from PDF documents. This project was born out of the need to improve the process of extracting figures from PDFs, which is often imprecise and time-consuming. Existing PDF Image Extractors are unable to accurately detect useful figures or extract captions.

## Data
The original data used for this project consists of research articles from the Arxiv website in PDF format. The dataset includes 870 PDFs. The PDFs are split into pages and converted to images. We selected 900 pages with figures and 100 pages without figures.

## Model Selection
The main model used in this project is YoLo v5s, a state-of-art object detection algorithm that uses a Convolutional Neural Network. It has 191 layers and 7.5*106 trainable parameters. The model was chosen for its speed, accuracy, and compatibility with Pytorch and RoboFlow.

## Hyperparameters Tuning
Hyperparameters were selected based on the results from the hyperparameters evolution process using a Genetic Algorithm. The model was trained for 150 epochs with a batch size of 32 and an image size of 640*640.

## Results
The primary metric used for evaluation is Mean Average Precision (mAP). The model performed well on both the testing dataset and a brand new dataset.

## Future Work
While the model performed well, the dataset used was biased. Future work will involve using a larger and more generalized dataset. This work is expected to have a positive impact on the computer vision research community.

## Links
- [YOLOv5 Github](https://github.com/ultralytics/yolov5)
- [Tips for Best Training Results](https://github.com/ultralytics/yolov5/wiki/Tips-for-Best-Training-Results)
- [Mean Average Precision (mAP) Explanation](https://jonathan-hui.medium.com/map-mean-average-precision-for-object-detection-45c121a31173)

