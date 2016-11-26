import os
from flask import Flask,render_template,flash,request,redirect,url_for,send_from_directory
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'JPG', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
           
@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        #first, if there is no file display upload page
        if 'file' not in request.files:
            return redirect(request.url) 
        photo = request.files['file']
        #if empty filename also display upload page
        if photo.filename == '': 
            return redirect(request.url)
        #process proper files. might also want to implement size limit
        if photo and allowed_file(photo.filename):
            filename = secure_filename(photo.filename)
            #saving: presumably normally you'd want to save uploaded photos
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename)) 
            return redirect(url_for('uploaded_file', filename=filename))
    #html (obv. could be in a static file)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/<filename>')
def uploaded_file(filename):
    data = send_from_directory(app.config['UPLOAD_FOLDER'],filename)
    #dump the file
    if filename != 'window.jpg': #keep my testing file!
        os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    #just streaming the photo directly, no html template
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    #app.run()

