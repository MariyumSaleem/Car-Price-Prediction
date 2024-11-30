from flask import Flask, render_template, request
import pandas as pd
import pickle
app = Flask(__name__)
model = pickle.load(open("LinearRegressionModel.pkl",'rb'))
df = pd.read_csv("Cleaned Car.csv")
@app.route('/')
def index():
    companies = sorted(df['company'].unique())
    car_models = sorted(df['name'].unique())
    years = sorted(df['year'].unique())
    fuel_types = sorted(df['fuel_type'].unique())
    return render_template('index.html', companies = companies, car_models = car_models, years= years,
                            fuel_types = fuel_types)
@app.route('/predict', methods=['POST'])
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    kms_driven = int(request.form.get('kms_driven'))
    print(company,car_model,year,fuel_type,kms_driven)


    prediction = model.predict(pd.DataFrame([[car_model, company,year,kms_driven,fuel_type]],columns = ['name','company','year','kms_driven','fuel_type']))
    return str(prediction[0])

if __name__ == "__main__":
    app.run(debug=True)