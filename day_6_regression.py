# -*- coding: utf-8 -*-
"""DAY_6_Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1r1C_JRnYo9DwSdqvHwpoHaoJw7YCIacP
"""



"""machine learning

1. It will be trained with labeled data
2. Takes a feature for every variable
3. feature 1 is for variable 1 and so on 1st
when a provied a new coin for machine it will look for the feature value then checks which label matches this feature value

supervied learning alogithm
1. linear reression
2. logistic regression
3. decision tree
4. random forest

1. linear regression
* liner regression is also a type of machine-learning algorithm
* supervised machine-learning alogorithm
* learns from the lablled databasets and maps the data points to the most optimized linear function
* these points can be used for preaction on new datasets


Dependent and independent variable
* independent
* the independent variable is the cause. its value is independent of other variables in your study
* dependent
* the dependent variable is the effect. its value depends




Case study
consider measurments of a chemical reaction:
the mass of the product increase with time.
the obsevations are:
time-independent
mass-dependent



find the mean of depedent variable and independent variable

"""

# Demo coding:
from sklearn.linear_model import LinearRegression
LR=LinearRegression()

t=[[5],[7],[12],[16],[20]]
m=[40,120,180,210,240]
LR.fit(t,m)

LR.predict([[5.5]])

"""What is binary classification
Example segregting food:
y=0,



Case study
. let us take data from football matches:
. Based on the distance between player and goal post, we are going to predict whether it is a goal are not!
. let us plot some trails now
. when distance=2m,goal is scored,y=1
. when ditance =4m,goal is scored,y=1
. for 5,7,10,20,22m,it is always a goal,y=1
. when disatance =23m,for 15trails,few are goals y=1,few are failures y=0



Sigmoid Function
. sigmod function is a s-shaped function with peak at 1 and 0 at valley.
. when model is very  confident,narrow DB
. when model is not conifident .wide dececison Boundary


EX:
after plotting distance vs goals between 20 and 30m,the probability reducses from 1 to0
. But logistic regression accepts only 2 classes
so. A thresold variables (0.5) is set
The model prediction:
1. p>0.5,its a goal!!-class A(y=1)
2. p=<0.5,its a miss!-class b(y=0)

"""



import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
# Distance and corresponding probability data
distances = np.array([1,2,5,10,15,20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,35,40,41,47,50]).reshape(-1, 1)
probabilities = np.array([1,1,1,1,1,1,0.9, 0.85, 0.73, 0.67, 0.5, 0.47, 0.39, 0.31, 0.25, 0.15,0,0,0,0,0])

# convert probabilities to binary labels
thresold =0.5
binary_labels=(probabilities>thresold).astype(int)

#create and fit logistic regresssion model
logr =LogisticRegression()
logr.fit(distances,binary_labels)

# distance
p=logr.predict([[10]])
print(p)

if p==[1]:
  print("Goal")
else:("No Goal")

# predict 100 distances between 1 and 50
# generate distances for prediction
dist= np.linspace(1,50,100).reshape(-1,1)
print(dist) #distances
#make predictions using the model
prob =logr.predict_proba(dist)[:,1] #predictions
print(prob)

#model=a copy of  an algorithm
#testing data=what are we predictig
#training data=data written in flt block
#plotting actual data-train
import matplotlib.pyplot as plt
plt.scatter(distances,binary_labels,color='black',label='data')

#plotting test data with predctions --test/valid
plt.plot(dist,prob,color='blue',label='LogesticRegression')
plt.title('Distane vs probability of scroing a Goal')
plt.xlabel('Distance')
plt.ylabel('probability')
plt.legend()
plt.grid(True)
plt.show()

"""Decision tress
. decision tress in machine learning provide an effective method for making for decisions because they lay out the problem and all the possible outcomes.
. Have Nodes and Leaves
.Node: condition having true and false branches

CASE STUDY


. Taking s dataset of 26 states with features like Literacy,cleanlines,crime rate and tragetting(prediciting) Good or Bad state!

. Good is called Target variable here, it has values of 0s and 1s

. view:

Now let us create a decision tree

.Decision tree recurrently (continosly) splits the data until it gets pure leaves
. Let us view a DT based on crime rate.

Building decision tree

NOde 1:  CR>60
True-[C,Q,X]=O(pure leaf)
FAlse-[A,E,F,G,I,K,L,N,P,R,U,V=0][B,D,H,J,M,O,S,T,W,Y,Z=1]
the mixed leaf has target variable with both 0s and 1s,Hence this data is slipped once again.
"""

import pandas as pd

df=pd.read_csv("/content/demodt.txt")
df

from sklearn.tree import DecisionTreeClassifier

target=df.Good
print(target)

feat_list=['Literacy','Cleanliness','Crime_Rate']
feat=df[feat_list]
print(feat)

model=DecisionTreeClassifier()
model.fit(feat,target)

Lit=int(input("Enter Lit"))
Cle=int(input("Enter Cle"))
Cri=int(input("Enter Cri"))

pred=model.predict([[Lit,Cle,Cri]])
print(pred)

if pred==1:
  print("Good")
else:
    print("Bad")

"""Random forest
. collection of many decision tree
. keywoards boosttraping


case study:
y-target
x0t,x1,x2,x3,x4 are features



* boosttraping
splicting datatype in to childdata sets
. having same no.of rows and should have differnt combination










"""

