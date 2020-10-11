from Bank import *
def test_over_withdrawal(): #this test function should throw an Exception or Error 
    user = BankUser("Joe");
    user.addAccount(AccountType.SAVINGS);
    user.deposit(AccountType.SAVINGS, 10);

    print("Test getBalance and deposit 1 (SAVINGS), current balance:",user.getBalance(AccountType.SAVINGS))
    
    try:
      user.deposit(AccountType.SAVINGS, -10);
    except Exception as e:
      print("Test deposit 2 (-10 to SAVINGS):",e)    
    
    try:
      user.withdraw(AccountType.SAVINGS, 1000); #this will cause an Exception or Error
    except Exception as e:
       print("Test withdraw 1 (1000 from SAVINGS):",e); #print the message for the Exeption

    try:
      user.withdraw(AccountType.SAVINGS, -1); #this will cause an Exception or Error
    except Exception as e:
       print("Test withdraw 2 (-1 from SAVINGS):",e); #print the message for the Exeption

    user.withdraw(AccountType.SAVINGS, 5); 
    print("Test withdraw 3 (5 from SAVINGS), current balance:",user.getBalance(AccountType.SAVINGS))

    
    try:
      user.getBalance(AccountType.CHECKING)
    except Exception as e:
      print("Test getBalance 2 (CHECKING):",e)
    
    try:
      user.deposit(AccountType.CHECKING, 10);
    except Exception as e:
      print("Test deposit 3 (10 to CHECKING):",e) 

    try:
      user.withdraw(AccountType.CHECKING, 10);
    except Exception as e:
      print("Test withdraw 4 (10 from CHECKING):",e)  


      print("Test addAcount 1 (adding SAVINGS):",e )

    print("Test __str__() 1:", user.__str__())


    user.addAccount(AccountType.CHECKING);

    print("Test addAccount 2 (__str__() After adding CHECKING):", user.__str__())
    print("Test addAccount 2 (getBalance After adding CHECKING):", user.getBalance(AccountType.CHECKING))

    user.deposit(AccountType.CHECKING, 100);
    print("Test __str__ in Class Bankaccount 1(CHECKING):", user.accounts[AccountType.CHECKING.name].__str__())
    user.deposit(AccountType.CHECKING, 100);
    print("Test __str__ in Class Bankaccount 2(SAVINGS):", user.accounts[AccountType.SAVINGS.name].__str__())

    user.deposit(AccountType.CHECKING, 100);
    print("Test __len__ in Class Bankaccount 1(SAVINGS, current balance):", user.accounts[AccountType.SAVINGS.name].__len__())
    
   
test_over_withdrawal();
