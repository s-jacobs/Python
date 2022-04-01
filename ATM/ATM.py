class Customer:
    next = 100

    def __init__(self, name):
        self.name = name
        self.custId = Customer.next
        Customer.next += 1

    def __repr__(self):
        return "Customer ID: " + str(self.custId) + "\nName: " + self.name

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getId(self):
        return self.custId

    # def setId(self, newId):
    #    self.custId = newId


# end class Customer


class Operator:
    next = 100

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password
        self.opId = Operator.next
        Operator.next += 1

    def __repr__(self):
        return "Operator ID: " + str(self.opId) + "\nName: " + self.name + "\nUser: " + self.user

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getUser(self):
        return self.user

    def setUser(self, newUser):
        self.user = newUser

    def getPass(self):
        return self.password

    def setPass(self, newPass):
        self.password = newPass

    def getId(self):
        return self.opId


class Account:
    next = 1000

    def __init__(self, cust, user, password, cBal, sBal):
        self.cust = cust
        self.user = user
        self.password = password
        self.cBal = cBal
        self.sBal = sBal
        self.acctNum = Account.next
        Account.next += 1

    def __repr__(self):
        return "Account Number: " + str(self.acctNum) + \
               "\nCust ID: " + str(self.cust.getId()) + "\nCustomer Name: " + self.cust.getName() + \
               "\nChecking Balance: " + str(self.cBal) + \
               "\nSavings Balance: " + str(self.sBal)

    def getAcctNum(self):
        return self.acctNum

    def setAcctNum(self, newAcctNum):
        self.acctNum = newAcctNum

    def getCust(self):
        return self.cust

    def setCust(self, newCust):
        self.cust = newCust

    def getUser(self):
        return self.user

    def setUser(self, newUser):
        self.user = newUser

    def getPass(self):
        return self.password

    def setPass(self, newPass):
        self.password = newPass

    def getcBal(self):
        return self.cBal

    def setcBal(self, newcBal):
        self.cBal = newcBal

    def getsBal(self):
        return self.sBal

    def setsBal(self, newsBal):
        self.sBal = newsBal


class Bills:
    def __init__(self, number, value):
        self.number = number
        self.value = value

    def __repr__(self):
        return "$" + str(self.value) + " - " + str(self.number)

    def getValue(self):
        return self.value

    def setValue(self, newValue):
        self.value = newValue

    def getNumber(self):
        return self.number

    def setNumber(self, newNum):
        self.number = newNum


# end class bills


# begin ServerCust
def custMenu(Id, custs, accts, bills):
    # print("in cust menu")
    cont = True
    choice = 0
    valid = False
    while cont:
        # print customer menu
        for c in custs:
            # print("in for " + str(c.getId()))
            if c.getId() == Id:
                print("\n\nWelcome " + c.getName() + "! What would you like to do?" +
                      "\n\n\t1. View Your balance " +
                      "\n\t2. Withdraw Money" +
                      "\n\t3. Deposit Money" +
                      "\n\t4. Transfer Money Between Checking and Savings Accounts" +
                      "\n\t5. Transfer Money From Your Checking Account to Another Checking Account" +
                      "\n\t6. Logout"
                      )

            # end if
        # end for

        valid = False
        while not valid:
            try:
                choice = int(input("CHOICE:  "))
                if choice < 1 or choice > 6:
                    print(
                        "\nError! Please enter the whole number in front of the menu option you would like to select (1-6)\n")
                    valid = False
                else:
                    valid = True
                    print("\n")
                # print("The Choice: " + str(choice))
                # switch for choice
                match choice:
                    case 1:
                        printBal(Id, accts, 1)
                    case 2:
                        withdraw(Id, accts, bills)
                    case 3:
                        print("three")
                    case 4:
                        print("four")
                    case 5:
                        print("five")
                    case 6:
                        print("You are officially logged out.\nThank you for banking with us! Have a nice day!\n\n")
                        cont = False
                        break

            except ValueError:
                print(
                    "\nError! Please enter the whole number in from of the menu option you would like to select (1-6)\n")
                valid = False
        # end while valid
    # end while cont


# end custMenu

def printBal(Id, acct, pType):
    # print("")
    if pType == 1:
        for a in acct:
            if a.getCust().getId() == Id:
                print("Your checking account balance is: " + str(a.getcBal()) +
                      "\nYour savings account balance is: " + str(a.getsBal()))
    elif pType == 2:
        for a in acct:
            if a.getCust().getId() == Id:
                print("\nYour account has been updated.\nYour checking account balance is: " + str(a.getcBal()) +
                      "\nYour savings account balance is: " + str(a.getsBal()))


