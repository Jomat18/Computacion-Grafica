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
    valor_t1 = request.form['valor_t1']
    valor_t2 = request.form['valor_t2']
    valor_minimo = request.form['valor_minimo']
    valor_maximo = request.form['valor_maximo']
    #valor_a = request.form['valor_a']
    valor_b = request.form['valor_b']
    valor_c = request.form['valor_c']
    valor_c_exp = request.form['valor_c_exp']
    valor_c_rai = request.form['valor_c_rai']
    #valor_d = request.form['valor_d']
    valor_r = request.form['valor_r']
    valor_intensidad = request.form['valor_intensidad']
    operador = request.form['operador']

    #os.system('python algoritmos/thresholding.py static/images/'+filename + ' '+valor_a+ ' '+valor_b)

    # Aqui llamar a las funciones
    if operador == "thresholding":
       os.system('python algoritmos/thresholding.py static/images/'+filename + ' '+valor_t1+ ' '+valor_t2)
    elif operador == "contrast":
       os.system('python algoritmos/contrast.py static/images/'+filename + ' '+valor_minimo+' '+valor_maximo)
    elif operador == "ecualizacion":
       os.system('python algoritmos/ecualizacion.py static/images/'+filename + ' '+valor_intensidad)
    elif operador == "logaritmico":
       os.system('python algoritmos/logaritmico.py static/images/'+filename + ' '+valor_c)
    elif operador == "raiz":
       os.system('python algoritmos/raiz.py static/images/'+filename + ' '+valor_c)
    elif operador == "exponencial":
       os.system('python algoritmos/exponencial.py static/images/'+filename + ' '+valor_c_exp+ ' '+valor_b)
    else:
       os.system('python algoritmos/raisetopower.py static/images/'+filename + ' '+valor_c_rai+ ' '+valor_r)

    #os.system('python ejercicio1.py static/images/'+filename + ' '+valor_c)
    return jsonify(name = filename)


if __name__ == '__main__':
    app.run(port=5000,debug=True)