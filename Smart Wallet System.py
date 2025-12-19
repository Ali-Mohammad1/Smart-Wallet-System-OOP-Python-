import re
import random
import string

print("Hello, Smart Wallet System!".center(50, '-'))

class SmartWallet:
    Normal_Members = 0

    def __init__(self, name, balance=0):
        self._name = name
        self._balance = float(balance)
        # Generate a random 5-character password
        pwd = "".join(random.choices(string.printable, k=5))
        self._password = pwd
        SmartWallet.Normal_Members += 1
    
    def check_password(self):
        answer = input("Enter wallet password to access: ")
        return answer == ''.join(self._password)
    
    @property
    def name(self):
        return self._name

    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if self.check_password():
            if value >= 0:
                self._balance = value
            else:
                raise ValueError("Balance cannot be negative")
        else:
            raise ValueError("Incorrect password")
    
    @name.setter
    def name(self, value):
        if self.check_password():
            self._name = value
        else:
            raise ValueError("Incorrect password")
    
    @name.deleter
    def name(self):
        if self.check_password():
            del self._name
        else:
            raise ValueError("Incorrect password")

    @balance.deleter
    def balance(self):  
        if self.check_password():
            del self._balance
        else:
            raise ValueError("Incorrect password")

    #-- Comparison Operators
    def __eq__(self, other):
        return self._balance == other._balance
    
    def __lt__(self, other):
        return self._balance < other._balance

    def __gt__(self, other):
        return self._balance > other._balance
    
    def __ge__(self, other):
        return self._balance >= other._balance

    def __le__(self, other):
        return self._balance <= other._balance
    
    def __add__(self, other):
        return self._balance + other._balance
    
    def __sub__(self, other):
        return self._balance - other._balance
    
    def __len__(self):
        return len(self._name)
    
    # Display wallet information
    def display_info(self):
        print(f"Wallet Name: {self._name}")
        print(f"Wallet Balance: {self._balance}")
        print(f"Wallet Password: {self._password}")
    
    #-- String Representation
    def __str__(self):
        return f"Wallet '{self._name}' has balance: {self._balance}"
    
    #-- Class Method to create new wallet from string
    @classmethod
    def new_wallet(cls, information):
        name, balance = re.split(r',\s*', information)
        balance = float(balance)
        return cls(name, balance)
    
    #-- Static Method to provide usage instructions
    @staticmethod
    def how_to_use():
        return "To use the Smart Wallet System, create a wallet with a name and initial balance. Use the password to modify attributes."


#-- Subclass for VIP Wallet with interest rate
class VIPWallet(SmartWallet):
    VIP_Members = 0

    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self._interest_rate = interest_rate
        VIPWallet.VIP_Members += 1
        print("VIP Wallet created successfully!")
    
    @property
    def interest_rate(self):
        return self._interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if self.check_password():
            self._interest_rate = value
            print("✅ Interest rate updated.")
        else:
            raise ValueError("Incorrect password")

    @SmartWallet.name.setter
    def name(self, value):
        if self.check_password():
            self._name = value
            print("✅ Name updated.")
        else:
            raise ValueError("Incorrect password")

    @SmartWallet.balance.setter
    def balance(self, value):
        if self.check_password():
            self._balance = value
            print("✅ Balance updated.")
        else:
            raise ValueError("Incorrect password")

    def display_info(self):
        print(f"VIP Wallet Name: {self._name}")
        print(f"VIP Wallet Balance: {self._balance}")
        print(f"VIP Wallet Interest Rate: {self._interest_rate}")
        print(f"VIP Wallet Password: {self._password}")

    #-- String Representation
    def __str__(self):
        return (f"VIP Wallet Details:\n"
                f"Name: {self._name} (VIP)\n"
                f"Balance: {self._balance}\n"
                f"Interest Rate: {self._interest_rate}")
    
    #-- Class Method to create new VIP wallet from existing wallet
    @classmethod
    def promote_to_vip(cls, other):
        print("To promote, you must pay 1000 units as a VIP fee.")
        reply = input("Do you want to proceed? (yes/no): ")
        if reply.lower() != 'yes':
            print("Promotion to VIP cancelled.")
            return None
        return cls(other._name, other._balance - 1000, interest_rate=0.05)
    
    @staticmethod
    def how_to_use():
        return "To use the VIP Smart Wallet System, create/promote a wallet. Access attributes using the assigned password."

# --- TESTING THE CLASSES ---

# 1. Creating a normal wallet
wallet1 = SmartWallet("Alice", 5000)

# 2. Promoting to VIP
vip_wallet2 = VIPWallet.promote_to_vip(wallet1)

if vip_wallet2:
    vip_wallet2.display_info()
    
    # 3. Testing property setters (Will trigger password prompt)
    try:
        vip_wallet2.balance = 500 
        print(vip_wallet2)
    except ValueError as e:
        print(f"Error: {e}")
