from http.server import HTTPServer, BaseHTTPRequestHandler
import json
estudiantes = [
    {
        "id": 1,
        "nombre": "Pedrito",
        "apellido": "García",
        "carrera": "Ingeniería de Sistemas",
    },
]


class RESTRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    def find_student(self, id):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
        )
    def get_carrers(self):
        carreras = list(set(estudiante["carrera"] for estudiante in estudiantes))
        return carreras
    def find_students_career(self, carrera):
        return [estudiante for estudiante in estudiantes if estudiante["carrera"] == carrera]
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8"))
        return data
    
    def do_GET(self):
        if self.path == "/estudiantes":
            self.response_handler(200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            if estudiante:
                self.response_handler(200, [estudiante])
            else:
                self.response_handler(204, [])
        elif self.path == "carreras":
            carreras = self.get_carrers()
            self.response_handler(200,carreras)
        elif self.path == "/estudiantes/economia":
            estudiantes_economia = self.find_students_career("Economía")
            self.response_handler(200, estudiantes_economia)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_POST(self):
        if self.path == "/estudiantes":
            data = self.read_data()
            data["id"] = len(estudiantes) + 1
            estudiantes.append(data)
            self.response_handler(201, estudiantes)

        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_PUT(self):
        if self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            data = self.read_data()
            if estudiante:
                estudiante.update(data)
                self.response_handler(200, [estudiantes])
            else:
                self.response_handler(404, {"Error": "Estudiante no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

    def do_DELETE(self):
        if self.path == "/estudiantes":
            estudiantes.clear()
            self.response_handler(200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = self.find_student(id)
            if estudiante:
                estudiantes.remove(estudiante)
                self.response_handler(200, estudiantes)
            else:
                self.response_handler(404, {"Error": "Estudiante no encontrado"})
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})


def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()