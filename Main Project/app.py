from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'Media'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            subprocess.run(['python', 'helmet_detection_image.py', file_path])
        elif filename.endswith('.mp4'):
            subprocess.run(['python', 'helmet_detection_video.py', file_path])
        return redirect(url_for('index'))
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)