# Importar las librerias 
from flask import Flask, render_template 

# Crear una aplicacion 
app = Flask(__name__) 

# Crear una pagina principal 
@app.route ("/") 
def pagina_principal (): 
    nombre = "Pablo"
    apellido = "Sanchez"
    return render_template("pagina-principal.html", nombre=nombre, apellido=apellido)

# Creamos una ruta de ejemplo
@app.route("/ejemplo") 
# Definimos la funcion que se va a ejecutar al acceder a /ejemplo
def ejemplo(): 
    return render_template("ejemplo.html")

# Para ejecutar con el boton de 'play's
if __name__ == "__main__":
    app.run(debug = True)  
