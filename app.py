# Importar las librerias 
from flask import Flask, render_template 
import requests # nos permite hacer el pedido a la API

# Crear una aplicacion 
app = Flask(__name__) 

# Crear una pagina principal 
@app.route ("/") 
def pagina_principal (): 
    # Pedido a la api 
    lista_de_personajes = requests.get('https://rickandmortyapi.com/api/character').json()
    personajes = lista_de_personajes['results']

    # Acceder a la informacion de un solo personaje 
    personaje_uno = personajes[0]

    return render_template("pagina-principal.html", personaje_uno=personaje_uno)

# Creamos una ruta de ejemplo
@app.route("/ejemplo") 
# Definimos la funcion que se va a ejecutar al acceder a /ejemplo
def ejemplo(): 
    return render_template("ejemplo.html")

# Para ejecutar con el boton de 'play's
if __name__ == "__main__":
    app.run(debug = True)  
