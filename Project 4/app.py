from flask import Flask, render_template, request
import pandas as pd
from sklearn import *
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():

        loan_data_df = pd.read_csv("Main_Doc.csv")

        X = loan_data_df.drop(['Loan_Status'], axis=1)
        y = loan_data_df['Loan_Status']

        X_scaler = StandardScaler().fit(X)
        X_scaled = X_scaler.transform(X)

        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.5, random_state=42)

        classifier = LogisticRegression()

        classifier.fit(X_train, y_train)

        y_predict = classifier.predict(X_test)

        train_pred = classifier.predict(X_train)

        if request.method == "POST":

                data = []

                data.append(int(request.form['Married']))
                data.append(int(request.form['Dependents']))
                data.append(int(request.form['Self_Employed']))
                data.append(float(request.form['ApplicantIncome']))
                data.append(float(request.form['CoapplicantIncome']))
                data.append(float(request.form['LoanAmount']))
                data.append(float(request.form['Loan_Amount_Term']))

                prediction = classifier.predict_proba(X_scaler.transform([data]))
                output = round(prediction[0][1],2) * 100


        return render_template("results.html", output=output)


if __name__ == '__main__':
    app.run(debug=True)
