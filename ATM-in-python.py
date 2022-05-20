name = input("What is your name? \n")
allowedUsers = ['Hamzat', 'Adebayo']
allowedPassword = ['hamzat','adebayo']

if(name in allowedUsers):
    password = input("Your password \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        print('These are the available services:')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select a service:'))
        Amount1 = 1000
        Amount2 = 2000
        Amount3 = 3000

        if(selectedOption == 1):
                    print('You selected option: %s' % selectedOption)
                    print('These are the available amount:')
                    print('1. 1000')
                    print('2. 2000')
                    print('3. 3000')
                    withdraw = int(input('Select the amount you want to withdraw:'))

                    if(withdraw == 1):
                        print('You have succesfull withdrawn %s' % Amount1)
                    elif(withdraw == 2):
                        print('You have succesfull withdrawn %s' % Amount2)
                    elif(withdraw == 3):
                        print('You have succesfull withdrawn %s' % Amount3)
                        
        if(selectedOption == 2):
                    print('You selected option: %s' % selectedOption)
                    print('How much would you like to deposit:')
                    print('1. 1000')
                    print('2. 2000')
                    print('3. 3000')
                    deposit = int(input('Select the amount you want to deposit:'))

                    if(deposit == 1):
                        print('You have succesfull deposited %s' % Amount1)
                    elif(deposit == 2):
                        print('You have succesfull deposited %s' % Amount2)
                    elif(deposit == 3):
                        print('You have succesfull deposited %s' % Amount3)
                    else:
                        print('Invalid Option selected, please try again')

        if(selectedOption == 3):
            print('You selected option: %s' % selectedOption)
            complaint = input('What is your complaint:')
            print('We have recieved your complaint and will get back to you soon')

    
    else:
        print('Password Incorrect, please try again')

else:
    print('Name not found, please try again')