#Import Library
from openai import OpenAI

#Established connection
client =OpenAI(api_key="Your API KEY")

def call_llm(prompt):
    response = client.responses.create(
        model="gpt-4.1-nano",
        input=user_input
    )
    return response.output_text

#Open the File

def upper_process(text):
    print("I am in Upper block")
    uppercase=text.upper()
    return uppercase

def Openfile():
    file_name =input("Enter the file Name:")
    with open(file_name,"r") as file:
        print("I am reading the file ",file_name)

        content =file.read()
    result=upper_process(content)
    print("::Processed Text::")
    print(result)

Openfile()    