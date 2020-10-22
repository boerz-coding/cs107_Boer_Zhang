#!/usr/bin/python3

import numpy as np
class Regression():

    def __init__(self):
        # your code
        self.params={}

    def get_params(self):
        # your code
        return self.params

    def set_params(self, **kwargs):
        for key,value in kwargs.items():
          self.params[key]=value
          #print(self.params["alpha"])

    def fit(self, X, y):
        # your code
        raise NotImplementedError

    def predict(self, X):
        # your code
        #print(self.params["coefficients"].shape)
        beta_star=np.append(self.params["coefficients"],self.params["intercept"])
        X1=np.append(X,np.ones([X.shape[0],1]),axis=1)
        return np.dot(X1,beta_star)

    def score(self, X, y):
        # your code
        y_star=self.predict(X)
        ybar=np.mean(y)
        SST=np.linalg.norm(y-ybar)**2
        SSE=np.linalg.norm(y-y_star)**2
        return 1-SSE/SST


class LinearRegression(Regression):
  def fit(self, X, y):
    X1=np.append(X,np.ones([X.shape[0],1]),axis=1)
    beta_star=np.dot(np.dot(np.linalg.pinv(np.dot(X1.T,X1)),X1.T),y)
    self.params["coefficients"]=beta_star[0:-1]
    self.params["intercept"]=beta_star[-1]
    #print("fit ols")

class RidgeRegression(Regression):
  def __init__(self):
    # your code
    self.params={}
    self.params["alpha"]=0.1
  def fit(self, X, y):
    X1=np.append(X,np.ones([X.shape[0],1]),axis=1)
    #print(np.eye(X1.shape[]))
    Gamma=self.params["alpha"]*np.eye(X1.shape[1])
    beta_star=np.dot(np.dot(np.linalg.pinv(np.dot(X1.T,X1)+np.dot(Gamma.T,Gamma)),X1.T),y)
    self.params["coefficients"]=beta_star[0:-1]
    self.params["intercept"]=beta_star[-1]
    #print("fit ridge")

