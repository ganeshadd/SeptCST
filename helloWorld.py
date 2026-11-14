# Intro to Python Session

#print("Hey Guys, Welcome to Python 101")


# Variable in python  
text1 = "Hello guys,Welcome to gen Ai session"
#print(text1)

text1 =25
#print(text1)

text1 = "Hello guys,Welcome to gen Ai session"
#print(text1)

fName =input("Enter your FirstName :")
lName = input("Enter your LastName :")
sessions =int(input("Enter how many session you have attended : "))
#Function

def calculateCost(sessions):
    cost =100
    trainingcost = (sessions)*(cost)
    return trainingcost

def fullName(fname,lname):
    output =fname+lname
    return output

result =calculateCost(sessions)
print(result)

result2=fullName(fName,lName)
print(result2)