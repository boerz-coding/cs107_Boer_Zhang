def numerical_diff(f,h):
    def df(x):
        return  (f(x+h)-f(x))/h        
    return df
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0.2,0.4,100)
##exact derivative
exact_derivative=1/x
####
ffdh1=numerical_diff(lambda x:np.log(x),1e-1)
ffdh2=numerical_diff(lambda x:np.log(x),1e-7)
ffdh3=numerical_diff(lambda x:np.log(x),1e-15)
plt.plot(x,exact_derivative,'x',label='Analytical 'r'$\frac{df}{dx} (x)=\frac{1}{x}$')
plt.plot(x,ffdh1(x),label=r'$h=1\times 10^{-1}$')
plt.plot(x,ffdh2(x),label=r'$h=1\times 10^{-7}$')
plt.plot(x,ffdh3(x),label=r'$h=1\times 10^{-15}$')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
print("Answer to Q-a: h=1e-7 most closely approximates \
the true derivatives. When h is too small, the numerical derivative becomes \
inaccurate, and it goes away from the true derivative. \
When h is too large, the result becomes quite weird, it oscillates \
around the true derivative, instead of overlapping with the true value.")
print("Answer to Q-b: With automatic differentiation, the symbolic derivative\
is calculated and then evaluated numerically. Thus it will be the same to directly\
calculating the analytical derivative.")
plt.show() 
