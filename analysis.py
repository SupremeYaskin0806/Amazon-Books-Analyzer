import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/bestsellers with categories.csv")


# ==================== DATASET OVERVIEW ====================

print("========== DATASET OVERVIEW ==========")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Information:")
df.info()

print("\nBasic Statistics:")
print(df.describe())


# ==================== AUTHOR ANALYSIS ====================

print("\n========== AUTHOR ANALYSIS ==========")

print("\nTop 10 Authors:")
print(df["Author"].value_counts().head(10))


# ==================== BOOK ANALYSIS ====================

print("\n========== BOOK ANALYSIS ==========")

print("\nTop 10 Highest Rated Books:")
print(
    df.sort_values(
        "User Rating",
        ascending=False
    )[["Name", "Author", "User Rating"]].head(10)
)

print("\nTop 10 Most Reviewed Books:")
print(
    df.sort_values(
        "Reviews",
        ascending=False
    )[["Name", "Author", "Reviews"]].head(10)
)

print("\nUnique Books:")
print(df["Name"].nunique())


# ==================== GENRE ANALYSIS ====================

print("\n========== GENRE ANALYSIS ==========")

genre_counts = df["Genre"].value_counts()

print("\nBooks by Genre:")
print(genre_counts)

print("\nAverage Rating by Genre:")
print(df.groupby("Genre")["User Rating"].mean())

print("\nAverage Price by Genre:")
print(df.groupby("Genre")["Price"].mean())


# ==================== YEAR ANALYSIS ====================

print("\n========== YEAR ANALYSIS ==========")

year_counts = df["Year"].value_counts().sort_index()
year_rating = df.groupby("Year")["User Rating"].mean()

print("\nBooks Published by Year:")
print(year_counts)

print("\nAverage Rating by Year:")
print(year_rating)


# ==================== KEY INSIGHTS ====================

print("\n========== KEY INSIGHTS ==========")

print("Average User Rating:", round(df["User Rating"].mean(), 2))
print("Average Price:", round(df["Price"].mean(), 2))
print("Average Reviews:", round(df["Reviews"].mean(), 2))

print("\nMost Expensive Book:")
print(
    df.loc[
        df["Price"].idxmax(),
        ["Name", "Author", "Price"]
    ]
)

print("\nBook With Most Reviews:")
print(
    df.loc[
        df["Reviews"].idxmax(),
        ["Name", "Author", "Reviews"]
    ]
)

print("\nHighest Rated Book:")
print(
    df.loc[
        df["User Rating"].idxmax(),
        ["Name", "Author", "User Rating"]
    ]
)


# ==================== DATA CLEANING ====================

print("\n========== DATA CLEANING ==========")

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_count)

df_clean = df.drop_duplicates()

print("Rows After Removing Duplicates:", len(df_clean))

print("\nMissing Values:")
print(df_clean.isnull().sum())


# ==================== CORRELATION ANALYSIS ====================

print("\n========== CORRELATION ANALYSIS ==========")

correlation = df_clean[
    ["User Rating", "Reviews", "Price", "Year"]
].corr()

print(correlation)


# ==================== TOP BOOKS ANALYSIS ====================

print("\n========== TOP BOOKS ANALYSIS ==========")

top_books = df_clean.sort_values(
    ["User Rating", "Reviews"],
    ascending=[False, False]
)[["Name", "Author", "User Rating", "Reviews"]].head(10)

print("\nTop 10 Books by Rating and Reviews:")
print(top_books)


# ==================== UNIQUE BOOK ANALYSIS ====================

print("\n========== UNIQUE BOOK ANALYSIS ==========")

unique_books = df_clean.drop_duplicates(subset=["Name"])

print("Total Unique Books:", len(unique_books))

top_unique_books = unique_books.sort_values(
    ["User Rating", "Reviews"],
    ascending=[False, False]
)[["Name", "Author", "User Rating", "Reviews"]].head(10)

print("\nTop 10 Unique Books by Rating and Reviews:")
print(top_unique_books)


# ==================== FINAL SUMMARY ====================

