
'''
This is the file where the main promt is executed, this promt identified the funcion to 
execute, chose the promt and the respective funcion to the promt.
'''
import os
from groq import Groq
from HakuCore.Main.json_helpers import extract_json
from HakuCore.Main.actions.files.files import filesH
from HakuCore.Conf.conf import groq_api_key

def main(cont,role):
        iter=0
        while True:
            iter=iter+1
            print(iter)
            client = Groq(
            api_key=groq_api_key,
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
            try:
                choosed_function=json_function[0]['choosed_function']
                route = json_function[0]['ruta']
                name = json_function[0]['nombre']
                ext = json_function[0]['ext']
                con = json_function[0]['content']
                message = json_function[0]['message']
                obj=filesH(name,route,ext)
                if choosed_function=="create_file":
                    if  obj.create_file() and obj.write_file(con):
                        print("Route: ",route)
                        return message
            except Exception as e:
                pass
     




