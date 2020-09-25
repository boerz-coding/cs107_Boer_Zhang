def make_withdrawal(balance):
    def inner(withdraw):
        if withdraw<0:
            print("wrong:withdraw<0")
            return None
        if withdraw>balance:
            print("wrong:withdraw>balance")
            return None
        return balance-withdraw
    return inner
wd = make_withdrawal(100)
print("From 100, withdraw 10:",wd(10))
print("Then withdraw 20:",wd(20))
print("Not correct, because the total balance is not reassigned during withdraw")
