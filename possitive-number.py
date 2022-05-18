user_no = input("Enter a number : ")
#  is used to check for errors and validation
try: 
    # runs input is valid
    user_no = float(user_no)
    print("You just enterd a number")

    if user_no >= 0:
        print("True")
    
    else:
        print("false")

except:
    # if input isinvalid
        # validation
        print("Oh, This is not a number")