# end printBal


def withdraw(Id, acct, bills):
    # print("withdraw")
    printBal(Id, acct, 1)
    choice = 0
    amtChoice = 0
    amt = 0
    valid = False
    validChoice = False

    while not valid:
        try:
            choice = int(input("\nWhich account do you want to withdraw from?" +
                               "\n\t1. Checking" +
                               "\n\t2. Savings" +
                               "\n\t3. Back to menu\nCHOICE: "))
            if choice < 1 or choice > 3:
                print("Error! Please enter either 1, 2, or 3.\nTry again...")
                valid = False
            else:
                valid = True
        except ValueError:
            print("Error! Please enter either 1, 2, or 3.\nTry again...")
            valid = False

        if choice != 3:
            validChoice = False

            while not validChoice:
                try:
                    amtChoice = int(input("\nHow much do you want to withdraw:" +
                                          "\n\t1. $10\n\t2. $20\n\t3. $50\n\t4. $100\n\t5. Cancel\n\nCHOICE: "))
                    if amtChoice < 1 or amtChoice > 5:
                        print("\nError! Please enter a number 1-5.\nTry again...")
                        validChoice = False
                    else:
                        validChoice = True
                except ValueError:
                    print("\nError! Please enter a number 1-5.\nTry again...")
                    validChoice = False
            # end while validChoice

            billsValid = True
            acctValid = True

            match amtChoice:
                case 1:
                    amt = 10
                    fiveBills = bills[0].getNumber()
                    if fiveBills < 2:
                        print("Error! Not enough money in ATM. Please see teller inside for funds."+
                              "\nAccount has not been updated")
                        billsValid = False
                    else:
                        acctValid = withdrawFromAcct(acct, amt, choice, Id)
                        if acctValid:
                            bills[0].setNumber(fiveBills-2)
                case 2:
                    amt = 20
                    twBills = bills[1].getNumber()
                    if twBills < 2:
                        print("Error! Not enough money in ATM. Please see teller inside for funds." +
                              "\nAccount has not been updated")
                        billsValid = False
                    else:
                        acctValid = withdrawFromAcct(acct, amt, choice, Id)
                        if acctValid:
                            bills[1].setNumber(twBills-1)
                case 3:
                    amt = 50
                    fifBills = bills[2].getNumber()
                    if fifBills < 2:
                        print("Error! Not enough money in ATM. Please see teller inside for funds." +
                              "\nAccount has not been updated")
                        billsValid = False
                    else:
                        acctValid = withdrawFromAcct(acct, amt, choice, Id)
                        if acctValid:
                            bills[2].setNumber(fifBills - 1)
                case 4:
                    amt = 100
                    hunBills = bills[3].getNumber()
                    if hunBills < 2:
                        print("Error! Not enough money in ATM. Please see teller inside for funds." +
                              "\nAccount has not been updated")
                        billsValid = False
                    else:
                        acctValid = withdrawFromAcct(acct, amt, choice, Id)
                        if acctValid:
                            bills[3].setNumber(hunBills - 1)
            # end match

            if amtChoice == 5:
                print("\nReturning to main menu...\n\n")
            else:
                if not billsValid:
                    printBal(Id, acct, 1)
                else:
                    printBal(Id, acct, 2)
        # end if choice not 3

    # end while not valid

# end withdraw


def withdrawFromAcct(acct, amt, choice, Id):
    valid = True

    for a in acct:
        if a.getCust().getId() == Id:
            # Withdraw from checking
            if choice == 1:
                print("checking")
                oldBal = a.getcBal()
                if amt < oldBal:
                    newBal = oldBal - amt
                    a.setcBal(newBal)
                    valid = True
                # end if amt < oldBal
                else:
                    print("Error! Insufficient account funds.\n")
                    valid = False
            elif choice == 2:
                print("savings")
                # Withdraw from savings
                oldBal = a.getsBal()
                if amt < oldBal:
                    newBal = oldBal - amt
                    a.setsBal(newBal)
                    valid = True
                # end if amt < oldBal
                else:
                    print("Error! Insufficient account funds.\n")
                    valid = False
            # end if/elif choice
        # end if id = id
    # end for acct
    return valid
