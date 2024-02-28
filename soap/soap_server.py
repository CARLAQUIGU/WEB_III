from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "¡Hola, {}!".format(nombre)

dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)
def suma_dos_numeros(numero1,numero2):
    return numero1+numero2

dispatcher.register_function(
    "SumaDosNumeros",
    suma_dos_numeros,
    returns={"suma": int},
    args={"numero1": int, "numero2":int},
)

def cadena_palindromo(cadena):
    return cadena == cadena[::-1]

dispatcher.register_function(
    "CadenaPalindromo",
     cadena_palindromo,
    returns={"es_palindormo":bool},
    args={"cadena": str},
)

server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()