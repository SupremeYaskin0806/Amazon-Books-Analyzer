# Amazon Books Analyzer

A Python-based Exploratory Data Analysis project analyzing Amazon bestselling books to identify trends in ratings, reviews, pricing, genres, authors, and publication years.

## Project Overview

This project performs Exploratory Data Analysis (EDA) on an Amazon bestselling books dataset containing 550 records.

The analysis explores:

- Book ratings and reviews
- Book pricing trends
- Bestseller appearances by author
- Fiction vs Non-Fiction distribution
- Year-wise publishing trends
- Relationships between ratings, reviews, price, and publication year
- Highly rated and highly reviewed books

## Technologies Used

- Python
- Pandas
- Matplotlib

## Dataset

The dataset contains the following attributes:

| Column | Description |
|---|---|
| `Name` | Book title |
| `Author` | Book author |
| `User Rating` | Average user rating |
| `Reviews` | Number of user reviews |
| `Price` | Book price |
| `Year` | Publication year |
| `Genre` | Fiction or Non Fiction |

## Analysis Performed

### Exploratory Data Analysis

- Dataset shape and structure
- Column and data type analysis
- Statistical summary
- Author frequency analysis
- Genre distribution
- Rating analysis
- Review analysis
- Price analysis
- Year-wise analysis
- Unique book analysis

### Data Cleaning

- Checked for duplicate records
- Checked for missing values
- Removed duplicate records
- Created a cleaned dataset for analysis

### Statistical Analysis

- Correlation between ratings, reviews, price, and year
- Average rating by genre
- Average price by genre
- Average rating by year
- Books published each year
- Top books based on ratings and reviews

## Key Findings

- The dataset contains **550 records**.
- There are **351 unique book titles**.
- **Non Fiction** is the most common genre.
- The average user rating is approximately **4.62**.
- The average book price is approximately **$13.10**.
- **2019** has the highest average rating at approximately **4.74**.
- *Where the Crawdads Sing* has the highest number of reviews with **87,841 reviews**.
- **Jeff Kinney** has the highest number of bestseller appearances among the analyzed authors.

## Visualizations

The project uses Matplotlib to visualize:

- Fiction vs Non-Fiction book distribution
- Top 10 authors by bestseller appearances
- Book ratings vs number of reviews
- Average user rating by genre
- Average book price by genre
- Number of bestselling books by year
- Average user rating by year
- Top 10 most reviewed books

## Project Structure


Amazon-Books-Analyzer/
│
├── data/
│   └── bestsellers with categories.csv
│
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore


## Visualizations

### Genre Distribution

![Genre Distribution](Images/genre_distribution.png)

### Top Authors

![Top Authors](Images/top_authors.png)

### Ratings vs Reviews

![Ratings vs Reviews](Images/ratings_vs_reviews.png)

### Average Rating by Genre

![Average Rating by Genre](Images/average_rating_by_genre.png)

### Average Price by Genre

![Average Price by Genre](Images/average_price_by_genre.png)

### Books Published by Year

![Books Published by Year](Images/books_published_by_year.png)

### Top 10 Most Reviewed Books

![Top 10 Most Reviewed Books](Images/top_10_most_reviewed_books.png)
