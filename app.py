# app.py
from flask import Flask, render_template, request
import os
import time
from zip_cracker import crack_zip

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        zip_file = request.files['zipfile']
        wordlist_file = request.files['wordlist']

        zip_path = os.path.join(UPLOAD_FOLDER, 'secret.zip')
        wordlist_path = os.path.join(UPLOAD_FOLDER, 'wordlist.txt')

        zip_file.save(zip_path)
        wordlist_file.save(wordlist_path)

        start_time = time.time()
        success, password, attempts = crack_zip(zip_path, wordlist_path)
        duration = time.time() - start_time

        if success:
            message = f"✅ Password found: <b>{password}</b> in {attempts} attempts (⏱ {duration:.2f}s)"
        else:
            message = f"❌ Password not found in {attempts} attempts (⏱ {duration:.2f}s)"

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
