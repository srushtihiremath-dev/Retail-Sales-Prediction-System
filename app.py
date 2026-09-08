from flask import Flask, render_template, request
from retail_prediction import predict_sales

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        store = int(request.form['store'])
        feature = float(request.form['feature'])

        result = predict_sales(store, feature)

        return render_template('index.html', prediction=result)

    except Exception as e:
        return render_template('index.html', prediction="Error")

if __name__ == "__main__":
    app.run(debug=True)