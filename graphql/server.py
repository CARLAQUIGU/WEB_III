from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from graphene import ObjectType, String, Int, List, Schema

#Query = consulta
#uery que tiene un atributo que es cadena
class Query(ObjectType):
    hello = String()
    
    goodbye = String()
    #el nombre tiene que tener resolve _ y el nombre del atributo
    def resolve_goodbye(root,info):
        return "Bye Bye"
    
    def resolve_hello(root,info): #info estatus de la solicitud
        return "Hello, World!" #el return tiene que ser del tipo del atributo si o si
#contruyendo el schema 
schema = Schema(query=Query)

#contuyendo el servidor
class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"]) #leyendo en contenleght hay un json
            data = self.rfile.read(content_length)#leyendo
            data = json.loads(data.decode("utf-8"))#
            result = schema.execute(data["query"])#en el json tiene que haber un query #data es diccionario
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})

#levantando el sevidor
def run_server(port=8000):
    try:
        server_address = ("", port)#dupla
        httpd = HTTPServer(server_address, GraphQLRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()

if __name__ == "__main__":
    run_server()