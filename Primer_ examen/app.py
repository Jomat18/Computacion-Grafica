import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
dir = os.path.dirname(os.path.realpath(__file__))
filename = ''

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/mostrar", methods=["POST"])
def mostrar(): 
    global filename           
    try:
        if 'file' in request.files:
            imageFile = request.files['file']
            filename = secure_filename(imageFile.filename)
            imageFile.save(os.path.join(dir + '/static/images/', filename))
    except Exception as e:
        print(e)

    return jsonify(name = filename)

@app.route("/calcular", methods=["POST"])        
def calcular():
    global filename
    valor_a = request.form['valor_a']
    valor_b = request.form['valor_b']
    valor_c = request.form['valor_c']
    valor_d = request.form['valor_d']
    valor_r = request.form['valor_r']
    operador = request.form['operador']

    # Aqui llamar a las funciones

    return jsonify(name = filename)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)