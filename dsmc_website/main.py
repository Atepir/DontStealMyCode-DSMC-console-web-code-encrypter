# coding: utf-8

from flask import Flask, render_template, request, send_file, redirect, url_for
from werkzeug.utils import secure_filename
from dsmc_web import Code

app = Flask(__name__)
app.secret_key = b"macrohacks"
UPLOAD_DIRECTORY = "dsmc_website/uploads/"
UPLOAD_SHORT_DIR = "uploads/"


@app.route('/')
def upload_file():
    return render_template('index.html')


todo = 1
f1 = 1
f2 = 1
secured_name = "default"


@app.route('/uploader', methods=['GET', 'POST'])
def uploads_file():
    if request.method == 'POST':
        f = request.files['file']
        encryption = request.form.get('encrypt')
        decryption = request.form.get('decrypt')
        global todo
        todo = 1 if encryption == "Encrypt" else 0
        global f1
        f1 = request.form.get('f1')
        global f2
        f2 = request.form.get('f2')
        name = f.filename
        global secured_name
        secured_name = secure_filename(name)
        final_name = UPLOAD_DIRECTORY + secured_name
        f.save(final_name)
        return render_template('download.html')
    else:
        return render_template('index.html')


@app.route('/get_file')
def get_fil():
    global secured_name
    received = UPLOAD_DIRECTORY + secured_name
    global f1, f2
    codeObject = Code(received, f1, f2)
    encrypted_name = "encrypted_" + secured_name
    decrypted_name = "decrypted_" + secured_name
    global todo
    if todo == 1:
        codeObject.encrypt(output=UPLOAD_DIRECTORY + encrypted_name)
        return send_file(UPLOAD_SHORT_DIR + encrypted_name, as_attachment=True, attachment_filename=encrypted_name)
    else:
        codeObject.decrypt(output=UPLOAD_DIRECTORY + decrypted_name)
        return send_file(UPLOAD_SHORT_DIR + decrypted_name, as_attachment=True, attachment_filename=decrypted_name)
