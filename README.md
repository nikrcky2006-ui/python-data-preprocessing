# python-data-preprocessing
# Employee Data Cleaning Project

## Overview

This project focuses on cleaning and preprocessing a dirty employee dataset using Python and Pandas.

The dataset contained:

* Missing values
* Duplicate records
* Inconsistent data
* Invalid entries

The project demonstrates basic data preprocessing and exploratory data analysis (EDA) techniques used in real-world data analysis workflows.

---

## Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn

---

## Features

* Loaded CSV dataset using Pandas
* Checked dataset information and statistics
* Identified missing values
* Removed duplicate records
* Filled missing values using:

  * Mean
  * Median
  * Mode
* Performed basic data visualization
* Exported cleaned dataset to a new CSV file

---

## Dataset Operations

### Missing Value Handling

* Employee_ID → Filled using Mode
* Department → Filled with "Unknown"
* Salary → Filled using Mean
* Age → Filled using Median
* Name → Filled with "Unknown"

### Duplicate Handling

* Removed duplicate rows
* Reset dataset index after cleaning

---

## Visualizations

The project includes:

* Salary Distribution Histogram
* Salary Boxplot for Outlier Detection

---

## Project Structure

```bash
employee-data-cleaning/
│
├── data/
│   ├── dirty_dataset.csv
│   └── cleaned_dataset.csv
│
├── prepos.py
├── README.md
└── screenshots/
```

---

## How to Run

### Install Required Libraries

```bash
pip install pandas matplotlib seaborn
```

### Run the Project

```bash
python prepos.py
```

---

## Output

The cleaned dataset is exported as:

```bash
cleaned_dataset.csv
```

---

## Learning Outcomes

Through this project, I learned:

* Data cleaning techniques
* Handling missing values
* Exploratory Data Analysis (EDA)
* Data preprocessing using Pandas
* Basic visualization using Matplotlib and Seaborn

---

## Author

Nikhil Kumar

Aspiring AI & Data Science Learner 🚀
