from flask import Blueprint
import pandas as pd
import numpy as np
from data_to_csv import
#import json
#app = Flask(__name__)
gradient_descent = Blueprint('gradient_descent', __name__)
@gradient_descent.route("/",methods=['POST']) # 'http::/www.google.com/'
def gradient_descent():
    df = pd.read_csv("train.csv")
    X = df['X']
    Y = df['Y']
    lam = 0.001
    #em = m
    #ec = c
    #while(em > 0.1 and ec > 5):
    for i in range(20000):
#     em = m
#     ec = c
#     while(True):
        calm = (m*X + c - Y)*X
        dcdm = np.sum(calm)/n
        m = m - lam*dcdm
#         em = em - m
        
        calc = (m*X + c - Y)
        dcdc = np.sum(calc)/n
        c = c - lam*dcdc
#         ec = ec - c
#         if(em < 0.3 and ec < 0.7):
#             break
    return c, m

