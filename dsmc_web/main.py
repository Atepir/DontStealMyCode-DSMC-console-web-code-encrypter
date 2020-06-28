# coding: utf-8
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = b"macrohacks"
UPLOAD_DIRECTORY = "dsmc_web/uploads/"
UPLOAD_SHORT_DIR = "uploads/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploads_file():
    if request.method == 'POST':
        f = request.files['file']
        name = f.filename
        secured_name = secure_filename(name)
        final_name = UPLOAD_DIRECTORY + secured_name
        download_path = UPLOAD_SHORT_DIR + secured_name
        output_name = "encrypted_" + secured_name
        folder_index = 0
        for i in range(10000):
            folder_index += 1
            if not os.path.exists(UPLOAD_DIRECTORY + "temp" + str(i)):
                os.mkdir(UPLOAD_DIRECTORY + "temp" + str(i))
                break
        f.save(UPLOAD_DIRECTORY + "temp" + str(folder_index - 1) + f.filename)
        page = '<a href="/get_file?path='+download_path+'&name='+output_name+'">Telecharger le fichier</a>'
        return page
    else:
        return render_template('index.html')

@app.route('/get_file', methods=['GET'])
def get_fil():
    if request.method == 'GET':
        path = request.form.get('path')
        name = request.form.get('name')
        return send_file(path, as_attachment=True, attachment_filename=name)