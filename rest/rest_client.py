import requests


url = "http://localhost:8000/"
ruta_get = url + "lista_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)


ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)

ruta_post = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Carla",
    "apellido": "Quispe",
    "carrera": "Informatica",
}

post_response = requests.request(method="POST", 
                                    url=ruta_post, 
                                    json=nuevo_estudiante)
print(post_response.text)


ruta_get = url + "buscar_nombre"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_get = url + "contar_carreras"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

ruta_get = url + "total_estudiantes"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

#DELETE 
ruta_eleminar = url + "estudiantes"
eliminar_response = requests.request(method="DELETE", url=ruta_eleminar)
print(eliminar_response.text)

#actualizacion 
ruta_actualizar = url + "estudiantes"
estudiante_actualizado={
    "id": 1,
    "nombre" : "Juan",
    "apellido" : "Perez",
    "carrera" : "Ingenieria Agronomica",
}
put_response = requests.request(
    method="PUT", url=ruta_actualizar,
    json=estudiante_actualizado
)
print(put_response.text)