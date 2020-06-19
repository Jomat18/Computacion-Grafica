import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
dir = os.path.dirname(os.path.realpath(__file__))

stack = []

@app.route("/remove", methods=["POST"])
def remove():
    global stack
    stack.pop()
    return jsonify(state = 'Success')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/mostrar", methods=["POST"])
def mostrar(): 
    global stack
                   
    try:
        if 'file' in request.files:
            imageFile = request.files['file']
            filename = secure_filename(imageFile.filename)
            imageFile.save(os.path.join(dir + '/static/images/', filename))
    except Exception as e:
        print(e)

    stack.append(filename)    

    return jsonify(name = filename)

@app.route("/calcular", methods=["POST"])        
def calcular():
    global stack
    valor_1 = request.form['valor_1']
    valor_2 = request.form['valor_2']
    valor_r = request.form['valor_r']
    operador = request.form['operador']

    size = len(stack)

    if operador=='equalizacion':
        os.system('python algoritmos/hist_Equalization.py static/images/'+stack[size-1])
    elif operador=='logaritmo':
        os.system('python algoritmos/logaritmo.py static/images/'+stack[size-1] +' '+ valor_1)
    elif operador=='exponencial':    
        os.system('python algoritmos/exponencial.py static/images/'+stack[size-1]+' '+valor_1+' '+valor_2)
    elif operador=='raizC':    
        os.system('python algoritmos/raizC.py static/images/'+stack[size-1]+' '+valor_1+' '+valor_r)
    elif operador=='contrast':    
        os.system('python algoritmos/contrast.py static/images/'+stack[size-1]+' '+valor_1)
    #practica 6
    elif operador=='adicion':    
        os.system('python algoritmos/adicion.py static/images/'+stack[size-1]+' static/images/'+stack[size-2])   
    elif operador=='adicion_gris':    
        os.system('python algoritmos/adicion_gris.py static/images/'+stack[size-1]+' static/images/'+stack[size-2])
    elif operador=='sustraccion_letra':    
        os.system('python algoritmos/sustraccion_letras.py static/images/'+stack[size-1]+' static/images/'+stack[size-2])  
    elif operador=='sustraccion_movimiento':    
        os.system('python algoritmos/sustraccion_movimiento.py static/images/'+stack[size-1]+' static/images/'+stack[size-2]+' '+valor_1)   
    #practica 7   
    elif operador=='multiplicacionC':
        os.system('python algoritmos/multiplicacionC.py static/images/'+stack[size-1]+' '+valor_1)
    elif operador=='division_letra':    
        os.system('python algoritmos/division_letras.py static/images/'+stack[size-1]+' static/images/'+stack[size-2]) 
    elif operador=='division':    
        os.system('python algoritmos/division.py static/images/'+stack[size-1]+' static/images/'+stack[size-2]) 
    elif operador=='blending':    
        os.system('python algoritmos/blending.py static/images/'+stack[size-1]+' static/images/'+stack[size-2]+' '+valor_1)     
    #practica 8   
    elif operador=='operador_and':    
        os.system('python algoritmos/operador_and.py static/images/'+stack[size-1]+' static/images/'+stack[size-2])
    elif operador=='operador_or':    
        os.system('python algoritmos/operador_or.py static/images/'+stack[size-1]+' static/images/'+stack[size-2])
    elif operador=='operador_xor':    
        os.system('python algoritmos/operador_xor.py static/images/'+stack[size-1]+' static/images/'+stack[size-2])                  
    else:    
        os.system('python algoritmos/thresholding.py static/images/'+stack[size-1]+' '+valor_1+' '+valor_2)

    
    filename, file_extension = os.path.splitext(stack[size-1])
    filename = filename + '_r'+file_extension

    stack.append(filename)    

    return jsonify(name = filename)


if __name__ == '__main__':
    app.run(debug = True, port=5000)