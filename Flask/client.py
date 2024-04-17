import requests

url="http://localhost:5000/"

res=requests.get(url)
print(res.text)

#meotodo
#params = {'nombre': 'Carla'}
#response = requests.get(url+'saludar', params=params)
#print(response.text)
#suma
response=requests.get(url+'sumar?a=5&b=3')
print(response.text)
response=requests.get(url+'palindromo?cadena="reconocer"')
print(response.text)
response=requests.get(url+'contar?cadena=exepciones&vocal=e')
print(response.text)