import subprocess , uuid

str_val = 'GeeksforGeeks'
result = subprocess.run('sgpt "dame solo y solo un número de 6 digitos al azar"', stdout=subprocess.PIPE)
print(result.stdout.decode('windows-1252'))#resul.st... contiene el string completo de la respuesta de ChatGPT, recorda procesar el texto para obtener la contraseña generada
print("The string hash value is : " + str(uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')))#str(uuid.uuid3... es la funcion de hash