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
    porcentaje = request.form['porcentaje']
    valor_a = request.form['valor_a']
    valor_b = request.form['valor_b']
    valor_c = request.form['valor_c']
    valor_r = request.form['valor_r']
    operador = request.form['operador']

    if operador=='equalizacion':
        os.system('python hist_Equalization.py static/images/'+filename)
    elif operador=='logaritmo':
        os.system('python logaritmo.py static/images/'+filename +' '+ valor_c)
    elif operador=='exponencial':    
        os.system('python exponencial.py static/images/'+filename+' '+valor_c+' '+valor_b)
    elif operador=='raizC':    
        os.system('python raizC.py static/images/'+filename+' '+valor_c+' '+valor_r)
    elif operador=='contrast':    
        os.system('python contrast.py static/images/'+filename+' '+porcentaje)
    else:    
        os.system('python thresholding.py static/images/'+filename+' '+valor_a+' '+valor_b)

    return jsonify(name = filename)


if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)