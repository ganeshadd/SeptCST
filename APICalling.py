#Import Library
from openai import OpenAI

#Established connection
client =OpenAI(api_key="Your_Key_Here")

def call_llm(prompt):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )
    return response.output_text

user_input=input("Enter your instructions: ")

print("## User input ## \n")
print(user_input)

result =call_llm(user_input)
print("\n ##AI Response ## \n")
print(result)