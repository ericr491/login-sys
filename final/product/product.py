#!/usr/bin/python
print "Content-Type: text/html\n\n"
print ""

import cgi, base64, cgitb

htmlStrr = ""
ctr = 0
htmlStr = ""

d = {}
foo = cgi.FieldStorage()
for k in foo.keys():   # makes a dictionary of values containing the input# as key and your input as values
    d[k] = foo[k].value
for i in d: # turns the string values into int values
    try: # turns the string values into int values if the isinstance returns false
        d[i] = int(d[i]) # if this returns an error like if string is inputted, then it will try the exceptation
    except:
        if i != "Username" and i != "Password":
            htmlStrr += "Please input an integer!<br>"
            ctr += 1
    if i != "Username" and i != "Password":
        d[i] = int(d[i])


def q1():
    value = d['TEXTHERE1']        # data from an independent study
    if value >= 8:
        newvalue = 0
    else:
        newvalue = abs(8-value) * 18
    return '<b>' +(str(newvalue)) + '</b>'

def q2():
    value = d['TEXTHERE2']         # data from bank report
    if value >= 8:
        newvalue = 0
    else:
        newvalue = ( 1 - (abs(8 - value)) / 8.0) * 5880000000
    return '<b>' + (str(newvalue)) + '</b>'

def q3():
    value = d['TEXTHERE3']           # data from hourly wages
    newvalue = 300000000 * value * 11
    return '<b>' + (str(newvalue)) + '</b>'

def q4():
    value = d['TEXTHERE4']         # data from hourly wages
    newvalue = 300000000 * value * 16
    return '<b>' + (str(newvalue)) + '</b>'

def q5():
    value = d['TEXTHERE5']          # data from hourly wages
    newvalue = 300000000 * (value / 60.0) * 11
    return '<b>' +(str(newvalue)) + '</b>'

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

htmlStr += "<html><head><title> Productivity! </title></head></html>\n"
htmlStr += '<a href= "../product/product"> link back to productivity questions </a><br>'   # creates a hyperlink
htmlStr += '<body bgcolor="#7FDBFF"><br><br>'

info__ = ""

if d.has_key('TEXTHERE1') and ctr == 0:       # if theres an input for Q1 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE1']) + ","
    htmlStr += "Q1: Work productivity in companies will drop by " + q1() + "%." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE2') and ctr == 0:       # if theres an input for Q2 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE2']) + ","
    htmlStr += "Q2: The economy will suffers by $" + q2() + " a year." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE3') and ctr == 0:       # if theres an input for Q3 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE3']) + ","
    htmlStr += "Q3: Collectively the GDP could have been increased by $" + q3() + "." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE4') and ctr == 0:       # if theres an input for Q4 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE4']) + ","
    htmlStr += "Q4: Collectively employers would have to pay $" + q4() + "." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE5') and ctr == 0:      # if theres an input for Q5 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE5']) + ","
    htmlStr += "Q5: If the minutes were paid, collectively it would cost $" + q5() + "."
else:
    info__ += " ,"

htmlStr += htmlStrr
htmlStr += '</body>'
htmlStr += "</html>"

#Account section of code (to save data)
username = None
password = None

if d.has_key('Username'):
    username = d["Username"]
if d.has_key('Password'):
    password = d["Password"]

info__ = info__.strip(',') + "\n"

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

def checkInfo(username_, password_): #Checks login info against user file
    info = open("../../Login/users.csv", "r")
    info_ = sublistify(info.readlines())
    info.close()
    for x in info_:
        if username_ in x:
            if password_ in base64.b64decode(x[1]):
		return True
            else:
                return "Wrong Password"
    return "User does not exist"
    
def writeInfo():
    file_ = open("Info.csv", "a")
    file_.write(username + "," + info__)
    file_.close()

def output(value): #Takes action based on password information
    if value == True:
        writeInfo() #Html code to redirect to proper account info
        print '<br><br><b>Data saved successfully</b>'
    else:
	print "<br><br><b>" + value + '</b>'

def user():
    output(checkInfo(username, password))

print htmlStr
if username != None and password != None:
    user()
else:
    print "<br><br><b>Data was not saved due to information missing in the fields</b>"

