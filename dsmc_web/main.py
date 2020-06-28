# coding: utf-8
from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from flask_dropzone import Dropzone

app = Flask(__name__)
dropzone = Dropzone(app)
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
        global secured_name
        secured_name = secure_filename(name)
        file_final_name = UPLOAD_DIRECTORY + name
        final_name = file_final_name
        f.save(final_name)
        return '<a href="/get_file">Telecharger le fichier</a>'
    else:
        return render_template('index.html')

@app.route('/get_file')
def get_fil():
    global secured_name
    to_send = UPLOAD_SHORT_DIR + secured_name
    fname = "encoded_" + secured_name
    return send_file(to_send, as_attachment=True, attachment_filename=fname)