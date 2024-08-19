# PhonePe Pulse Data Visualization and Exploration

## Project Overview

The PhonePe Pulse Data Visualization and Exploration project is a user-friendly tool built using Streamlit and Plotly. The project focuses on extracting, transforming, and visualizing data from the PhonePe Pulse GitHub repository. The goal is to provide an interactive and visually appealing dashboard that offers valuable insights into various metrics and statistics related to PhonePe transactions and user registrations.

## Technologies

- **Github Cloning**: To fetch the data from the PhonePe Pulse GitHub repository.
- **Python**: For scripting and data manipulation.
- **Pandas**: For data processing and transformation.
- **MySQL**: For efficient data storage and retrieval.
- **mysql-connector-python**: For connecting Python to MySQL.
- **Streamlit**: For creating the interactive web application.
- **Plotly**: For creating interactive visualizations.

## Domain

Fintech

## Problem Statement

The PhonePe Pulse GitHub repository contains extensive data on various metrics and statistics. The objective is to extract this data, process it to gain insights, and visualize it in a user-friendly manner. The solution should include:

1. Extracting data from the PhonePe Pulse GitHub repository through scripting and cloning.
2. Transforming the data into a suitable format, performing necessary cleaning, and preprocessing steps.
3. Inserting the transformed data into a MySQL database for efficient storage and retrieval.
4. Creating a live geo-visualization dashboard using Streamlit and Plotly to display the data interactively.
5. Fetching the data from the MySQL database to display it on the dashboard.
6. Providing at least 10 different dropdown options for users to select various facts and figures on the dashboard.

## Solution Approach

1. **Data Extraction**: Cloned the GitHub repository using Python scripts to fetch data from the PhonePe Pulse repository and stored it in CSV formats.
2. **Data Transformation**: Cleaned and transformed the data using Pandas, handling missing values and preparing it for analysis and visualization.
3. **Database Insertion**: Created a MySQL database using `mysql-connector-python`, defined how the data should be stored, and inserted the transformed data.
4. **Dashboard Creation**: Developed an interactive dashboard using Streamlit and Plotly. The dashboard includes live geo-visualizations and various dropdown options for users to interact with different data views.
5. **Data Retrieval**: Implemented functionality to fetch and dynamically update the data from the MySQL database into the dashboard.

### Additional Details

- **Data Extraction and Cleaning**: Cloned the data from the GitHub repository, cleaned it, and created a MySQL database. The data processing and database creation were handled in `phonepe.py`.
- **Visualization and Dashboard**: Implemented all functions for data visualization and dashboard creation in `phonepe_app.py`.

## Results

The project results in a live geo-visualization dashboard that presents insights from the PhonePe Pulse GitHub repository interactively. Users can access the dashboard via a web browser, select different options from at least 10 dropdowns, and view various facts and figures. The data is stored efficiently in a MySQL database, and the dashboard dynamically reflects the latest information.

The completed dashboard provides valuable insights into PhonePe transaction metrics and user registrations, making it a comprehensive tool for data analysis and decision-making.

## Getting Started

To run this project locally:

1. Clone the repository:
   ```bash
   git clone [repository-url]
