#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

#Python Script to make new users

import cgi, cgitb, base64
cgitb.enable()

def split():
    d = {}
    cgi.FieldStorage()  # returns a mutant dictionary
    foo = cgi.FieldStorage()  # obtain the query string
    # print foo.keys()   diag output
    for k in foo.keys():
        d[k] = foo[k].value  # makes a new dict that has the values
    return d

#Defines variables based on query string, functions are self explanatory
Storage = split()
username = None
password = None
password1 = None
password2 = None

if "Username" in Storage: #Next lines define strings based on QUERY
    username = Storage["Username"]
if "Password" in Storage:
    password = base64.b64encode(Storage["Password"])
if "Password1" in Storage:
    password1 = base64.b64encode(Storage["Password1"])
if "Password2" in Storage:
    password2 = base64.b64encode(Storage["Password2"])


def sublistify(lines): #Sublistifies data from CSV file
    overall = []
    for x in lines:
        this_line = x.split(",")
        ctr = 0
        while ctr < len(this_line):
            this_line[ctr] = this_line[ctr].strip()
            ctr += 1
        overall += [this_line]
    return overall

def changeAccount(username, password, password1, password2): #Takes inputs to change username's password to password 1
    file_ = open("../users.csv", "r")
    accounts = sublistify(file_.readlines())
    file_.close()
    value = None
    for x in accounts:
        if username in x:
            value = True
    if value != True:
        print "User does not exist."
    elif password1 != password2:
        print "New Passwords do not match."
    else:
        ctr = 0
        while ctr < len(accounts):
            if username in accounts[ctr]:
                if password == accounts[ctr][1]:
                    accounts[ctr][1] = password1
                    print "Success!"
                else:
                    print "Wrong Password"
            ctr += 1
    write_ = ""
    for x in accounts:
        this_line = ""
        for y in x:
            this_line += y + ","
        this_line = this_line.strip(",")
        this_line += "\n"
        write_ += this_line
    file__ = open("../users.csv", "w")
    file__.write(write_)
    file__.close()

if username != None and password != None and password1 != None and password2 != None: #Checks for all fields filled
    if "," in password or "," in password1 or "," in password2 or "," in username: #handles commas
        print "No commas!"
    else:
        changeAccount(username, password, password1, password2) #Runs code if error checks work properly
else:
    print "Please fill all fields"
    
print "<!DOCTYPE html><html><head><title>Login Info</title></head><body>"
print '<br><a href="../../index.html">' +\
      "Click to Return to the Homepage</a>"
