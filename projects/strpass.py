import re
passwordregex = re.compile(r'''(^([a-z])
^([A-Z])
^([0-9])
.{8,})''', re.VERBOSE)
def passwordchecker(pw):
    if passwordregex.search(pw) == None:
        return False
    else:
        return True

password = input("Enter a password to check the strength: ")
if passwordchecker(password) is True:
    print("password is strong. ")
else:
    print("make your brain think for better one. ")
