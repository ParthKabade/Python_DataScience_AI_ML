from ollama import chat

#Select the local LLm
model="llama3.2:1b"

#define prompts
prompt= [
    "Explain recursion",
    "Explain recursion in python in 3 simple points",
    """Your experinced python techer explain  recursion for beginner
    give one simple example.
    """,
    """Convert programming languages to uppercase.
    Example 1:
    Input :python
    output:PYTHON
    
    Example 2:
    Input :java
    output:JAVA
    
    Input :javascript
    output:PYTHON"""  
]

#excecute every prompt
for index,prompt in enumerate(prompt,start=1):
    print("*"*50)
    print("prompt number :",index)
    print("input prompt:",prompt)

    response=chat(
        model=model,
        messages=[{
            "role":"users",
            "contect":prompt
        }]
    )

    print("\nresponce from llm is")
    print(response.message.content)

