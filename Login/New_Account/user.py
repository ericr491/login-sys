#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

# Python Script to make new users

import cgi, cgitb, base64

def split():
    d = {}
    cgi.FieldStorage()  # returns a mutant dictionary
    foo = cgi.FieldStorage()  # obtain the query string
    # print foo.keys()   diag output
    for k in foo.keys():
        d[k] = foo[k].value  # makes a new dict that has the values
    return d

# Defines variables based on query string, functions are self explanatory
Storage = split()
username = None   # sets a temporary value to user
password = None  #  sets a temporar value to password
password1 = None  # the retype confirmation password
if "Username" in Storage:   # if a username is type into the field, it creates a var
    username = Storage["Username"]
if "Password" in Storage: # if a password exists, it creates a var
    password = base64.b64encode(Storage["Password"])
if "Password1" in Storage: # if a reconfirmation password exists, it creates a var
    password1 = base64.b64encode(Storage["Password1"])


def sublistify(lines):  # Sublistifies data from CSV file
    overall = []
    for x in lines:
        this_line = x.split(",") # splits the csv by the comma, add adds each word which is now apart of list into overall
        overall += [this_line]
    return overall


def newAccount(username, password):
    file_ = open("../users.csv", "a+")  # opens the users.csv in a+ mode, which appends at the end of the file and creates a
    # new file if none exists
    accounts = sublistify(file_.readlines())  # creates a pairing of username and password, bc its in readline mode
    value = "Not_Exist"
    for x in accounts:
        if x[0] == username:  # if the username is equal to the username in the csv file, then it prints user "Exists"
            value = "Exists"
    if value == "Not_Exist":  # if its a new account, and all the parameters is inputed correctly, then it writes
        # the new account onto the file
        if password == password1:
            file_.write(username + ',' + password + "\n")
            print "<b>Success!</b>"
        else:
            print "Passwords did not match in both fields."
    else:
        print "Account with that username already exists, please select another username."
    file_.close()

if username != None and password != None and password1 != None:
    if "," in password or "," in password1 or "," in username: #handles commas
        print "No commas!"
    else:
        newAccount(username, password)
else:
    print "Please fill all fields"

print "<!DOCTYPE html><html><head><title>Login Info</title></head><body>"
print '<br><a href="../../index.html">' + \
      "Click to Return to the Homepage</a>"
