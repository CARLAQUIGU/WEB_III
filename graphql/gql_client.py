import requests
url = 'http://localhost:8000/graphql'
query_crear = """
mutation {
        crearEstudiante(nombre: "Angel", apellido: "Gomez", carrera: "Biologia") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""
query_creara = """
mutation {
        crearEstudianteArquitectura(nombre: "Carla", apellido: "Quispe") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

# Definir l
# Definir la consulta GraphQL simple
query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
    }
"""
response_mutation = requests.post(url, json={'query': query_creara})
print(response_mutation.text)

# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)


#query = """{
#    estudianteNombreApellido(nombre: Jose, apellido: Lopez){
#        nombre
#    }
#}"""
#query = """{
#    estudiantes{
#        nombre
#        apellido
#    }
#}"""
# Solicitud POST al servidor GraphQL
#response = requests.post(url, json={'query': query})
#print(response.text)