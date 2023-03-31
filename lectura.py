import json
with open('data.json') as file:
    data = json.load(file)
    for client in data['clients']:
        print('nombre:', client['first_name'])
        print('apellido:', client['last_name'])
        print('edad:', client['age'])
        print('altura (m):', client['amount'])
        print('')
#Para convertirlo a una cadena
# print("la cadena es: ")
# client = json.dumps(data)
# print(client)