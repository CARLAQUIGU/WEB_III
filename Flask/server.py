from flask import Flask , request , jsonify
#app vive el servidor
app= Flask(__name__)

#definirmos nuestra primera ruta 
@app.route('/')
def hello_world():
    return '!Hola, Mundo!'
#Saludo
@app.route("/saludar", methods=["GET"])
def saludar():
    nombre = request.args.get("nombre")
    if not nombre:
        return (
            jsonify({"error": "Se requiere un nombre en los parámetros de la URL."}),
            400,
        )
    return jsonify({"mensaje": f"¡Hola, {nombre}!"})

#Suma de dos numeros
@app.route("/sumar", methods=["GET"])
def sumar():
    a=request.args.get("a")
    b=request.args.get("b")
    if not a and not b:
        return(
            jsonify({"Mesaje": "Falta un parametro"}),400,
        )
    res = int (a)+ int(b)
    return jsonify({"La suma es" : f"{res}"})
#palindromo
@app.route("/palindromo", methods=["GET"])
def palindromo():
    cadena=request.args.get("cadena")
    if not cadena:
        return (
            jsonify({"error": "Se requiere una cadena en los parámetros de la URL."}),
            400,
        )
    lena=len(cadena)
    b=[]
    for i in range(lena - 1, -1, -1):
        b.append(cadena[i])
    rev = "".join(b)
    if cadena == rev:
        return  jsonify({"La cadena ":f"{cadena} es palindromo"})
    else:
        return  jsonify({"La cadena ":f"{cadena} no es palindromo"})

#Contar vocal en cadena
@app.route("/contar", methods=["GET"])
def contar():
    cadena = request.args.get("cadena")
    vocal = request.args.get("vocal")

    if not cadena or not vocal:
        return (
            jsonify({"Mensaje": "Falta un parámetro"}),
            400
        )
    count=0
    cadena = cadena.lower()
    vocal = vocal.lower()
    for letra in cadena:
        if letra == vocal:
            print(letra)
            count=count+1
    return jsonify({"Número de veces que aparece la vocal": count})

#inicia el servidor local en el puerto 5000
if __name__ == "__main__":
    app.run();
