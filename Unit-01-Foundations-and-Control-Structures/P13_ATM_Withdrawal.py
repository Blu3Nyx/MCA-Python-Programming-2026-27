# Unit 1 - P13
# Program to simulate ATM withdrawal

correct_pin = 1234

pin = int(input("Enter your PIN: "))

if pin != correct_pin:
    print("Wrong PIN! Transaction cancelled.")
else:
    balance = float(input("Enter your account balance: "))
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount! Please enter a positive amount.")
    elif amount % 100 != 0:
        print("Amount should be in multiples of 100.")
    elif amount > balance:
        print("Insufficient balance!")
    else:
        balance = balance - amount
        print("Transaction successful. Please collect your cash.")
        print("Remaining balance:", balance)
