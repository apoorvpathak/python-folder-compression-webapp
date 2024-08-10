from flask import Flask, render_template, request, send_file, redirect, url_for
import os
import zipfile
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']): #MAKING UPLOAD FOLDER IF IT DOES NOT EXITS ALREADY
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload(): #UPLOAD LOGIC
    #CHECKING IF POST REQUEST GOT THE FILE
    if 'folder' not in request.files:
        return redirect(url_for('index'))
    folder = request.files.getlist('folder')
    foldername = request.form.get('foldername')
    folder_path = os.path.join(app.config['UPLOAD_FOLDER'], foldername)

    os.makedirs(folder_path, exist_ok=True)
    

    for file in folder:
        filename = secure_filename(file.filename)
        file.save(os.path.join(folder_path, filename))

    zip_filename = f"{foldername}.zip"
    zip_filepath = os.path.join(app.config['UPLOAD_FOLDER'], zip_filename)

    #CREATE ZIP FIE WITH ZIPFILE LIBRARY
    with zipfile.ZipFile(zip_filepath, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), folder_path))
  
    #MAKING ZIP AVAILABLE TO USER
    return send_file(zip_filepath, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)


