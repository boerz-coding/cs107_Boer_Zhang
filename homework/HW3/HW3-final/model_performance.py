#!/usr/bin/python3

##model_performance.py
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
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

alpha_array=np.logspace(-2,1,10)
score_array_ols=np.zeros(alpha_array.shape)
score_array_rig=np.zeros(alpha_array.shape)

cnt=0
for alpha_i in alpha_array:
  for model in models:
    model.set_params(alpha=alpha_i)
    model.fit(X_train, y_train)
  score_array_ols[cnt]=olsreg.score(X_test, y_test)
  score_array_rig[cnt]=rigreg.score(X_test, y_test)
  cnt+=1

plt.semilogx(alpha_array,score_array_ols,'o',label="OLS Regression")
plt.semilogx(alpha_array,score_array_rig,'x',label="Ridge Regression")
plt.xlabel(r'$\alpha$',fontsize=12)
plt.ylabel(r'Score $R^{2}$',fontsize=12)
plt.legend()
plt.tick_params(labelsize=12);
plt.show()
