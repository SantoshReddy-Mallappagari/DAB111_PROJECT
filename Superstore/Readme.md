# Superstore Dashboard

## Overview

The **Superstore Dashboard** is a web application that provides insights from the **Superstore Sales Dataset**. This project uses Python, Flask, SQLite, and Pandas to display key information about Superstore sales, including data visualization and exploration.

The dataset contains information about sales transactions, including product categories, sales amounts, quantities, discounts, and profits, as well as location and customer segment details.

## Features

- **Home Page**: An introduction to the Superstore Dashboard.
- **About Page**: Information about the dataset, including column descriptions and data types.
- **Data Sample Page**: A sample of the Superstore dataset, displayed in a tabular format.

## Dataset

The Superstore dataset contains 9,994 entries (rows) and 13 columns, providing detailed information about sales transactions. The dataset includes columns such as:

- **Ship Mode**: The mode of shipment used for each order.
- **Segment**: The market segment of the customer.
- **Country, City, State, Postal Code**: Location details of the customer.
- **Region**: The region within the country where the order was placed.
- **Category and Sub-Category**: The product category and subcategory.
- **Sales, Quantity, Discount, Profit**: Sales-related data, including discounts and profits.

Dataset source: [Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/roopacalistus/superstore).

## Requirements

To run this project locally, you'll need to install the following dependencies:

- **Flask**: For creating the web application.
- **SQLite3**: For storing and querying the Superstore data.
- **Pandas**: For data processing and manipulation.

You can install these dependencies by running:

```bash
pip install -r requirements.txt
