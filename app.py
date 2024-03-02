from flask import Flask, request, render_template
import openai
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            file.save(os.path.join("uploads", file.filename))
            r = sr.Recognizer()
            with sr.AudioFile(os.path.join("uploads", file.filename)) as source:
                audio_data = r.record(source)
                text = r.recognize_google(audio_data)
                return render_template('index.html', text=text)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)