# Unit 1 - P29
# Menu driven mathematical application
# Options: Prime, Palindrome, Armstrong, Factorial, Fibonacci, Exit

while True:
    print()
    print("===== MATH MENU =====")
    print("1. Check Prime")
    print("2. Check Palindrome")
    print("3. Check Armstrong")
    print("4. Factorial")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice (1-6): "))

    if choice == 1:
        n = int(input("Enter a number: "))
        is_prime = True
        if n <= 1:
            is_prime = False
        else:
            for i in range(2, n):
                if n % i == 0:
                    is_prime = False
                    break
        if is_prime:
            print(n, "is a prime number")
        else:
            print(n, "is not a prime number")

    elif choice == 2:
        n = int(input("Enter a number: "))
        temp = n
        rev = 0
        while temp > 0:
            rev = rev * 10 + temp % 10
            temp = temp // 10
        if rev == n:
            print(n, "is a palindrome")
        else:
            print(n, "is not a palindrome")

    elif choice == 3:
        n = int(input("Enter a number: "))
        count = len(str(n))
        temp = n
        total = 0
        while temp > 0:
            digit = temp % 10
            total = total + digit ** count
            temp = temp // 10
        if total == n:
            print(n, "is an Armstrong number")
        else:
            print(n, "is not an Armstrong number")

    elif choice == 4:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Factorial is not defined for negative numbers")
        else:
            fact = 1
            for i in range(1, n + 1):
                fact = fact * i
            print("Factorial of", n, "is", fact)

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a = 0
        b = 1
        print("Fibonacci series:")
        for i in range(n):
            print(a, end=" ")
            c = a + b
            a = b
            b = c
        print()

    elif choice == 6:
        print("Thank you! Exiting the program.")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
