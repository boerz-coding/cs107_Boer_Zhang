#!/usr/bin/python3
class Regression():

    def __init__(self):
        # your code
        self.params={}

    def get_params(self):
        # your code
        return self.params

    def set_params(self, **kwargs):
        # your code
        raise NotImplementedError

    def fit(self, X, y):
        # your code
        raise NotImplementedError

    def predict(self, X):
        # your code
        raise NotImplementedError

    def score(self, X, y):
        # your code
        raise NotImplementedError
