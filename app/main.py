import os
from flask import Flask, render_template, request, send_from_directory, url_for
from pdf2image import convert_from_path
from flask_pymongo import PyMongo

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


app = Flask(__name__,template_folder='../templates')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MONGO_DBNAME'] = 'python_flask_mongo_test'
app.config['MONGO_URI'] = 'mongodb://mohitgarg:testpassword1@ds261155.mlab.com:61155/python_flask_mongo_test'

mongo = PyMongo(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/Airbus')
def Airbus_dashboard():
    return render_template('indexAirbus.html')

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
