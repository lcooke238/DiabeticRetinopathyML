#imports
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, roc_auc_score

# load data
Xtrain = np.load("../data/train/Xtrain.npy")
Ytrain = np.load("../data/train/Ytrain.npy")
Xtest = np.load("../data/test/Xtest.npy")
Ytest = np.load("../data/test/Ytest.npy")

# train
clf = SVC()
clf.fit(Xtrain, Ytrain)
print("Done training!")
y_pred = clf.predict(Xtest)
print(f"accuracy score: {accuracy_score(Ytest,y_pred)}")
print(f"roc auc score: {roc_auc_score(Ytest, y_pred)}")
