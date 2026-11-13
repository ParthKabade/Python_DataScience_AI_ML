from ollama import chat
import json

#prompt for LLM
prompt ="""Give me the information about python programming Language.
Return the result as JSON with these Keys:
language
type 
creator
version
"""
#Exceute LLM
response=chat(
        model="llama3.2:1b",
        messages=[{
            "role":"users",
            "contect":prompt
        }
        ],
        format="json"
    )

answer = response.message.content

print("LLM response")
print(answer)

#Convert JSON string to python dictionary 
data = json.loads(answer)

print("Data from dictionary ")
print("Language:",data.get("Language"))
print("Language:",data.get("type"))
print("Language:",data.get("Creator"))

