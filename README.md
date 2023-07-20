# DiabeticRetinopathyML: Using Machine Learning to diagnose Diabetic Retinopathy

## Introduction
For this project, I built a machine learning model and a processing pipeline for retina scans to diagnose moderate to severe diabetic retinopathy. All original data used for this project was provided by Basys.AI as a part of their interview process, and therefore will not be included in the public version of the repository. This README gives a high level overview of the code portion of repository containing this project. Structure:

code: folder that contains code
- ```exploration.ipynb```: initial data exploration, this notebook documents my figuring out how to best isolate the features of interest from the original data.
- ```preprocessing.ipynb```: runs the most successful image preprocessing functions developed in the exploration file.
- ```modeling.ipynb```: first model attempt, uses a prebuilt cnn network along with some additional layers (and no transfer learning).
- ```modeling_baseline.ipynb```: base model attempt, uses a prebuilt cnn network along with some additional layers with minimal to no image preprocessing.
- ```modelingv2.ipynb```: final model, uses similar prebuild cnn network to first attempt, uses transfer learning and cleaner images.
 
