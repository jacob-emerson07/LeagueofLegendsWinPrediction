"""
Created on Sat Jun 20 15:00:57 2020

@author: Jacob Emerson
"""

import pandas as pd
import numpy as np

# Import data

df = pd.read_csv("C:/Users/Jacob's PC/Desktop/LeagueofLegendsWinPrediction/cleanedData.csv", index_col=False)

#print(df.columns)

# Remove the deaths and ward columns like I said I would in the EDA

df_for_model = df.drop(['blueDeathDiff', 'blueWardPlacedDiff', 'blueWardDestroyedDiff'], axis=1)

print(df_for_model.columns)
# Normalize data for Linear SVC/Logistic Regression models

# Code for this section adapted from raullalves on 
# https://stackoverflow.com/questions/26414913/normalize-columns-of-pandas-data-frame

from sklearn.preprocessing import MinMaxScaler

min_max_scaler = MinMaxScaler()
column_names_to_not_normalize = ['blueWins', 'dragTeam', 'heraldTeam', 'fbTeam', 'blueTowerDestroyedDiff', 'blueAvgLvlDiff']
column_names_to_normalize = [x for x in df_for_model.columns if x not in column_names_to_not_normalize]
x = df_for_model[column_names_to_normalize].values
x_scaled = min_max_scaler.fit_transform(x)
df_temp = pd.DataFrame(x_scaled, columns=column_names_to_normalize, index = df.index)
df_for_model[column_names_to_normalize] = df_temp

df_for_model.to_csv(r"C:\Users\Jacob's PC\Desktop\LeagueofLegendsWinPrediction\modelData.csv", index=False)

# Set up train/test data
from sklearn.model_selection import train_test_split

X = df_for_model.drop('blueWins', axis = 1)
y = df_for_model['blueWins']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=15)


# I will try 4 different kinds of ML models: SVC, LinearSVC, Logistic Regression and a Random Forest Classifier

# SVC
# SVC has a score of  0.7155870445344129  and a cross val score of  0.7116287560348761

from sklearn.svm import SVC

svc = SVC(random_state = 15)

svc.fit(X_train, y_train)


from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score


print("SVC has a score of ", accuracy_score(y_test, svc.predict(X_test)), " and a cross val score of ", np.mean(cross_val_score(svc,X_train,y_train, cv= 5)))


# LinearSVC
# Linear SVC has a score of  0.7302631578947368  and a cross val score of  0.7166902857508867

from sklearn.svm import LinearSVC

linSvc = LinearSVC(random_state = 15)

linSvc.fit(X_train, y_train)

print("Linear SVC has a score of ", accuracy_score(y_test, linSvc.predict(X_test)), " and a cross val score of ", np.mean(cross_val_score(linSvc,X_train,y_train, cv= 5)))


# Logistic Regression
# Logistic Regression has an accuracy of  0.7307692307692307  and a cross val score of  0.7174494591630036

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state = 15)

lr.fit(X_train, y_train)

print("Logistic Regression has an accuracy of ", accuracy_score(y_test, lr.predict(X_test)), " and a cross val score of ", np.mean(cross_val_score(lr,X_train,y_train, cv= 5)))


# Random Forest Classifier
# Forest has an accuracy of  0.7044534412955465  and a cross val score of  0.6884719653480011

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(random_state = 15)

rfc.fit(X_train, y_train)

print("Forest has an accuracy of ", accuracy_score(y_test, rfc.predict(X_test)), " and a cross val score of ", np.mean(cross_val_score(rfc,X_train,y_train, cv= 5)))


# Pickle and Save best model (Logistic Regression)

import pickle

pickle.dump(lr, open(r"C:\Users\Jacob's PC\Desktop\LeagueofLegendsWinPrediction\finalModel", "wb"))

# Ensure model was saved properly

lrCheck = pickle.load(open(r"C:\Users\Jacob's PC\Desktop\LeagueofLegendsWinPrediction\finalModel","rb"))

print(str(lrCheck) == str(lr))
