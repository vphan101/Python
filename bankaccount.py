print("\t\t\t***** Bank of Vinh *****")

print("\t\t----- Main Menu -----")

bank_data = {}
user_data = {}


while True:
    ch = int(input("""\n\n1. New Customer\n2. Existing Customer\n3. Exit\n\nEnter choice:"""))

    if ch ==1:
        name = input("Enter name:")
        city = input("Enter city:")
        email = input("Enter email:")
        age = int(input("Enter age:"))
        acc_type = input("Enter account type:")
        amt = int(input("Enter initial amount:$ "))
        acc_no = int(input("Enter account number:"))

        user_data["name"] = name
        user_data["city"] = city
        user_data["age"] = age
        user_data["acc_type"] = acc_type
        user_data["account_number"] = amt

        bank_data["account_number"] = acc_no
        bank_data["detail"] = user_data

        print("\n-----Account created successfully-----")

    elif ch == 2:
        acc_no = int(input("Enter account number:"))

        if acc_no in bank_data["account_number"]:
            print("\n----Account Exists----\n")

            u_ch = int(input("\n1.Check Balance\n2 Withdraw\n3.Deposit\n4.Back to main menu\n\nEnter choice:"))

            if u_ch == 1:
                print("Your available balance:",bank_data["detail"]["amount"])

            elif u_ch ==2:
                w_amt = int(input("Enter the amount you wish to withdrawal:"))
                bank_data["account_number"]["amount"] = bank_data["detail"]["amount"] - w_amt
                print("Amount withdrawn")

            elif u_ch ==3:
                d_amt = int(input("Enter the amount you wish to deposit:"))
                bank_data["account_number"]["amount"] = bank_data["detail"]["amount"] + d_amt
                print("\n-----Amount Deposited-----")
                
            elif u_ch ==4:
                break
            else:
                print("\nInvalid Input")

        else:
            print("\n-----Account does not exists-----")

    elif ch == 3:
        break

    else:
        print("\nInvalid Input")

print("\n\n***** Thank You for banking with Us *****")
