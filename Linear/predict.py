from flask import Blueprint
from calculate_c_m import calculatecm
#import numpy as np
#import pandas as pd

pred = Blueprint('pred', __name__)
@pred.route("/<x>",methods=['POST'])
def predict(x):
    c, m = calculatecm()
    y = m*int(x) + c
    return ("Predicted value is: "+str(y))