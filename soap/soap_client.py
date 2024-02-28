from zeep import Client

client = Client('http://localhost:8000')
#Suma de dos Numeros
#result = client.service.SumaDosNumeros(numero1=5,numero2=5)
#print(result)
#Cadena Palindroma
result = client.service.CadenaPalindromo(cadena="ana")
print(result)