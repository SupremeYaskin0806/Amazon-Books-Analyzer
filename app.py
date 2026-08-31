import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Amazon Books Analyzer",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .dashboard-title {
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .dashboard-subtitle {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 28px;
        font-weight: 700;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .metric-card {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        background-color: rgba(128,128,128,0.06);
        text-align: center;
    }

    .metric-title {
        font-size: 15px;
        color: #9ca3af;
        margin-bottom: 8px;
    }

    .metric-value {
        font-size: 30px;
        font-weight: 700;
    }

    .insight-card {
        padding: 18px;
        border-radius: 12px;
        border: 1px solid rgba(128,128,128,0.25);
        background-color: rgba(128,128,128,0.06);
        margin-bottom: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    data = pd.read_csv("data/bestsellers with categories.csv")

    data["User Rating"] = pd.to_numeric(
        data["User Rating"],
        errors="coerce"
    )

    data["Reviews"] = pd.to_numeric(
        data["Reviews"],
        errors="coerce"
    )

    data["Price"] = pd.to_numeric(
        data["Price"],
        errors="coerce"
    )

    data["Year"] = pd.to_numeric(
        data["Year"],
        errors="coerce"
    )

    data = data.dropna(
        subset=[
            "Name",
            "Author",
            "User Rating",
            "Reviews",
            "Price",
            "Year",
            "Genre"
        ]
    )

    return data


df = load_data()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("🔎 Filters")

st.sidebar.markdown("### Filter the Dataset")

genre_options = ["All"] + sorted(
    df["Genre"].dropna().unique().tolist()
)

selected_genre = st.sidebar.selectbox(
    "Select Genre",
    genre_options
)


year_options = ["All"] + sorted(
    df["Year"].dropna().astype(int).unique().tolist()
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    year_options
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_genre != "All":
    filtered_df = filtered_df[
        filtered_df["Genre"] == selected_genre
    ]


if selected_year != "All":
    filtered_df = filtered_df[
        filtered_df["Year"] == int(selected_year)
    ]


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="dashboard-title">📚 Amazon Books Analyzer</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="dashboard-subtitle">
    Interactive analysis of Amazon bestselling books based on
    ratings, reviews, prices, authors, genres, and publication years.
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# FILTER STATUS
# ============================================================

if selected_genre == "All" and selected_year == "All":

    st.info(
        "Showing analysis for the complete dataset."
    )

else:

    filter_text = []

    if selected_genre != "All":
        filter_text.append(f"Genre: {selected_genre}")

    if selected_year != "All":
        filter_text.append(f"Year: {selected_year}")

    st.info(
        " | ".join(filter_text)
    )


# ============================================================
# KEY STATISTICS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Key Statistics</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)


total_books = len(filtered_df)

average_rating = (
    filtered_df["User Rating"].mean()
    if len(filtered_df) > 0
    else 0
)

average_price = (
    filtered_df["Price"].mean()
    if len(filtered_df) > 0
    else 0
)

total_reviews = (
    filtered_df["Reviews"].sum()
    if len(filtered_df) > 0
    else 0
)


with col1:
    st.metric(
        "📚 Total Books",
        f"{total_books:,}"
    )

with col2:
    st.metric(
        "⭐ Average Rating",
        f"{average_rating:.2f}"
    )

with col3:
    st.metric(
        "💰 Average Price",
        f"${average_price:.2f}"
    )

with col4:
    st.metric(
        "📝 Total Reviews",
        f"{total_reviews:,.0f}"
    )


# ============================================================
# DATASET
# ============================================================

st.markdown(
    '<div class="section-title">📖 Books Dataset</div>',
    unsafe_allow_html=True
)

display_columns = [
    "Name",
    "Author",
    "User Rating",
    "Reviews",
    "Price",
    "Year",
    "Genre"
]

st.dataframe(
    filtered_df[display_columns],
    width="stretch",
    hide_index=True
)


# ============================================================
# GENRE ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">📊 Genre Analysis</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)


with col1:

    genre_counts = (
        filtered_df["Genre"]
        .value_counts()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(
        genre_counts.index,
        genre_counts.values
    )

    ax.set_title(
        "Books by Genre",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("Genre")
    ax.set_ylabel("Number of Books")

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{int(bar.get_height())}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    st.pyplot(
        fig,
        width="stretch"
    )

    plt.close(fig)


with col2:

    avg_rating_genre = (
        filtered_df
        .groupby("Genre")["User Rating"]
        .mean()
        .sort_values(ascending=False)
    )

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(
        avg_rating_genre.index,
        avg_rating_genre.values
    )

    ax.set_title(
        "Average Rating by Genre",
        fontsize=15,
        fontweight="bold"
    )

    ax.set_xlabel("Genre")
    ax.set_ylabel("Average Rating")

    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height(),
            f"{bar.get_height():.2f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    st.pyplot(
        fig,
        width="stretch"
    )

    plt.close(fig)


# ============================================================
# PRICE ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">💰 Price Analysis</div>',
    unsafe_allow_html=True
)

avg_price_genre = (
    filtered_df
    .groupby("Genre")["Price"]
    .mean()
    .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.bar(
    avg_price_genre.index,
    avg_price_genre.values
)

ax.set_title(
    "Average Book Price by Genre",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Genre")
ax.set_ylabel("Average Price ($)")

for bar in bars:
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        f"${bar.get_height():.2f}",
        ha="center",
        va="bottom"
    )

plt.tight_layout()

st.pyplot(
    fig,
    width="stretch"
)

plt.close(fig)


# ============================================================
# AUTHOR ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">👤 Top Authors</div>',
    unsafe_allow_html=True
)

author_counts = (
    filtered_df["Author"]
    .value_counts()
    .head(10)
    .sort_values()
)

fig, ax = plt.subplots(figsize=(10, 6))

bars = ax.barh(
    author_counts.index,
    author_counts.values
)

ax.set_title(
    "Top 10 Authors by Bestseller Appearances",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Number of Appearances")
ax.set_ylabel("Author")

for bar in bars:
    ax.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f"{int(bar.get_width())}",
        va="center"
    )

plt.tight_layout()

st.pyplot(
    fig,
    width="stretch"
)

plt.close(fig)


# ============================================================
# RATINGS VS REVIEWS
# ============================================================

st.markdown(
    '<div class="section-title">⭐ Ratings vs Reviews</div>',
    unsafe_allow_html=True
)

fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(
    filtered_df["Reviews"],
    filtered_df["User Rating"],
    alpha=0.6
)

ax.set_title(
    "Book Ratings vs Number of Reviews",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Number of Reviews")
ax.set_ylabel("User Rating")

plt.tight_layout()

st.pyplot(
    fig,
    width="stretch"
)

plt.close(fig)


# ============================================================
# YEAR ANALYSIS
# ============================================================

st.markdown(
    '<div class="section-title">📅 Year-wise Analysis</div>',
    unsafe_allow_html=True
)

year_counts = (
    filtered_df["Year"]
    .value_counts()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    year_counts.index,
    year_counts.values,
    marker="o"
)

ax.set_title(
    "Number of Bestseller Books by Year",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Year")
ax.set_ylabel("Number of Books")

ax.set_xticks(year_counts.index)

plt.xticks(
    rotation=45
)

plt.tight_layout()

st.pyplot(
    fig,
    width="stretch"
)

plt.close(fig)


# ============================================================
# AVERAGE RATING BY YEAR
# ============================================================

year_rating = (
    filtered_df
    .groupby("Year")["User Rating"]
    .mean()
    .sort_index()
)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(
    year_rating.index,
    year_rating.values,
    marker="o"
)

ax.set_title(
    "Average User Rating by Year",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Year")
ax.set_ylabel("Average User Rating")

ax.set_xticks(year_rating.index)

plt.xticks(
    rotation=45
)

plt.tight_layout()

st.pyplot(
    fig,
    width="stretch"
)

plt.close(fig)


# ============================================================
# TOP 10 MOST REVIEWED BOOKS
# ============================================================

st.markdown(
    '<div class="section-title">🔥 Top 10 Most Reviewed Books</div>',
    unsafe_allow_html=True
)

top_reviews = (
    filtered_df
    .sort_values(
        "Reviews",
        ascending=False
    )
    .head(10)
    .sort_values("Reviews")
)

fig, ax = plt.subplots(figsize=(11, 7))

bars = ax.barh(
    top_reviews["Name"],
    top_reviews["Reviews"]
)

ax.set_title(
    "Top 10 Most Reviewed Books",
    fontsize=15,
    fontweight="bold"
)

ax.set_xlabel("Number of Reviews")
ax.set_ylabel("Book")

for bar in bars:
    ax.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        f"{int(bar.get_width()):,}",
        va="center"
    )

plt.tight_layout()

st.pyplot(
    fig,
    width="stretch"
)

plt.close(fig)


# ============================================================
# TOP RATED BOOKS
# ============================================================

st.markdown(
    '<div class="section-title">🏆 Top Rated Books</div>',
    unsafe_allow_html=True
)

top_rated = (
    filtered_df
    .sort_values(
        ["User Rating", "Reviews"],
        ascending=[False, False]
    )
    .head(10)
)

st.dataframe(
    top_rated[
        [
            "Name",
            "Author",
            "User Rating",
            "Reviews",
            "Price",
            "Year",
            "Genre"
        ]
    ],
    width="stretch",
    hide_index=True
)


# ============================================================
# KEY INSIGHTS
# ============================================================

st.markdown(
    '<div class="section-title">💡 Key Insights</div>',
    unsafe_allow_html=True
)

if len(filtered_df) > 0:

    highest_rated = filtered_df.loc[
        filtered_df["User Rating"].idxmax()
    ]

    most_reviewed = filtered_df.loc[
        filtered_df["Reviews"].idxmax()
    ]

    most_expensive = filtered_df.loc[
        filtered_df["Price"].idxmax()
    ]

    most_common_genre = (
        filtered_df["Genre"]
        .value_counts()
        .idxmax()
    )

    best_year = (
        filtered_df
        .groupby("Year")["User Rating"]
        .mean()
        .idxmax()
    )

    best_year_rating = (
        filtered_df
        .groupby("Year")["User Rating"]
        .mean()
        .max()
    )

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            f"""
            <div class="insight-card">
            🏆 <b>Highest Rated Book</b><br>
            {highest_rated["Name"]}<br>
            ⭐ Rating: {highest_rated["User Rating"]:.1f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="insight-card">
            🔥 <b>Most Reviewed Book</b><br>
            {most_reviewed["Name"]}<br>
            📝 Reviews: {most_reviewed["Reviews"]:,.0f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="insight-card">
            💰 <b>Most Expensive Book</b><br>
            {most_expensive["Name"]}<br>
            💵 Price: ${most_expensive["Price"]:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="insight-card">
            📚 <b>Most Common Genre</b><br>
            {most_common_genre}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="insight-card">
            📅 <b>Best Year by Average Rating</b><br>
            {int(best_year)}<br>
            ⭐ Average Rating: {best_year_rating:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            f"""
            <div class="insight-card">
            👥 <b>Unique Authors</b><br>
            {filtered_df["Author"].nunique():,}
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center; color:#9ca3af;">
        📚 Amazon Books Analyzer
        <br>
        Built with Python • Pandas • Matplotlib • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)