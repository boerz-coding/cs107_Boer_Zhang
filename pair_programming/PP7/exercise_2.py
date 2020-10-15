"""
Pair Programming Assignment #7
Collaborators: Ryan Liu, Blake Bullwinkel, Zhufeng Kang, Boer Zhang
Forward mode on f(x) = x**r
"""

# Define a simple function
def my_pow(x, r):
    f = x**r
    f_prime = (r)*x**(r-1)
    output = (f, f_prime)
    return output

# Implement a closure
def outer(r):
    def inner(x, seed):
        f = x**r
        f_prime = seed*(r)*x**(r-1)
        output = (f, f_prime)
        return output
    return inner

# Using a class        
class my_pow_class:
    def __init__(self, r):
        self.r = r
    def get_tuple(self, x, seed):
        f = x**self.r
        f_prime = seed*(self.r)*x**(self.r-1)
        output = (f, f_prime)
        return output
        

if __name__ == "__main__":
    print(my_pow(3, 4))
    closure_test = outer(4)
    print(closure_test(3,1))
    class_test = my_pow_class(4)
    print(class_test.get_tuple(3,1))