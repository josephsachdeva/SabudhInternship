from flask import Flask
from celery import Celery
from flask import request

celery = Celery('upload_files_celery', broker = 'redis://localhost:6379', backend = 'redis://localhost:6379')	#initializing the celery

@celery.task
def upload_file(filename):

	path = '/home/mandy/Desktop/'+str(filename) #path to where we saved the temporary files in the flask file

	with open(path, 'rb') as file:
		data = file.read()	#read the file
		''' Here the s3 upload file code will be written and the below code can be commented because we know the path
		and we can directly pick that file to upload in the server(s3) '''
	
		''' This code can be omitted'''
		'''It is used to save the file locally'''
	with open(filename, 'wb') as f:
		f.write(data)	#save the file where we want to

	file.close()
	f.close()
