# incapuslation
#protected, private, public

class Bank:
    def __init__(self, account, name, age):
        self.name = name
        self._age = age
        self.__account = account

    @property
    def get_account(self):
        return f'***' f'Current status: {self.__account}'

    @get_account.setter
    def get_account(self, money):
        self.__account += money
        return self.__account

    def add_cash(self):
        new_cash = float(input("Enter sum: "))
        get_acc = float(self.__account) + new_cash
        return get_acc


uln = Bank(155000, 'uLN', 24)
print(uln.get_account)
# print(uln.add_cash())
# print(uln.add_cash_2(24000))
uln.get_account = 23000
print(uln.get_account)


# print(uln.__account)
# print(dir(uln)) - gets the private string/data and other classes/function

# uln._Bank__account = _Bank__account
# print(uln._Bank__account)
# print(uln.name)
