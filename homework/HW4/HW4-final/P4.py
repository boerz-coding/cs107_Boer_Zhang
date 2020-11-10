class AutoDiffToy():
  def __init__(self,value,der=1):
    self.val=value
    self.der=der
  def __add__(self,other):
    temp=AutoDiffToy(self.val,self.der)
    try:
      temp.val+=other.val
      temp.der+=0
    except AttributeError:
      if isinstance(other, (int, float)):
        temp.val+=other
        temp.der+=0
      else:
        print(f"Undefined __add__ calculation between 'AutoDiffToy' and '{type(other)}' !")
    return temp
  
  def __mul__(self,other):
    temp=AutoDiffToy(self.val,self.der)
    try:
      temp.val=temp.val*other.val
      temp.der=temp.der*other.der
    except AttributeError:
      if isinstance(other, (int, float)):
        temp.val=temp.val*other
        temp.der=temp.der*other
      else:
        print(f"Undefined __mul__ calculation between 'AutoDiffToy' and '{type(other)}' !")
    return temp

  def __radd__(self,other):
    return self.__add__(other)
  def __rmul__(self,other):
    return self.__mul__(other)
  

a = 2.0 # Value to evaluate at
x = AutoDiffToy(a)

alpha = 2.0
beta =  3.0
#demo
print("Demo for 4 different cases")
f = alpha*x + beta
print(f.val, f.der)
f = x*alpha + beta
print(f.val, f.der)
f = x*alpha + beta
print(f.val, f.der)
f = x*alpha + beta
print(f.val, f.der)
