
# banking system App

lst=["deposit", "withdrawal", "balance"]
bank={"Azeez":1000,
       "Asif":1000,
        "Ahmed":1000}


class Banking:

    def transactions(self, history):
        with open('transactions_history2.txt','a') as trans_hty:
            trans_hty.write(history)
    def Deposits(self,deposit):
        deposit=float(deposit)
        self.transactions(f"{account_holder}\tinitial_bal: {str(bank[account_holder])}\t")
        bank["deposit"]=deposit
        bank[account_holder]=bank[account_holder] + bank['deposit']
        # bank['azeez]=sum(bank.values(), deposit)
        self.transactions(f"\tdeposited: {deposit}\t\tbalance: {bank[account_holder]}\n")
        print(f"Dear {account_holder}\nyou have applied for deposit to your account.\ndeposit amount {deposit} \nyour bank balance: {bank[account_holder]}")
            
    def Withdrawals(self,withdrawal):
        bank['withdrawal']=withdrawal
        self.transactions(f"{account_holder}\tinitial_bal: {str(bank[account_holder])}\t")
        val=bank[account_holder] - bank['withdrawal']
        bank[account_holder]=val  
        print(f"dear {account_holder} \nyou have applied for withdraw amount from your account.\n withdrawal amount is:{withdrawal}")
        print(f"your remaining balance: {bank[account_holder]}")
        self.transactions(f"\twithdrawal: {withdrawal}\t\tbalance: {bank[account_holder]}\n")

the_bank=Banking()
while True:
    account_holder=input("Enter the name of account holder:")
    account_holder=account_holder.capitalize()
    if account_holder in bank.keys():
        typee=input("what type of transaction do you want:")
        typee=typee.strip()
        if typee in lst:
            if typee == "deposit":
                deposit=int(input("how much do you what to deposit:"))
                the_bank.Deposits(deposit)
                continue


            elif typee == 'withdrawal':
                withdrawal=float(input("how much money do you to withdrawal:"))
                the_bank.Withdrawals(withdrawal)
                continue
            elif typee == 'balance':
                print(bank[account_holder])
                continue
            elif typee=="asdf":
                print("you entered wrong term")
                break
            else:
                print("you entered wrong term")
                continue

        else:
            print("incorrect transaction")
            continue
    else:
        print(f"{account_holder} is not in our database")
        break
try:
    deposits=the_bank.Deposits(deposit)
    withdrawals=the_bank.Withdrawals(withdrawal)
except:
    print("try again")

