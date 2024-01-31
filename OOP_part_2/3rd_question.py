"""
Create a simple personal budgeting program using everything learned.
"""


class Entry:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount

    def __repr__(self):
        return f"{self.type}: {self.amount}"


class Budget:
    def __init__(self):
        self.book = []
        self.balance = 0

    def add_income(self):
        amount = int(input("Enter amount: "))
        entry = Entry("Income", amount)
        self.book.append(entry)
        self.balance += amount

    def add_expense(self):
        amount = int(input("Enter amount: "))
        entry = Entry("Expense", amount)
        self.book.append(entry)
        self.balance -= amount

    def show_book(self):
        print(budget.book)


budget = Budget()

while True:

    usr_input = int(input("\nChoose an option: \n\n1. Add income.\n2. Add expenses\n3. View book\n4. View balance\n5. "
                          "Exit program.\n\nChoice: "))

    match usr_input:
        case 1:
            budget.add_income()
        case 2:
            budget.add_expense()
        case 3:
            budget.show_book()
        case 4:
            print(budget.balance)
        case 5:
            break