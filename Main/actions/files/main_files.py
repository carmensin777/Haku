
'''
This is the file where the main promt is executed, this promt identified the funcion to 
execute, chose the promt and the respective funcion to the promt.
'''
import os
from groq import Groq
from Main.json_helpers import extract_json
from Main.actions.filesAction import filesH

def main_files(role,cont):
    client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system" ,
            "content": role,
        },
        {
            "role": "user" ,
            "content": cont,
        }
    ],
    model="llama3-8b-8192",
    )
    response=chat_completion.choices[0].message.content
    json_function = extract_json(response)
    print(response)
    if json_function:
        choosed_function=json_function[0]['choosed_function']
        route = json_function[0]['ruta']
        name = json_function[0]['nombre']
        ext = json_function[0]['ext']
        con = json_function[0]['content']
        obj=filesH(route,name,ext)
        if choosed_function=="create_file":
            obj.create_file()
    else:
        print("Something went wrong")
     

