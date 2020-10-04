# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 21:03:25 2020

@author: ashte
"""


import pandas as pd 
from sklearn.model_selection import train_test_split
import numpy as np

dataset_new = pd.read_csv("dataset.csv")

COLS = ['AGE','GENDER','TYPE']

X = dataset_new[COLS]
y = dataset_new['SCHEMES']


#missing data for training
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(dataset_new[['SCHEMES']])
dataset_new[['SCHEMES']] =imputer.fit_transform(dataset_new[['SCHEMES']])

#encoding categorical data train
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[1])], remainder='passthrough')
X = np.array(ct.fit_transform(X))
ct_1 = ColumnTransformer(transformers=[('encoder', OneHotEncoder(),[3])], remainder='passthrough')
X = np.array(ct_1.fit_transform(X))

#feature scaling train
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)
from sklearn.preprocessing import MinMaxScaler
minmax= MinMaxScaler()
X= minmax.fit_transform(X) 


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
from sklearn.tree import DecisionTreeClassifier
#Using the random forest classifier for the prediction 
classifier=DecisionTreeClassifier(random_state = 10) 
classifier=classifier.fit(X_train,y_train) 
predicted=classifier.predict(X_test) 



from sklearn.metrics import confusion_matrix 
from sklearn.metrics import accuracy_score 
from sklearn.metrics import classification_report 
print ('Confusion Matrix :') 
print(confusion_matrix(y_test, predicted)) 
print ('Accuracy Score :',accuracy_score(y_test, predicted)) 
print ('Report : ') 
print (classification_report(y_test, predicted))
import smtplib 
server = smtplib.SMTP()
print("Defined server")
server.connect("smtp.gmail.com",587)
print("Connected")
server.ehlo()
server.starttls()
server.ehlo()
def sendMail(FROM,TO,SUBJECT,TEXT,SERVER):
    import smtplib
    """this is some test documentation in the function"""
    message = """\
        From: %s
        To: %s
        Subject: %s
        %s
        """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    # Send the mail
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.sendmail(FROM, TO, message)
    server.close()

physician = pd.read_csv("Physician_details.csv")


dataset_new_1 = pd.read_csv("SchemeDetails.csv")
col =['scheme', 'description']
M = dataset_new_1[col]

for key in predicted:
    m=0
    for i,j in M.iterrows():
        if(key == j.scheme):
            sendMail("ashtekarsejal@gmail.com", [X_test.iloc[[m],[5]]], "MAil Regarding new Medical Trial", j.description + physician.sample(),'localhost')


