# Retail Sales Prediction System

A Python-based retail sales forecasting project designed to predict weekly sales using a simple machine learning model and a Flask web interface. The project also includes exploratory data analysis (EDA) scripts for visualizing sales trends, correlations, holiday effects, and store performance.

## Overview

This repository combines:

- A simple web application for sales prediction
- Data analysis scripts to understand retail trends
- CSV datasets for training and testing
- Visual outputs such as plots and heatmaps
- Supporting project documentation and presentation materials

The project is built primarily in Python and uses:

- Flask for the web interface
- Pandas for data processing
- Scikit-learn for prediction modeling
- Matplotlib and Seaborn for data visualization

## Project Goal

The goal of the project is to analyze retail sales behavior and estimate expected sales using a lightweight predictive model. The application lets users enter a store ID and feature value and returns an estimated sales amount.

## Tech Stack

- Python 3.x
- Flask
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Phonenumbers (used in a separate phone-location script)

## Repository Structure

```text
Retail-Sales-Prediction-System/
├── app.py                           # Flask application entry point
├── retail_prediction.py             # Model training and prediction logic
├── userinput.py                    # Manual prediction script from user input
├── boxplot.py                      # Sales boxplot generation
├── correlation.py                  # Correlation heatmap generation
├── holiday_sales_graph.py          # Holiday vs non-holiday sales graph
├── locations.py                    # Phone number location lookup example
├── monthly_trend.py                # Monthly sales trend visualization
├── store_sales_graph.py            # Top store sales chart
├── top10_store_sales_graph.py      # Top 10 stores bar chart
├── weekly_sales_graph.py           # Weekly sales trend chart
├── train.csv                       # Training data
├── test.csv                        # Test dataset
├── features.csv                    # Additional feature dataset
├── stores.csv                      # Store information
├── static/
│   └── graph.png                  # Static graph asset
├── templates/
│   └── index.html                 # Front-end webpage
├── monthly_sales.png               # Generated monthly sales plot
├── boxplot_sales.png               # Generated boxplot image
├── correlation_heatmap.png        # Generated heatmap image
├── B13-Retail Sales Prediction System.pptx
├── B13-2-Retail Sales Prediction system.dox.zip
├── README.md
└── requirements.txt (if added later)
```

## Datasets

The project uses files such as:

- train.csv
- test.csv
- features.csv
- stores.csv

These files contain retail dataset column information like:

- Store
- Date
- Weekly_Sales
- Dept
- IsHoliday
- other store or promotional features

The exploratory scripts primarily load train.csv and generate graphs based on Weekly_Sales and related variables.

## Model and Prediction Logic

The main prediction logic is defined in `retail_prediction.py`:

- It creates a small example dataset
- Converts it into a Pandas DataFrame
- Uses `LinearRegression` from scikit-learn
- Trains a model on `store` and `feature` values
- Provides `predict_sales(store, feature)` for prediction

This is a simple demonstration model rather than a full production-grade forecasting system. The Flask app calls this function to generate a predicted value.

## How the Web App Works

The Flask app in `app.py` performs the following steps:

1. Starts a web server on localhost
2. Loads the homepage template from `templates/index.html`
3. Accepts `store` and `feature` values via a form
4. Calls `predict_sales(store, feature)`
5. Displays the prediction result in the browser

### App routes

- `GET /` → loads the homepage
- `POST /predict` → processes the prediction request

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/srushtihiremath-dev/Retail-Sales-Prediction-System.git
cd Retail-Sales-Prediction-System
```

### 2. Create a virtual environment

On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask pandas scikit-learn matplotlib seaborn phonenumbers
```

If you are using a requirements file in the future, you can also do:

```bash
pip install -r requirements.txt
```

### 4. Start the Flask app

```bash
python app.py
```

### 5. Open the application

Visit:

```text
http://127.0.0.1:5000/
```

Then enter:

- Store ID
- Feature Value

and click Predict.

## Running the Analysis Scripts

Several scripts in the repository are standalone analysis tools.

### Example: monthly sales trend

```bash
python monthly_trend.py
```

This generates a monthly_sales.png chart.

### Example: boxplot generation

```bash
python boxplot.py
```

### Example: correlation heatmap

```bash
python correlation.py
```

### Example: holiday sales graph

```bash
python holiday_sales_graph.py
```

### Example: top store sales graph

```bash
python store_sales_graph.py
```

### Example: user input-based prediction

```bash
python userinput.py
```

This script prompts the user for a store and department number and then prints a prediction.

## Important Notes

- The main machine learning model is intentionally simple and based on a small demonstration dataset in `retail_prediction.py`.
- The project also contains EDA scripts that visualize trends in the retail dataset, which are useful for understanding sales behavior.
- Some scripts are data exploration tools rather than part of the web application itself.
- The repository includes presentation/documentation files (PPT and .dox archive), but they are not required to run the code.

## Example of the App Interface

The HTML interface in `templates/index.html` includes:

- a form with `Store ID`
- a `Feature Value` input
- a `Predict` button
- a result display showing the predicted sales value

## Troubleshooting

### Module not found error

If you see errors such as `No module named flask` or `No module named pandas`, install the required dependencies again:

```bash
pip install flask pandas scikit-learn matplotlib seaborn phonenumbers
```

### App does not start

Make sure you are in the project directory and that Python is pointing to the correct environment:

```bash
python --version
python app.py
```

### File not found errors

Some scripts expect files like `train.csv` to be present in the project root. Ensure the repository has not been moved or the dataset files are still in the same folder.

## Future Improvements

Possible enhancements for this project include:

- Replace the toy model with a real dataset-driven regression model
- Use more relevant retail features such as `Dept`, `IsHoliday`, `Temperature`, and store metadata
- Add model validation and evaluation metrics
- Add a proper requirements.txt file
- Deploy the app using Flask hosting or cloud deployment
- Improve the UI using CSS and a better dashboard design

## Conclusion

This project demonstrates a simple retail sales prediction system combining a basic machine learning model with web-based interaction and data visualization. It is suitable for learning how Python, Flask, pandas, matplotlib, and scikit-learn can be used together for data analysis and forecasting tasks.

## Project Status

The repository is currently a learning/demo project and is not a production-grade sales forecasting system. It is useful as a practical implementation for academic or beginner-level machine learning and web application development.

## Notes for the Author / Maintainer

This project is intended for education and demonstration. If you want to enhance it further, consider connecting the app to the real `train.csv` and `test.csv` data and replacing the simplified model with one trained on the full dataset.

---

If you want, I can also generate a polished `requirements.txt` file and improve the app code to make it run more realistically with the actual retail datasets.
