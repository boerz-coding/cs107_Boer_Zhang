##Collaborators: Connor Capitolo, Boer Zhang, Kristen Grabarz, Seeam Noor
import numpy as np

# helper function
def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1;
    else:
        return fibo(n - 1) + fibo(n - 2);

class Fibonacci:

    def __init__(self,n):
        self.series= list(range(n))#a list
        
        for i in range(0,n):
            self.series[i]=fibo(i)

    def __iter__(self):
        return Fibiterator(self.series)

class Fibiterator:

    def __init__(self,series):
        self.series=series
        self.index=0
        
    def __next__(self): 
        try:
            value = self.series[self.index]
        except IndexError:
            raise StopIteration()
        self.index+=1
        return value


    def __iter__(self):
        return self

fib = Fibonacci(10) # Create a Fibonacci iterator called fib that contains 10 terms
list(iter(fib))
