from flask import Flask, render_template, request

import joblib

import numpy as np

app = Flask(__name__)

reg_model = joblib.load("/home/23Bondora23/mysite/Regression_model(1).pkl")

clf_model = joblib.load("/home/23Bondora23/mysite/Classification_model.pkl")



@app.route('/')

def home():

    return render_template('index.html')

@app.route('/result', methods=['POST'])

def result():

    # if request.method == 'POST':

    features = [float(x) for x in request.form.values()]

        # features = np.array(features).reshape(1, -1)
    features = [np.array(features)]

        # print(features)

    clf_pred = clf_model.predict(features)

        # print('The Classification Prediction is: ',clf_pred)

    reg_pred = reg_model.predict(features)

        # print('The Regression Prediction is: ',reg_pred)


    return render_template('result.html',clf_pred=clf_pred[0], reg_pred_emi=round(reg_pred[0][0],2),reg_pred_ela=round(reg_pred[0][1],2),reg_pred_roi=round(reg_pred[0][2],2))

if __name__ == '__main__':

    app.run(debug=True)

