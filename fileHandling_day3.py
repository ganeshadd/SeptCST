#Open File
#Realtive : input.txt ,Knowledge\input2.txt
#Actual/absolute : C:\Users\ganes\SeptUST\input.txt
file =open("Knowledge\input2.txt","r")

#Read and store the content
content =file.read()

#close the connection/file
file.close()

print(content)
