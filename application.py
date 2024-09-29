from flask  import  Flask, render_template, request, jsonify
import pickle
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

ridge_model=pickle.load(open('models/ridge.pkl', 'rb'))
standard_scaler=pickle.load(open('models/scaler.pkl','rb'))

application=Flask(__name__)
app=application

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/predictdata",methods=['GET', 'POST']):
 
if __name__=="__main__":
    app.run("0.0.0.0")
    