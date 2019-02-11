#from flask import Blueprint
import pandas as pd
import numpy as np
#import json
#app = Flask(__name__)
#cm = Blueprint('cm', __name__)
#@cm.route("/",methods=['GET']) # 'http::/www.google.com/'
def calculatecm():
    n=50
    df = pd.read_csv("train.csv")
    X = df['X']
    Y = df['Y']
    xm = np.mean(X)
    ym = np.mean(Y)
    ssxy = np.sum(X*Y) - n*xm*ym
    ssxx = np.sum(X**2) - n*(xm**2)
    
    m = ssxy/ssxx
    c = ym - m*xm
    
    return c, m