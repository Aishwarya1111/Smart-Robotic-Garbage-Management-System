import os 
import csv 
from sklearn.ensemble import RandomForestClassifier from joblib import dump, load 
import cv2 
from skimage import color 
from skimage.feature import hog 
from sklearn import svm 
from skimage import io 
from sklearn.metrics import classification_report,accuracy_score import numpy as np 
import time 
TestData="Test" 
while True: 
 for(direcpath,direcnames,files) in os.walk(TestData):  for file in files: 
 if 'jpg' in file: 
 Features=[] 
 time.sleep(1) 
 frame = frame = io.imread(TestData+'//'+file)  converted2 = color.rgb2gray(frame) 
 converted2 = cv2.resize(converted2,(128,128))
 fd,hog_image = hog(converted2, orientations=8,  
pixels_per_cell=(16,16),cells_per_block=(4, 4),block_norm= 'L2',visualize=True)  infet=[] 
 for j in fd: 
 infet.append(j) 
 Features.append(infet) 
 clf = load('RF.Model') 
 cl = clf.predict(Features) 
 print(cl[0]) 
 os.remove(TestData+'/'+file) 
