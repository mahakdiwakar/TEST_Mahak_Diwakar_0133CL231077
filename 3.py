# Q3. Create abstract class Payment
# Abstract methods: pay() and receipt()
# Create child classes:
# GPay
# CreditCard
# Implement all methods and test them.

from abc import ABC, abstractmethod
import datetime

class Payment(ABC):
    
    
    @abstractmethod
    def pay(self, amount: float) -> bool:
        
        pass

    @abstractmethod
    def receipt(self, amount: float) -> None:
        
        pass


class GPay(Payment):
    
    
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def pay(self, amount: float) -> bool:
        if amount <= 0:
            print("[GPay] Error: Payment amount must be greater than zero.")
            return False
        print(f"[GPay] Processing payment of Rs. {amount:.2f} using mobile number {self.phone_number}...")
        print("[GPay] Payment Successful! UPI transaction completed.")
        return True

    def receipt(self, amount: float) -> None:
        print("\n" + "="*30)
        print("          GPAY RECEIPT          ")
        print("="*30)
        print(f"Date/Time : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Mobile No : {self.phone_number}")
        print(f"Amount    : Rs. {amount:.2f}")
        print(f"Status    : SUCCESS")
        print("="*30 + "\n")


class CreditCard(Payment):
    
    
    def __init__(self, card_holder: str, card_number: str):
        self.card_holder = card_holder

        self.masked_card_number = f"xxxx-xxxx-xxxx-{card_number[-4:]}" if len(card_number) >= 4 else card_number

    def pay(self, amount: float) -> bool:
        if amount <= 0:
            print("[CreditCard] Error: Payment amount must be greater than zero.")
            return False
        print(f"[CreditCard] Processing credit card payment of Rs. {amount:.2f}...")
        print(f"[CreditCard] Verifying card holder: {self.card_holder}...")
        print(f"[CreditCard] Card {self.masked_card_number} Authorized. Payment Successful!")
        return True

    def receipt(self, amount: float) -> None:
        print("\n" + "="*30)
        print("      CREDIT CARD RECEIPT       ")
        print("="*30)
        print(f"Date/Time : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"CardHolder: {self.card_holder}")
        print(f"Card No   : {self.masked_card_number}")
        print(f"Amount    : Rs. {amount:.2f}")
        print(f"Status    : APPROVED")
        print("="*30 + "\n")



if __name__ == "__main__":
    print("--- Testing Abstract Payment System ---")

    
    print("\n--- GPay Transaction ---")
    gpay_payment = GPay("9876543210")
    gpay_amount = 1500.50
    if gpay_payment.pay(gpay_amount):
        gpay_payment.receipt(gpay_amount)

    
    print("\n--- Credit Card Transaction ---")
    cc_payment = CreditCard("Alice Johnson", "1234567812345678")
    cc_amount = 4999.00
    if cc_payment.pay(cc_amount):
        cc_payment.receipt(cc_amount)

    
    print("\n--- Testing Edge Case (Invalid Amount) ---")
    invalid_payment = GPay("9876543210")
    invalid_payment.pay(-100.0)
