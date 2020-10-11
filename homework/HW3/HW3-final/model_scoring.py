#!/usr/bin/python3
##model_scoring.py

from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
import Regression as myReg


dataset = datasets.load_boston()
X_train, X_test, y_train, y_test = train_test_split(dataset['data'], 
                                                    dataset['target'], 
                                                    test_size=0.2, 
                                                    random_state=42)


alpha=0.1
olsreg=myReg.LinearRegression()
rigreg=myReg.RidgeRegression()

rigreg.set_params(alpha=0.1)




models = [olsreg, rigreg]

for model in models:
    model.fit(X_train, y_train)
    print(type(model).__name__,model.score(X_test, y_test))
