# Lists & Dictionaries — Structured Data

student1 ="Laya"
student2 ="Guru"
student3="Amulya"

#print(student1)
# 1-laya -0
# 2-Guru -1
#3-Amulya -2
#4.Gandhi -3

students =["Laya","Guru","Amulya","Gandhi"]
#print(students)

students[0]="Sunny"
#print(students)



User=["Ganesh",18,19,123.99,True]
User1=["Ramesh",22,99.99,False]

User1=[{"Name":"Ganesh",
       "Age":17,
       "Sector":19,
       "Score":123.99,
       "isActive":True},
       {"Name":"Ramesh",
        "Age":18,
        "Sector":19,
        "Score":99.99,
        "isActive":False},
        {"Name":"Sunny",
        "Age":20,
        "Sector":19,
        "Score":101.99,
        "isActive":False}]

SelectedUser=int(input("Enter the user index :"))
print(User1[SelectedUser]["Age"])
#User1[SelectedUser]["Score"] =input("Enter new Score for  :")
#print(User1[SelectedUser]["Score"])

Age = User1[SelectedUser][1]
Name =User1[SelectedUser][0]

if Age>=18:
    print(Name, " is eligible to vote")
else:
    print(Name, " is not eligible to vote")   


# 40 and above is Passed
# below 40 is failed 
# >40 = Pass    