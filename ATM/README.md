# ATM Machine
## Python Version

Program starts with the main menu that has two options  -  Login as a customer or login as an operator
For the customer menu choose 1
    You will be asked to login
        Customer logins for 10 accounts:
            -  JoDoe  -  pass
            -  jadoe  -  1234
            -  pjones  -  2345
            -  mikejones  -  3456
            -  pthomas  -  4567
            -  jKelly  -  5678
            -  coopNelson  -  6789
            -  rnelson  -  7891
            -  joeJack  -  8910
            -  lizhouston  -  9101
    Next the customer menu will load  -  choose an option 1-5 or 6 to logout
        1. View Your Balance  -  This will print out the customer checking and savings balance
            -  there are two types
                1. shows the original customer balance before any changes
                2. shows the customer balance after a change has been made (Ex. withdraw, deposit transfer)

        2. Withdraw Money  -  This allows the user to withdraw money from his or her either checking or savings account
            User will be prompted to choose which account to withdraw from (checking or savings) and the amount they wish to withdraw
                Program will validate user has enough funds in account and that ATM has enough bills
                    If not, user will be notified
                ** If the user wishes to cancel this withdraw, enter -999 on either prompt. Once both prompts are answered (not -999) withdraw can't be canceled
                

        3. Deposit Money  -  This allows the user to deposit money into his or her either checking or savings account
            User will be prompted to choose which account to deposit to (checking or savings) and the amount they wish to deposit
                ** If the user wishes to cancel this deposit, enter -999 on either prompt. Once both prompts are answered (not -999) the deposit can't be canceled 

        4. Transfer Between Your Checking and Savings  -  This allows the user to transfer funds between his or her checking and savings accounts
            User will be prompted to choose which account to transfer from and they amount they wish to transfer
                Program will validate user has enough funds in account
                    If not, user will be notified
                ** If the user wishes to cancel this transfer, enter -999 on either prompt. Once both prompts are answered (not -999) the transfer can't be canceled
        
        5. Transfer Between Your Checking Account to Another Checking Account
            User will be prompted to enter the account number they wish to transfer to and the amount to transfer
                Program will validate that the second account exists and user has enough funds in account
                    If not, user will be notified
                A summary of the transaction will show and user will be prompted to confirm that the information is correct before the transaction is completed
                    1. Confirm  -  transaction is completed
                    2. Cancel   -  transaction is NOT completed and user is sent back to customer main menu
            ** If the user wishes to cancel this transfer, enter -999 on either prompt. Once both prompts are answered (not -999), and the transaction is confirmed, it can't be canceled

        6. Logout  -  user is logged out and sent back to first menu (customer or operator login)

        
        
For the operator menu choose 2
    User will be asked to login
        admin  -  pass
        oper   -  1234

    Next operator main menu will load  -  Choose an option 1-3, 6 to logout, and 5 to shutdown the ATM (END/EXIT program)
        1. Display Number of Bills  -  This option displays the number of each bill in the ATM

        2. Add Bills to ATM  -  This allows the operator to add bills to the ATM
            Operator will be prompted to choose which bill they want to add and how many they are adding
                ** Choose option 5 on which bill menu to cancel and return to the operator main menu
            Operator will then be asked if they want to add more bills
                1. Yes  -  sent back to choose which bill they want to add
                2. No   -  display the new number of bills and return to operator main menu
            
        3. Remove Bills from ATM  -  This allows the operator to remove bills from the ATM
            Operator will be prompted to choose which bill they want to remove and how many
                ** Choose option 5 to cancel
                Program will validate that ATM has enough bills
                    If not, operator will be notified

        4. Shutdown ATM  -  This allows the operator to shutdown the ATM (END/EXIT program)
            Operator will be prompted to confirm shutdown
                1. Operator will be logged out and ATM will shut down
                2. Shutdown is canceled. Return to operator main menu

        5. Logout  -  Operator is logged out and sent back to first menu (customer or operator login)

