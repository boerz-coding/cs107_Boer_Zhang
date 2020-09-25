def make_withdrawal(balance):
    def inner(withdraw):
        if withdraw<0:
            print("wrong:withdraw<0")
            return None
        if withdraw>balance:
            print("wrong:withdraw>balance")
            return None
        balance=balance-withdraw
        return balance
    return inner

wd = make_withdrawal(100)
print("Not correct, will get an UnboundLocalError because no value has been bound to variable 'balance' in the scope of the inner function. It is only defined in the outer function, i.e. the enclosing function scope.")
print("From 100, withdraw 10:",wd(10))
print("Then withdraw 20:",wd(20))