# end withdrawFromAcct
# -------------------- end ServerCust --------------------


def loadBills():
    b = list()
    b.append(Bills(100, 5))
    b.append(Bills(100, 20))
    b.append(Bills(100, 50))
    b.append(Bills(100, 100))
    return b


def loadCust():
    c = list()
    c.append(Customer("John Doe"))
    c.append(Customer("Jane Doe"))
    c.append(Customer("Paul Jones"))
    c.append(Customer("Mike Jones"))
    c.append(Customer("Peter Thomas"))
    c.append(Customer("June Kelly"))
    c.append(Customer("Roger Nelson"))
    c.append(Customer("Joseph Jackson"))
    c.append(Customer("Elizabeth Houston"))
    c.append(Customer("Louise Ciccone"))
    return c


def loadAcct(c):
    a = list()
    a.append(Account(c[0], "JoDoe", "pass", 15000, 6000))
    a.append(Account(c[1], "jadoe", "1234", 20000, 10000))
    a.append(Account(c[2], "pjones", "2345", 10000, 1000))
    a.append(Account(c[3], "mikejones", "3456", 10000, 5000))
    a.append(Account(c[4], "pthomas", "4567", 12000, 7000))
    a.append(Account(c[5], "jKelly", "5678", 40000, 6000))
    a.append(Account(c[6], "rnelson", "7891", 13000, 8000))
    a.append(Account(c[7], "joeJack", "8910", 50000, 8000))
    a.append(Account(c[8], "lizhouston", "9101", 70000, 7000))
    a.append(Account(c[9], "lciccone", "1011", 30000, 10000))

    return a


def loadOper():
    o = list()
    o.append(Operator("Richard Bobby", "admin", "pass"))
    o.append(Operator("Sandy Patrick", "oper", "1234"))
    return o


def custLogin(acct):
    Id = 0
    found = False

    while not found:
        user = input("\nEnter your username (or -999 to return to the main menu): ")
        if user == "-999":
            break

        Pass = input("\nEnter your password: ")

        # validate user and pass
        for a in acct:
            if a.getUser() == user and a.getPass() == Pass:
                Id = a.getCust().getId()
                found = True
        # end for

        if not found:
            print("\nInvalid username or password.\nPlease try again.")

    # end while found
    return Id


# end custLogin


def main():
    b = loadBills()
    c = loadCust()
    a = loadAcct(c)
    o = loadOper()

    who = 0
    valid = False
    cont = True
    Id = -1

    # while loop for cont
    while cont:
        print("Hello! Welcome to this bank!\nPress:\n\t1. For Customers\n\t2. For Operators")
        #   while loop for valid who
        while not valid:
            try:
                who = int(input("CHOICE: "))
                if who < 1 or who > 2:
                    print(
                        "\nError! Please enter the whole number in from of the menu option you would like to select (1 or 2)" +
                        "\nTry again...\n\t1. For Customers\n\t2. For Operators")
                    valid = False
                else:
                    valid = True
            except ValueError:
                print(
                    "\nError! Please enter the whole number in from of the menu option you would like to select (1 or 2)" +
                    "\nTry again...\n\t1. For Customers\n\t2. For Operators")
                valid = False
        # end while valid

        match who:
            case 1:
                Id = custLogin(a)

        if Id != 0 and Id != -999:
            custMenu(Id, c, a, b)

        # print("ID: " + str(Id))
        valid = False
    # end while cont
    # custMenu(c[7].getId(), c, a, b)

    """
    print(b)
    for cust in c:
        print("\n" + cust.__repr__())
    print("\n")
    for acct in a:
        print("\n" + acct.__repr__())
    print("\n")
    for oper in o:
        print("\n" + oper.__repr__())
    """


main()
"""
cust1 = Customer("Bob")
print(cust1)
print("")
cust2 = Customer("Sally")
print(cust2)
"""

"""
print("")
five = Bills(10, 5)
ten = Bills(20, 10)
twenty = Bills(30, 20)

print(five)
print(ten)
print(twenty)

print("")
op1 = Operator("Jane", "jdoe", "1234abc")
op2 = Operator("Dave", "jdoe", "5678def")
op3 = Operator("Jim", "jimjim", "91011ghi")
print(op1)
print("")
print(op2)
print("")
print(op3)


print("")
acct1 = Account(cust1, "bb", "abc123", 54, 62)
print(acct1)
acct1.setCust(cust2)
print("")
print(acct1)
"""
