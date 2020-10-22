from enum import Enum

class AccountType(Enum):
    SAVINGS = 1
    CHECKING = 2


class BankAccount():
  def __init__(self, owner, accountType: AccountType):
    # your code
    self.owner=owner
    self.accountType=accountType
    self.balance=0


  def withdraw(self, amount):
    if(amount>self.balance):
      raise ValueError("You do not have that amount of money!")
    if(amount<0):
      raise ValueError("Amount should be positive!")
    # your code  
    self.balance=self.balance-amount
        
  def deposit(self, amount):
    # your code
    if(amount<0):
      raise ValueError("Amount should be positive!")
    self.balance=self.balance+amount

  def __str__(self):
    return f"Account owner: {self.owner}, Account type: {self.accountType.name}."

  def __len__(self):
    return self.balance



class BankUser():
  def __init__(self, owner):
    # your code
    self.owner=owner
    self.accounts={}
    
  def addAccount(self, accountType):
    # your code
    if accountType.name in self.accounts.keys():
      raise ValueError("Account already exist.")
    self.accounts[accountType.name]=BankAccount(self.owner, accountType)

    
        
  def getBalance(self, accountType):
    # your code
    if accountType.name not in self.accounts.keys():
      raise ValueError("Account does not exist.")
    return self.accounts[accountType.name].balance
  
  def deposit(self, accountType, amount):
    # your code
    if accountType.name not in self.accounts.keys():
      raise ValueError("Account does not exist.")
    self.accounts[accountType.name].deposit(amount)
  
  def withdraw(self, accountType, amount):
    # your code
    if accountType.name not in self.accounts.keys():
      raise ValueError("Account does not exist.")
    self.accounts[accountType.name].withdraw(amount)

  def __str__(self):
    # your code
    str_accounts=""
    for key in self.accounts:
      if str_accounts:
        str_accounts+=", "
      str_accounts+=key
    if not str_accounts:
      str_accounts="not exist"
    return f"Owner: {self.owner}; Accounts: {str_accounts}."

  
def ATMSession(bankUser):
  def Interface():
    while True:
      print("Enter Option:\n"
            +"1)Exit\n"
            +"2)Create Account\n"
            +"3)Check Balance\n"
            +"4)Deposit\n"
            +"5)Withdraw")
      opt=input()
      try:
        opt=int(opt)
      except Exception as e:
        print(e) 
        print("Must input an integar!")
        continue
      if (opt==1):
        return None
      elif (opt==2 or opt==3 or opt==4 or opt==5):
        print("Enter Option:\n"
            +"1)Checking\n"
            +"2)Savings")
        opt2=input()
        try:
          opt2=int(opt2)
        except Exception as e:
          print(e) 
          print("Must input an integar!")
          continue 
        
        if (opt2==1):
          acttype=AccountType.CHECKING
        elif (opt2==2):
          acttype=AccountType.SAVINGS
        else:
          print("Wrong option input.")
          continue

        if (opt==2):
          try:
            bankUser.addAccount(acttype)
          except Exception as e:
            print(e)
            continue
          else:
            print(f"Successfully created {acttype.name} account.")

        if (opt==3):
          try:
            print(f"Balance in your {acttype.name} account is {bankUser.getBalance(acttype)}")
          except Exception as e:
            print(e)
            continue
        if (opt==4 or opt==5):
          print("Enter Integer Amount, Cannot Be Negative:")
          opt3_amount=input()
          try:
            opt3_amount=int(opt3_amount)  
          except Exception as e:
            
            print(e)
            print("Must input an integar!")
            continue

          if (opt==4):
            try:
              bankUser.deposit(acttype,opt3_amount)
            except Exception as e:
              print(e)
              continue
            else:
              print(f"Successfully deposited {opt3_amount} from your {acttype.name} account, current balance is {bankUser.getBalance(acttype)}.")
            
          if(opt==5):
            try:
              bankUser.withdraw(acttype,opt3_amount)
            except Exception as e:
              print(e)
              continue
            else:
              print(f"Successfully withdrawn {opt3_amount} from your {acttype.name} account, current balance is {bankUser.getBalance(acttype)}")
      else:
        print("Wrong option input.")
        continue
      
  return Interface
  
