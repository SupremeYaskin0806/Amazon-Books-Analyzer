# Amazon Books Analyzer

A Python-based data analysis project that explores Amazon bestselling books to identify trends in ratings, reviews, pricing, genres, authors, and publication years.

## Project Overview

This project performs Exploratory Data Analysis (EDA) on an Amazon bestselling books dataset containing 550 book records.

The analysis focuses on understanding:

- Book ratings
- Number of reviews
- Book prices
- Authors with the most bestseller appearances
- Fiction vs Non-Fiction distribution
- Year-wise publishing trends
- Relationships between ratings, reviews, price, and publication year
- Most popular and highly rated books

## Technologies Used

- Python
- Pandas
- Matplotlib
- NumPy

## Dataset

The dataset contains information about Amazon bestselling books with the following attributes:

- `Name` – Book title
- `Author` – Book author
- `User Rating` – Average user rating
- `Reviews` – Number of user reviews
- `Price` – Book price
- `Year` – Publication year
- `Genre` – Fiction or Non Fiction

## Analysis Performed

### Exploratory Data Analysis

- Dataset structure and column analysis
- Statistical summary
- Unique book analysis
- Author frequency analysis
- Genre distribution
- Rating analysis
- Review analysis
- Price analysis
- Year-wise analysis

### Data Cleaning

- Checked for duplicate records
- Checked for missing values
- Created a cleaned dataset for further analysis

### Statistical Analysis

- Correlation between ratings, reviews, price, and year
- Average rating by genre
- Average price by genre
- Average rating by year
- Books published each year

### Top Books

The project identifies:

- Highest-rated books
- Most-reviewed books
- Top books based on rating and reviews
- Most frequently appearing authors

## Key Findings

- The dataset contains **550 records**.
- There are **351 unique books**.
- **Non Fiction** is the most common genre.
- The average user rating is approximately **4.62**.
- The average book price is approximately **$13.10**.
- **2019** has the highest average user rating at approximately **4.74**.
- *Where the Crawdads Sing* has the highest number of reviews in the dataset, with **87,841 reviews**.
- **Jeff Kinney** has the highest number of bestseller appearances among the analyzed authors.

## Visualizations

The project uses Matplotlib to visualize:

- Fiction vs Non-Fiction book distribution
- Top authors by bestseller appearances
- Book ratings vs number of reviews
- Average user rating by genre
- Average book price by genre
- Number of bestselling books by year
- Average user rating by year

## Project Structure

```text
Amazon-Books-Analyzer/
│
├── data/
│   └── books.csv
│
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore