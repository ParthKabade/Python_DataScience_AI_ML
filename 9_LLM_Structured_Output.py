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
        }]
    )

answer = response.message.content

print("LLM response")
print(answer)

