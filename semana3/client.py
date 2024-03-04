import requests
url = "http://localhost:8000/"


ruta_get = url + "estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
#Delete
ruta_eliminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", 
                                    url=ruta_eliminar)
print(eliminar_response.text)
#Adicion
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica"
}
post_response = requests.request(method="POST", 
                        url=ruta_post,
                        json=nuevo_estudiante)
print(post_response.text)

nuevo_estudiante = {
    "nombre": "Pedrito",
    "apellido": "Lopez",
    "carrera": "Ingeniería",
}

post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)
#Busqueda
ruta_filtrar_nombre = url + "estudiantes/1"
filtrar_nombre_response = requests.request(method="GET", 
                                url=ruta_filtrar_nombre)
print(filtrar_nombre_response.text)
# Actualizar
ruta_actualizar = url + "estudiantes/1"
estudiante_actualizado = {
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar, 
    json=estudiante_actualizado
)
ruta_carrera = url
print(put_response.text)    
# Todas las carreras
ruta_carreras = url + "carreras"
carreras_response = requests.request(method="GET", 
                                     url=ruta_carreras)
print(carreras_response.text)
# Estudiantes de Economia
ruta_estudiantes_economia = url + "estudiantes/carrera/Economía"
estudiantes_economia_response = requests.request(method="GET", 
                                                url=ruta_estudiantes_economia)
#ADICION A ESTUDIANTES DE ECONOMIA 
print(estudiantes_economia_response.text)
ruta_post = url + "estudiantes"

# estudiante de Economía 1
nuevo_estudiante_economia_1 = {
    "nombre": "Lucia",
    "apellido": "Quispe",
    "carrera": "Economía"
}
post_response = requests.post(url, json=nuevo_estudiante_economia_1)
print(post_response.text)

# Estudiante de Economía 2
nuevo_estudiante_economia_2 = {
    "nombre": "Carlos",
    "apellido": "Gutierrez",
    "carrera": "Economía"
}
post_response = requests.post(url, json=nuevo_estudiante_economia_2)
print(post_response)
