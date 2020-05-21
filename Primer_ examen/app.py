import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename

app = Flask(__name__)
dir = os.path.dirname(os.path.realpath(__file__))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/calcular", methods=["POST"])
def calcular():
    if request.method == 'POST':        
        try:
            if 'file' in request.files:
                imageFile = request.files['file']
                filename = secure_filename(imageFile.filename)
                imageFile.save(os.path.join(dir + '/static/images/', filename))
        except Exception as e:
            print(e)

        return jsonify(name = filename)

if __name__ == '__main__':
    app.debug = True
    app.run(port=5000)