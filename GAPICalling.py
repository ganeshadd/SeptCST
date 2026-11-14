from google import genai
#Remmoved the API key and added a place holder
API_KEY="Your API Key"

client =genai.Client(api_key=API_KEY)

def  call_llm(prompt):
    response =client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )
    return response.text

user_input=input("Enter your instructions: ")

print("## User input ## \n")
print(user_input)

result =call_llm(user_input)
print("\n ##AI Response ## \n")
print(result)