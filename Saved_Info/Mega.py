#!/usr/bin/python
print "Content-Type: text/html\n\n"
print ""

print "<!DOCTYPE html><html><head><title>Account Info</title></head><header><a href='Mega.html'>Return to Login</a></header><body bgcolor='#7FDBFF'><br>"

import cgi, cgitb, base64

def split():
    d = {}
    cgi.FieldStorage()  # returns a mutant dictionary
    foo = cgi.FieldStorage()  # obtain the query string
    for k in foo.keys():
        d[k] = foo[k].value  # makes a new dict that has the values
    return d

Storage = split()
password = None     # temp assigned value
username = None     # temp assigned value

if "Username" in Storage:   # if there is a value, then the value is assigned to a var
    username = Storage["Username"]
if "Password" in Storage:
    password = base64.b64encode(Storage["Password"])  # encodes it

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

def retrieveAccountData():   # opens the users.csv to check account info
    file_ = open("../Login/users.csv", "r")
    accounts = sublistify(file_.readlines())
    file_.close()
    return accounts

accounts = retrieveAccountData()
final = None
if password == None or username == None:   # if there is an empty field, then it prints out return to login
    print "Missing Fields.<a href='Mega.html'> Return to Login Page</a>"
else:
    for x in accounts:
        if username in x:
            if password in x:
                final = username  # sets a var to passowrd, if it exists
            else:
                print "Wrong Password.<a href='Mega.html'> Return to Login Page</a>"
                ctr = 1
    if final == None and ctr != 1:
        print "This user does not exist.<a href='Mega.html'> Return to Login Page</a>"

def retrieveInfo():
    file_ = open("../final/environment/Info.csv", "r")   # opens the info from each of the info.csv files in r mode
    environment = sublistify(file_.readlines())
    file_.close()
    file__ = open("../final/global/Info.csv", "r")
    globe = sublistify(file__.readlines())
    file__.close()
    file___ = open("../final/population/Info.csv", "r")
    population = sublistify(file___.readlines())
    file___.close()
    file____ = open("../final/product/Info.csv", "r")
    product = sublistify(file____.readlines())
    file____.close()
    file_____ = open("../final/science/Info.csv", "r")
    science = sublistify(file_____.readlines())
    file_____.close()
    ctr = len(environment) # while there is something in the csv file
    while ctr > 0:   # final == username, so if the username is not in the csv file, it does that return the data
        # attributed to someone else username
        if final not in environment[ctr - 1]:
            del(environment[ctr - 1])
        ctr -= 1
    ctr = len(globe)
    while ctr > 0:
        if final not in globe[ctr - 1]:
            del(globe[ctr - 1])
        ctr -= 1
    ctr = len(population)
    while ctr > 0:
        if final not in population[ctr - 1]:
            del(population[ctr - 1])
        ctr -= 1
    ctr = len(product)
    while ctr > 0:
        if final not in product[ctr - 1]:
            del(product[ctr - 1])
        ctr -= 1
    ctr = len(science)
    while ctr > 0:
        if final not in science[ctr - 1]:
            del(science[ctr - 1])
        ctr -= 1
    if len(environment) == 0: # filler for empty list
        environment = [[' ',' ',' ',' ',' ',' ']]
    if len(globe) == 0:
        globe = [[' ',' ',' ',' ',' ',' ']]
    if len(population) == 0:
        population = [[' ',' ',' ',' ',' ',' ']]
    if len(product) == 0:
        product = [[' ',' ',' ',' ',' ',' ']]
    if len(science) == 0:
        science = [[' ',' ',' ',' ',' ',' ']]
    info = environment + globe + population + product + science
    return info
# the list is parralel, so everything fits in
def htmlTable(data):  # html code for the table
    line1 = "<table border='1'><tr><th>Paper Bags</th><th>Plastic Bags</th>" +\
            "<th>Metal Cans</th><th>Hours Walk</th><th>Chicken</th></tr>"
    line2 = "<tr>"
    for x in data[0][1:]:  # omitts the user from the final return table
        line2 += "<td>" + x + "</td>"  # puts the corresponding data inthe cell
    line2 += "</tr>"  # does it by a row, instead of column
    line3 = "</table>"
    table1 = "<b>Environment Stats</b><br>" + line1 + line2 + line3
    line1 = "<table border='1'><tr><th>Sleep</th><th>Sleep</th>" +\
            "<th>Lunch Break</th><th>Overtime</th><th>Commute</th></tr>"
    line2 = "<tr>"
    for x in data[1][1:]:
        line2 += "<td>" + x + "</td>"
    line2 += "</tr>"
    line3 = "</table>"
    table2 = "<br><br><b>Productivity Stats</b>" + line1 + line2 + line3
    line1 = "<table border='1'><tr><th>Family</th><th>Children</th>" +\
            "<th>Food</th><th>CO2</th><th>Water</th></tr>"
    line2 = "<tr>"
    for x in data[2][1:]:
        line2 += "<td>" + x + "</td>"
    line2 += "</tr>"
    line3 = "</table>"
    table3 = "<br><br><b>Population Stats</b>" + line1 + line2 + line3
    line1 = "<table border='1'><tr><th>Income</th><th>Age</th>" +\
            "<th>Lunch</th><th>Daily Trade</th><th>Oil Price</th></tr>"
    line2 = "<tr>"
    for x in data[3][1:]:   # data
        line2 += "<td>" + x + "</td>"
    line2 += "</tr>"
    line3 = "</table>"
    table4 = "<br><br><b>Global Politics Stats</b>" + line1 + line2 + line3
    line1 = "<table border='1'><tr><th>Vaccines</th><th>Wash Hands</th>" +\
            "<th>Space</th><th>Bacteria</th><th>English Speakers</th></tr>"
    line2 = "<tr>"
    for x in data[4][1:]:
        line2 += "<td>" + x + "</td>"
    line2 += "</tr>"
    line3 = "</table>"
    table5 = "<br><br><b>Science vs Culture Stats</b>" + line1 + line2 + line3
    print table1 + table2 + table3 + table4 + table5

if final != None:
    htmlTable(retrieveInfo())
