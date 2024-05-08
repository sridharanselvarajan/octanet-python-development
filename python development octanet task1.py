class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.balance = 0
        self.transaction_history = []

    def authenticate(self, entered_pin):
        return self.pin == entered_pin

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
        else:
            print("Insufficient balance.")

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def transfer(self, recipient_id, amount):
        # Logic to transfer amount to another user
        pass


class ATM:
    def __init__(self, users):
        self.users = users
        self.current_user = None

    def login(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.authenticate(pin):
                self.current_user = user
                return True
        return False

    def display_menu(self):
        print("1. Display Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Transactions History")
        print("6. Quit")

    def perform_transaction(self, choice):
        if choice == 1:
            print("Balance:", self.current_user.get_balance())
        elif choice == 2:
            amount = float(input("Enter amount to withdraw: "))
            self.current_user.withdraw(amount)
        elif choice == 3:
            amount = float(input("Enter amount to deposit: "))
            self.current_user.deposit(amount)
        elif choice == 4:
            recipient_id = input("Enter recipient's user ID: ")
            amount = float(input("Enter amount to transfer: "))
            self.current_user.transfer(recipient_id, amount)
        elif choice == 5:
            print("Transaction History:", self.current_user.get_transaction_history())
        elif choice == 6:
            print("Exiting. Goodbye!")
            exit()


def main():
    # Sample users
    users = [User("12345", "1234"), User("67890", "5678")]

    atm = ATM(users)

    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")

    if atm.login(user_id, pin):
        print("Welcome!")
        while True:
            atm.display_menu()
            choice = int(input("Enter your choice: "))
            atm.perform_transaction(choice)
    else:
        print("Invalid user ID or PIN.")


if __name__ == "__main__":
    main()

