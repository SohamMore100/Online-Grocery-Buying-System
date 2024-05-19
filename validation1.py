import re

#Name validation
def NameValidation(name):
    ptr='^[a-zA-Z\ ]+$'
    if re.match(ptr,name):
        return True
    else:
        return False

#Address validation
def AddressValidation(address):
    ptr='^[a-zA-Z0-9\,\s\-\,]'
    if re.match(ptr,address):
        return True
    else:
        return False

#Contact Validation
def ConatactValidation(contact):
    ptr='^[6-9]+[0-9]{9}'
    if re.match(ptr,contact):
        return True
    else:
        return False

#Email Validation
def EmailValidation(Email):
    ptr='^[a-z0-9\.\_]+@[a-z]+\.[com|org|in]+$'
    if re.match(ptr,Email):
        return True
    else:
        return False

#Password Validation
def PasswordValidation(password):
    if len(password)>=8:
        return True
    else:
        return 'Password length is less than 8'