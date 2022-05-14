from tkinter.tix import Tree
from flask import Flask, Request, make_response, redirect, render_template, request     #importamos lo que necesitamos

app= Flask(__name__)     #hace referencia abjeto tipo flask

items = ["Casa", "Carro"]

@app.route ("/index") #establecemos la ruta de la llamada al endpoint
def index(): # crea la funcion
    user_ip_information = request.remote_addr
    response = make_response(redirect("/information"))
    response.set_cookie("user_ip_information", user_ip_information)
    
    return response
    #return f"Return de index "


@app.route ("/information") #establecemos la ruta de la llamada al endpoint
def information(): # crea la funcion
    user_ip = request.cookies.get("user_ip_information")
    context = {
        "user_ip": user_ip,
        "items":items
    }
    
    return render_template("information.html", **context)
    #return f"Return de informacion "


def pagina_no_encontrada(error):
    return "<h1> La pagina a la que intentas acceder no existe. </h1>"

if __name__=='__main__':
    app.register_error_handler(404, pagina_no_encontrada)
    app.run(debug=True) 



