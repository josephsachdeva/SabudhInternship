from flask import Flask
#from gradient_descent import gradient_descent
from predict import pred
#from delete import appdel
#from insert import appins



app = Flask(__name__)
#app.register_blueprint(gradient_descent)
app.register_blueprint(pred)
#app.register_blueprint(appu)
#app.register_blueprint(appdel)

app.run()