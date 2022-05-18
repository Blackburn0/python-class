#generate a password that is hard to break


import random

lower_case = "abcdefghijklmnopqrstvuwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
number = "0123456789"
symbols = "@#$%&*/\?"

Use_for = lower_case + upper_case + number + symbols
length_for_pass = 10

password = "".join(random.sample(Use_for, length_for_pass))

print("your password is :", (password))