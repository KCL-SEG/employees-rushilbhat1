"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

        if name == 'Billie':
            self.salary = 4000
        elif name == 'Charlie':
            self.hourly_wage = 25
            self.hours_worked = 100
        elif name == 'Renee':
            self.salary = 3000
            self.contracts_landed = 4
            self.commission_per_contract = 200
        elif name == 'Jan':
            self.hourly_wage = 25
            self.hours_worked = 150
            self.contracts_landed = 3
            self.commission_per_contract = 220
        elif name == 'Robbie':
            self.salary = 2000
            self.bonus = 1500
        elif name == 'Ariel':
            self.hourly_wage = 30
            self.hours_worked = 120
            self.bonus = 600
        

    def get_pay(self):  
        total_pay = 0
        if hasattr(self, 'salary'):
            total_pay += self.salary
        else:
            total_pay += self.hourly_wage * self.hours_worked


        if hasattr(self, 'bonus'):
            total_pay += self.bonus
        elif hasattr(self, 'contracts_landed'):
            total_pay += self.contracts_landed * self.commission_per_contract

        return total_pay


    def __str__(self):
        description = f"{self.name} works on a "
        if hasattr(self, 'salary'):
            description += f"monthly salary of {self.salary}"
        else:
            description += f"contract of {self.hours_worked} hours at {self.hourly_wage}/hour"

        if hasattr(self, 'bonus'):
            description += f" and receives a bonus commission of {self.bonus}"
        elif hasattr(self, 'contracts_landed'):
            description += f" and receives a commission for {self.contracts_landed} contract(s) at {self.commission_per_contract}/contract"

        description += f". Their total pay is {self.get_pay()}."    
        return description



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
