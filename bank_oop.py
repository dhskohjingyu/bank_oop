from classes import *

if __name__ == "__main__":
    try:
        account_file = open("ACCOUNTS.DAT", "r")
        transaction_file = open("TRANSACTIONS.DAT", "r")

        account_lines = account_file.readlines()
        transaction_lines = transaction_file.readlines()

        for account_line in account_lines:
            account_line = account_line.rstrip("\n")
            
            account_no = account_line[0:6]
            account_type = account_no[0]
            customer_name = account_line[6:35]
            balance = float(account_line[36:])

            if(account_type == "S"):
                # create a saving account
                account = SavingAccount(account_no, customer_name, balance)
            else:
                # create a current account
                account = CurrentAccount(account_no, customer_name, balance)
                
            for transaction_line in transaction_lines:
                transaction_date = transaction_line[0:8]
                transaction_account = transaction_line[8:14]
                transaction_type = transaction_line[14:15]
                transaction_amount = float(transaction_line[15:])

                if transaction_account == account_no:
                    if transaction_type == "D":
                        account.deposit(transaction_amount)
                    else:
                        account.withdraw(transaction_amount)

            account.display_monthly_statement()
            print("\n")
            
        account_file.close()
        transaction_file.close()
    except IOError:
        print("Could not find or open ACCOUNTS.DAT")
