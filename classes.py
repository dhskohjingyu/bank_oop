class Account:
    def __init__(self, new_account_no, new_customer_name, new_balance):
        self.__account_no = new_account_no
        self.__customer_name = new_customer_name
        self.__balance = new_balance

    def get_account_no(self):
        return self.__account_no

    def get_customer_name(self):
        return self.__customer_name

    def get_balance(self):
        return self.__balance

    def set_account_no(self, change_account_no):
        self.__account_no = change_account_no

    def set_customer_name(self, change_customer_name):
        self.__customer_name = change_customer_name

    def set_balance(self, change_balance):
        self.__balance = change_balance

    def deposit(self, amount):
        self.set_balance(self.get_balance() + amount)

    def withdraw(self, amount):
        self.set_balance(self.get_balance() + amount)

    def display(self):
        print(self.__account_no)
        print(self.__customer_name)
        print(self.__balance)

class CurrentAccount(Account):
    def __init__(self, new_account_no, new_customer_name, new_balance):
        super().__init__(new_account_no, new_customer_name, new_balance)
    
    def display_monthly_statement(self):
        super().display()

class SavingAccount(Account):
    def __init__(self, new_account_no, new_customer_name, new_balance):
        super().__init__(new_account_no, new_customer_name, new_balance)
        self.__interest = 0.01/12

    def display(self):
        super().display()
        #print(self.__department)

    def display_monthly_statement(self):
        self.set_balance(self.get_balance() * (1 + self.__interest))
        super().display()
        
