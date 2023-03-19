# Task
Predict whether diabetic retinopathy is referenceable (NPDR {Moderate or beyond} or DPR with NDE) or not. Do not worry if you cannot differentiate the images with your eyes (it requires trained professional and a well-trained neural network to do it). Note that the class imbalance has to be accounted for (will be appropriately rewarded). This is a binary classification problem.


# Data Exploration and Preprocessing
Referencebale retinopathy folders (Class 1): ('03 Moderate NPDR', '04 Severe NPDR',
'05 PDR', '06 Mild NPDR, with DME', '07 Moderate NPDR, with DME', '08 Severe NPDR,
with DME', '09 PDR, with DME');
- Non-referenceable folders (Class 2): (‘01 No DR', '02 Mild NPDR')
- Ignore folders: '00 5-Field Images', '10 Ungradable'

## Preprocessing Goals
- Preprocess the images for the model to learn from signals and noise
- Feel free to use the best practices and do not forget to mention it
- You may want to have some summary statistics of the data to check for class
imbalance before doing the model

## Ideas
- convert to greyscale to eliminate any color issues
- increase contrast to highlight the veins of interest (Adaptive histogram equalization)
- remove noise (discrete wavelet transform, followed by k-means clustering to create discernable clusters of signal)


I am a bit familiar with this problem--enough to know that literature exists about other group's approaches to it. In particular, I examined the Google paper in JAMA (https://jamanetwork.com/journals/jama/fullarticle/2588763?utm_campaign=articlePDF&utm_medium=articlePDFlink&utm_source=articlePDF&utm_content=jama.2016.17216)