print("\n========== FINAL SUMMARY ==========")

print("Total Records:", len(df))
print("Unique Books:", df["Name"].nunique())
print("Unique Authors:", df["Author"].nunique())

highest = df.loc[df["User Rating"].idxmax()]
most_reviewed = df.loc[df["Reviews"].idxmax()]

print("\nHighest Rated Book:")
print("Name:", highest["Name"])
print("Author:", highest["Author"])
print("Rating:", highest["User Rating"])

print("\nMost Reviewed Book:")
print("Name:", most_reviewed["Name"])
print("Author:", most_reviewed["Author"])
print("Reviews:", most_reviewed["Reviews"])

print("\nMost Common Genre:")
print(df["Genre"].value_counts().idxmax())

print("\nAverage Rating:")
print(round(df["User Rating"].mean(), 2))

print("\nAverage Price:")
print(round(df["Price"].mean(), 2))

print("\nBest Year by Average Rating:")
print(
    year_rating.idxmax(),
    "->",
    round(year_rating.max(), 3)
)


# ==================== VISUALIZATIONS ====================

# Genre Distribution
plt.figure(figsize=(8, 6))

bars = plt.bar(
    genre_counts.index,
    genre_counts.values
)

plt.title("Fiction vs Non-Fiction Books")
plt.xlabel("Genre")
plt.ylabel("Number of Books")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.tight_layout()


# Top Authors
author_counts = df["Author"].value_counts().head(10)

plt.figure(figsize=(10, 6))

bars = plt.bar(
    author_counts.index,
    author_counts.values
)

plt.title("Top 10 Authors by Bestseller Appearances")
plt.xlabel("Author")
plt.ylabel("Number of Appearances")
plt.xticks(rotation=45, ha="right")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        int(bar.get_height()),
        ha="center",
        va="bottom"
    )

plt.tight_layout()


# Ratings vs Reviews
plt.figure(figsize=(10, 6))

plt.scatter(
    df["Reviews"],
    df["User Rating"],
    alpha=0.6
)

plt.title("Book Ratings vs Number of Reviews")
plt.xlabel("Number of Reviews")
plt.ylabel("User Rating")

plt.tight_layout()


# Average Rating by Genre
avg_rating = df.groupby("Genre")["User Rating"].mean()

plt.figure(figsize=(8, 6))

bars = plt.bar(
    avg_rating.index,
    avg_rating.values
)

plt.title("Average User Rating by Genre")
plt.xlabel("Genre")
plt.ylabel("Average User Rating")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"{bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()


# Average Price by Genre
avg_price = df.groupby("Genre")["Price"].mean()

plt.figure(figsize=(8, 6))

bars = plt.bar(
    avg_price.index,
    avg_price.values
)

plt.title("Average Book Price by Genre")
plt.xlabel("Genre")
plt.ylabel("Average Price")

for bar in bars:
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"${bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()


# Books Published by Year
plt.figure(figsize=(10, 6))

plt.plot(
    year_counts.index,
    year_counts.values,
    marker="o"
)

plt.title("Number of Bestseller Books by Year")
plt.xlabel("Year")
plt.ylabel("Number of Books")
plt.xticks(year_counts.index, rotation=45)

plt.tight_layout()


# Average Rating by Year
plt.figure(figsize=(10, 6))

plt.plot(
    year_rating.index,
    year_rating.values,
    marker="o"
)

plt.title("Average User Rating by Year")
plt.xlabel("Year")
plt.ylabel("Average User Rating")
plt.xticks(year_rating.index, rotation=45)

plt.tight_layout()


# Top 10 Most Reviewed Books
top_reviews = df.sort_values(
    "Reviews",
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

bars = plt.barh(
    top_reviews["Name"],
    top_reviews["Reviews"]
)

plt.title("Top 10 Most Reviewed Books")
plt.xlabel("Number of Reviews")
plt.ylabel("Book")

plt.gca().invert_yaxis()

for bar in bars:
    plt.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f"{int(bar.get_width())}",
        va="center"
    )

plt.tight_layout()

plt.show()