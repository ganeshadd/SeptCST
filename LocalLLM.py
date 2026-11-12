#Add library
import ollama

#Establish a connection
def call_llm(input):
    response =ollama.chat(
        model="KalamSir",
        messages=[
            {
                "role":"user",
                "content":input
            }
        ]
    )
    return response["message"]["content"]

user_input=input("Enter your instructions: ")

print("## User input ## \n")
print(user_input)

result =call_llm(user_input)
print("\n ##AI Response ## \n")
print(result)