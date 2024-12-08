from flask import Flask, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    description = """
    This dataset represents the sales data of a retail store. It includes various attributes like product categories, customer details, sales numbers, and discounts applied.
    The dataset contains 9994 records and 13 columns, and provides valuable insights for business analysis.
    """
    dataset_source = "The dataset is sourced from Kaggle: https://www.kaggle.com/datasets/roopacalistus/superstore"
    return render_template('about.html', description=description, source=dataset_source)

@app.route('/data')
def data():
    # Load data from CSV or SQLite database
    conn = sqlite3.connect('superstore.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM superstore LIMIT 10')  # Show a sample of 10 rows
    data = cursor.fetchall()
    conn.close()
    return render_template('data.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
