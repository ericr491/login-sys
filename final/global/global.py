#!/usr/bin/python
print "Content-Type: text/html\n\n"
print ""


import cgi, cgitb, base64

htmlStrr = ""
htmlStr = ""
ctr = 0

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

# just equations to calculate the answers to questions

def q1():
    value = d['TEXTHERE1']        # data from an article
    if value < 100000:
        newvalue = 1
    elif 30000 < value < 99999:
        newvalue = (value / 10000) * 0.5
    else:
        newvalue = (value / 1250) * 0.5
    return '<b>' +(str(newvalue)) + '</b>'

def q2():
    value = d['TEXTHERE2']         # data from article
    newvalue = (25 - value) * 12652
    return '<b>' + (str(newvalue)) + '</b>'

def q3():
    value = d['TEXTHERE3']           # data from charity
    newvalue = value / 0.14
    return '<b>' + (str(newvalue)) + '</b>'

def q4():
    value = d['TEXTHERE4']         # data from article
    newvalue = value * 2783150
    return '<b>' + (str(newvalue)) + '</b>'

def q5():
    value = d['TEXTHERE5']          # data from graph
    newvalue = 2.3121 * value
    return '<b>' +(str(newvalue)) + '</b>'

"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

htmlStr += "<html><head><title> Global! </title></head></html>\n"
htmlStr += '<a href= "../global/global"> link back to global questions </a><br>'   # creates a hyperlink
htmlStr += '<body bgcolor="#7FDBFF"><br><br>'

info__ = ''

if d.has_key('TEXTHERE1') and ctr == 0:       # if theres an input for Q1 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE1']) + ","
    htmlStr += "Q1: This is the chance of you being at proverty base on your income, " + q1() + "%." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE2') and ctr == 0:       # if theres an input for Q2 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE2']) + ","
    htmlStr += "Q2: The average income base on your age, $" + q2() + "." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE3') and ctr == 0:       # if theres an input for Q3 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE3']) + ","
    htmlStr += "Q3: " + q3() + " bottles of clean water will be provided to those in need." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE4') and ctr == 0:       # if theres an input for Q4 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE4']) + ","
    htmlStr += "Q4: Trade between nations will be increased by " + q4() + " kilograms per year." + "<br><br>"
else:
    info__ += " ,"

if d.has_key('TEXTHERE5') and ctr == 0:      # if theres an input for Q5 then the function add the string onto htmlStr
    info__ += str(d['TEXTHERE5']) + ","
    htmlStr += "Q5: Based on current trends the price of oil barrels will drop by " + q5() + "%." + "<br><br>"
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
