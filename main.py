import os
from flask import Flask, render_template, request, send_from_directory, url_for
from pdf2image import convert_from_path


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/upload')
def upload_form():
    return render_template('file_uploader.html')

@app.route('/download/<filename>')
def download_form(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filen = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
        f.save(filen)
        convertPdf(filen)
        return render_template('file_successful.html')

    return render_template('file_uploader.html')

def convertPdf(pdf_file):
    pages = convert_from_path(pdf_file, 300)

    for page in pages:
        page.save("temp/pdf-page%d.jpg" % (pages.index(page)), "JPEG")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
