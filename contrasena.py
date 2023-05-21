import openai

import time

import random

import os

# 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
##  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



while 1:
    os.system("cls")
    op = input("""
Bienvenido. Ingrese una openai key para comenzar el programa o utilice una key predeterminada
    
1) Usar openai api key personalizada/propia
2) Utilizar key preterminada. (Esto podria resultar en errores)

:   """)
    
    flag = True

    while (flag == True):
        try:
            op = int(op)
            flag = False
        except ValueError:
            print ("valor ingresado fuera de los parametros")
            flag = True


    if op == 2:
        llave = "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"
    if op == 1:
        llave = input("ingrese una openai api key, por favor:   ")

    try:
        openai.api_key = llave

        completion = openai.Completion.create(engine = "text-davinci-003",


        prompt = "give me a password written in spanish. It must be 20 or more characters in lenght. It must follow mnemotecnic rules. It must be as easy as possible in order to be understood by anyone",


                                            max_tokens = 2048)

        pure = (completion.choices[0].text)

        os.system("cls")

        print(pure)
        hash(pure)

        num = random.randint(1000,9999)
        print (num)

        password = str(pure) + str(num)







        clave = input("\nIngresar:  ")


        '''print(f"""
        {str(pure) + str(clave)}
        {str(password)}
        """)'''


        if ((str(pure) + str(clave)) == password):
            print ("contraseña correcta")

        else:
            print ("contraseña incorrecta")

        space = input("Precione cualquier tecla para continuar: ")

    except openai.error.AuthenticationError:
        print ("Un error inesperado ha ocurrido. Por favor, asegurese que su openai api key es valida. Precione cualquier tecla para continuar: ")
        space = input("")
