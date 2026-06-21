import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)
passlen=12
charvalues = string.ascii_letters + string.digits + string.punctuation

password="".join([random.choice(charvalues) for i in range(passlen)])

# password= ""
# for i in range(passlen):
#     password += random.choice(charvalues)
print("your password is  :", password)



 