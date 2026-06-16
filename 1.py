# Q1. Create a class BankAccount with: (4 Marks)
# • Private variable __balance = 10000
# • Method deposit(amount) -> add to balance and print new balance
# • Method withdraw(amount) -> if amount > balance print 'Insufficient!', else deduct
# • Method get_balance() -> print current balance
# Create 2 objects and perform deposit and withdraw operations on both.

class BankAccount:
    
    def __init__(self, account_holder: str, initial_balance: float = 10000):
        # Private variable __balance, initialized to 10000 by default
        self.__balance = initial_balance
        self.account_holder = account_holder
        print(f"Account created for {self.account_holder} with initial balance of Rs. {self.__balance}")

    def deposit(self, amount: float) -> None:
        
        if amount > 0:
            self.__balance += amount
            print(f"Deposited Rs. {amount} to {self.account_holder}'s account. New Balance: Rs. {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount: float) -> None:
        
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
            
        if amount > self.__balance:
            print(f"Withdrawal of Rs. {amount} failed for {self.account_holder}: Insufficient!")
        else:
            self.__balance -= amount
            print(f"Withdrew Rs. {amount} from {self.account_holder}'s account. Remaining Balance: Rs. {self.__balance}")

    def get_balance(self) -> float:
        """
        Prints and returns the current balance.
        """
        print(f"Current balance of {self.account_holder}'s account: Rs. {self.__balance}")
        return self.__balance



if __name__ == "__main__":
    print("--- Testing BankAccount Class ---")
    
    
    print("\nCreating Account 1:")
    account1 = BankAccount("Alice")
    
    
    account1.get_balance()
    account1.deposit(2500)
    account1.withdraw(5000)
    account1.withdraw(10000)  
    account1.get_balance()
    
    
    print("\nCreating Account 2:")
    account2 = BankAccount("Bob", 10000)
    
    
    account2.get_balance()
    account2.withdraw(3000)
    account2.deposit(1500)
    account2.withdraw(9000)   
    account2.get_balance()
