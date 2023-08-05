import random 

upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
number = "0123456789"
symbol = "-/:;()$&@'!?,._\|~<>€£¥•=+*^%#}{]["

var =  upper + lower + number + symbol
length = 20
password = "".join(random.sample(var,length))

print("Here is your Password Brodie 🫡: " + password)

