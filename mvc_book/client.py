import requests

# URL base de la API
BASE_URL = "http://localhost:5000/api"

# Definir los encabezados de la solicitud
headers = {"Content-Type": "application/json"}

# Crear un nuevo libro
url = f"{BASE_URL}/libros"
nuevo_libro = {"titulo": "Katya", "autor": "Adolfo Hernandez", "edicion": 2,"disponibilidad":True}
response = requests.post(url, json=nuevo_libro, headers=headers)
print("Creando un nuevo libro:")
print(response.json())

# Crear el segundo libro
nuevo_libro2 = {"titulo": "Calmar la sed", "autor": "Charo Ruano", "edicion": 1,"disponibilidad":True}
response = requests.post(url, json=nuevo_libro2, headers=headers)
print("\nCreando un nuevo libro:")
print(response.json())

# Obtener la lista de todos los libros
url = f"{BASE_URL}/libros"
response = requests.get(url, headers=headers)
print("\nLista de Libros:")
print(response.json())

# Obtener un libro específico por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.get(url, headers=headers)
print("\nDetalles del libro con ID 1:")
print(response.json())

# Actualizar un libro existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
datos_actualizacion = {"titulo": "Katya", "autor": "Adolfo Hernandez", "edicion": 1,"disponibilidad":False}
response = requests.put(url, json=datos_actualizacion, headers=headers)
print("\nActualizando el libro con ID 1:")
print(response.json())

# Eliminar un libro existente por su ID (por ejemplo, ID=1)
url = f"{BASE_URL}/libros/1"
response = requests.delete(url, headers=headers)
print("\nEliminando el libro con ID 1:")
if response.status_code == 204:
    print(f"libro con ID 1 eliminado con éxito.")
else:
    print(f"Error: {response.status_code} - {response.text}")