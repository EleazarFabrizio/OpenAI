import openai

import time

import random

# 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
##  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

openai.api_key = "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"

completion = openai.Completion.create(engine = "text-davinci-003",


prompt = "give me a password written in spanish. It must be 20 or more characters in lenght. It must follow mnemotecnic rules. It must be as easy as possible in order to be understood by anyone",


                                      max_tokens = 2048)

pure = (completion.choices[0].text)

print(pure)
hash(pure)

num = random.randint(1000,9999)
print (num)

password = str(pure) + str(num)



comenzar = time.time()






clave = input("\nIngresar:  ")
finalizar = time.time()

print(f"""
{str(pure) + str(clave)}
{str(password)}
""")


if ((str(pure) + str(clave)) == password):
    print ("contraseña correcta")

else:
    print ("contraseña incorrecta")

