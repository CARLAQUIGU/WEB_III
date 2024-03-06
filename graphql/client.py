import requests
#definir la consulta de G...
#tres cadenas es para cadena multilinea
query="""{ 
    hello
    goodbye
    }
"""
#definir donde se consultara URL
url = 'http://localhost:8000/graphql'
#post 
response = requests.post(url, json={'query': query})
print(response.text)
