from flask import Flask, jsonify
# from celery import Celery
from flask import request
from upload_files_celery import upload_file 
import os

app = Flask(__name__)	#creating the flask app

UPLOAD_FOLDER = '/home/mandy/Desktop/'	#path to temporary save the file(s) from which celery picks up the file to upload in the server
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

'''
We are temporarily saving the file in the local system because to upload the file to the server we have to know the path of the file.
But when we get any file from flask we get the file only, there is no method to get the filepath.
'''
@app.route("/", methods = ['Get', 'Post'])
def upload():

	if request.method =='POST':	
		file_ = request.files.getlist('upload')	#upload is the key in the form

		if file_:	#if any file exists

			for file in file_:
				file_name = file.filename
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], file_name))	#save the file to the path given above
				upload_file.delay(filename = file_name)	#calling celery fuction

	return "saved successfully"

if __name__ == "__main__":
	app.run(debug = True)

