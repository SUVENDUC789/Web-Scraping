import requests

responseWeb=requests.get('http://checker.soax.com/api/ipinfo')

dataUser=responseWeb.json()
print('status'.capitalize()," = ",dataUser['status'])
print('reason'.capitalize()," = ",dataUser['reason'])
dataUser=dataUser['data']
for key ,value in dataUser.items():
    key=key.capitalize()
    key=key.replace('_',' ')
    print(key," = ",value)
