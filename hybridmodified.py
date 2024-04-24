class A:
    def magicalprime(self, a):
        print("Checking if it's a magical prime number")
        if a > 1:
            if all(a % i != 0 for i in range(2, a)):
                print("It's a magical prime number")
            else:
                print("It's not a magical prime number")
        else:
            print("It's not a magical prime number")


class B(A):
    def neon(self, a):
        print("Checking if it's a neon number")
        if a > 0:
            square = a * a
            if square == int(str(square)[::-1]):
                print("It's a neon number")
            else:
                print("It's not a neon number")
        else:
            print("It's not a neon number")


class C(A):
    def zpattern(self, name):
        print("Printing Z pattern for the name:", name)
        length = len(name)
        for i in range(length):
            for j in range(length):
                if i == 0 or i == length - 1 or i + j == length - 1:
                    print(name[j], end=" ")
                else:
                    print(" ", end=" ")
            print()


class D(A):
    def reverse_string(self, string):
        print("Reversed string:", string[::-1])


class E(B, C, D):
    def banking_transactions(self):
        account = {'balance': 1000, 'transactions': []}

        def withdraw(amount):
            if amount > account['balance']:
                print("Insufficient funds!")
            else:
                account['balance'] -= amount
                account['transactions'].append(f"Withdrawal: ${amount}")
                print(f"Withdrawal successful. Remaining balance: ${account['balance']}")

        def deposit(amount):
            account['balance'] += amount
            account['transactions'].append(f"Deposit: ${amount}")
            print(f"Deposit successful. Remaining balance: ${account['balance']}")

        def get_balance():
            return account['balance']

        def get_transaction_history():
            str1="\n".join([str(i) for i in account['transcations']])
            a=open("bankingtransaction.txt","w")
            a.write("Initial balace")
            a.write(str(bal))
            a.write("\n")
            a.write(str1)
            a.write("\n")
            a.write("Remaining Balance:$")
            a.write(str(account['balance']))
            a.write("\n")
            a.close()
            return account['transactions']

        choices = {'1': deposit, '2': withdraw, '3': get_balance, '4': get_transaction_history}

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '5':
                print("Exiting program.")
                break

            if choice in choices:
                if choice == '1' or choice == '2':
                    amount = float(input("Enter amount: "))
                    choices[choice](amount)
                else:
                    print(choices[choice]())
            else:
                print("Invalid choice. Please try again.")


# Example usage
e = E()
e.magicalprime(17)
e.neon(4)
e.zpattern("harindra")
e.reverse_string("harindra")
e.banking_transactions()
