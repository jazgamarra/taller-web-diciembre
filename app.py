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
    # Lista de todos los personajes 
    personajes = lista_de_personajes['results'] 

    return render_template("pagina-principal.html", personajes=personajes)

# Creamos una ruta de ejemplo
@app.route("/ejemplo") 
# Definimos la funcion que se va a ejecutar al acceder a /ejemplo
def ejemplo(): 
    return render_template("ejemplo.html")

# Para ejecutar con el boton de 'play's
if __name__ == "__main__":
    app.run(debug = True)  
