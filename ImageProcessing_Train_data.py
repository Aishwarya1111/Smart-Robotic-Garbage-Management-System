import os 
import csv 
from sklearn.ensemble import RandomForestClassifier 
from joblib import dump, load 
import cv2 
from skimage import color 
from skimage.feature import hog 
from sklearn import svm 
from skimage import io 
from sklearn.metrics import classification_report,accuracy_score import numpy as np 
TrainData="Train" 
label=[] 
Features=[] 
count=0
for (dirpath,dirnames,filenames) in os.walk(TrainData): 
 for dirname in dirnames: 
 count=count+1 
 for(direcpath,direcnames,files) in os.walk(TrainData+"\\"+dirname):  for file in files: 
 if 'jpg' in file: 
 path=TrainData+"\\\\"+dirname+"\\\\"+file 
 frame = io.imread(path) 
 converted2 = color.rgb2gray(frame) 
 converted2 = cv2.resize(converted2,(128,128)) 
 fd,hog_image = hog(converted2, orientations=8,  pixels_per_cell=(16,16),cells_per_block=(4, 4),block_norm= 'L2',visualise=True) 
 label.append(int(dirname)) 
 Features.append(fd) 
clf = svm.SVC() 
fet = [] 
for i in Features: 
 infet=[] 
 for j in i: 
 infet.append(j) 
 fet.append(infet) 
X= (fet) 
clf.fit(X,label) 
y_pred = clf.predict(X) 
print("Accuracy: "+str(accuracy_score(label, y_pred))) 
dump(clf, 'RF.Model')
