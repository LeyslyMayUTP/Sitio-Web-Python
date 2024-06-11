from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('sitio/index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('sitio/nosotros.html')

@app.route('/servicios')
def servicios():
    return render_template('sitio/servicios.html')

@app.route('/menu')
def menu():
    return render_template('sitio/menu.html')

@app.route('/reservacion')
def reservacion():
    return render_template('sitio/reservacion.html')

@app.route('/contacto')
def contacto():
    return render_template('sitio/contacto.html')

if __name__ =='__main__':
    app.run(debug=True)