import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import matplotlib.pyplot as plt


# Data Analytics Tasks & Instructions — CodeAlpha
# TASK 1: Web Scraping

# Storing Anime Planet URL
url = "https://www.anime-planet.com/anime/all"

# Requesting the webpage
response = requests.get(url)

# Checking the response
print(response.status_code)

# Storing the HTML
html = response.text

# Creating the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Finding all anime cards
cards = soup.find_all("li", class_="card")

# Creating an empty list
anime_data = []

# Extracting information from each anime card
for card in cards:

    # Finding the anime link
    link = card.find("a", class_=lambda x: x and "anime" in x)

    # Finding the anime title
    title = card.find("h3", class_="cardName").text.strip()

    # Extracting the URL
    anime_url = "https://www.anime-planet.com" + link["href"]

    # Extracting the rating from the title attribute
    rating_match = re.search(
        r"class='ttRating'>(.*?)</div>",
        link["title"]
    )

    if rating_match:
        rating = rating_match.group(1)
    else:
        rating = None

    # Adding the information to our dataset
    anime_data.append({
        "Title": title,
        "Rating": rating,
        "URL": anime_url
    })

# Printing the dataset
for anime in anime_data:
    print(anime)

# Creating a DataFrame
df = pd.DataFrame(anime_data)

# Converting Rating from text to numbers
df["Rating"] = pd.to_numeric(df["Rating"])

# Displaying the dataset
print(df)

# Saving the dataset as a CSV file
df.to_csv("anime_dataset.csv", index=False)

print("Dataset saved successfully!")

# Loading the scraped dataset
df = pd.read_csv("anime_dataset.csv")

# Displaying the first 5 rows
print(df.head())

# Checking the number of rows and columns
print(df.shape)

# Checking the column names
print(df.columns)

# Checking the data type of the Rating column
print(df["Rating"].dtype)

# Calculating the average anime rating
average_rating = df["Rating"].mean()

print("Average anime rating:", average_rating)

# Data Analytics Tasks & Instructions — CodeAlpha
# TASK 2: Exploratory Data Analysis (EDA)

# Questions to investigate:
# 1. What is the average rating of the anime in the dataset?
# 2. What is the highest and lowest rating?
# 3. How are the ratings distributed?
# 4. Are there any missing or duplicate records?
# 5. Is the dataset heavily concentrated around one rating?

# Load the dataset
df = pd.read_csv("anime_dataset.csv")

print(df)

# Testig the structure
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# Checking whether the data was loaded correctly
print("\nFirst 5 Records:")
print(df.head())

# Checking for missing data
print("\nMissing Values:")
print(df.isnull().sum())

# Checking for duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Checking for duplicate anime titles
print("\nDuplicate Titles:")
print(df["Title"].duplicated().sum())

# Analyzing the ratings
print("\nRating Statistics:")
print(df["Rating"].describe())

# Find the highest and lowest ratings
print("\nHighest Rating:")
print(df["Rating"].max())

print("\nLowest Rating:")
print(df["Rating"].min())

# Finding the anime with the highest rating
highest_rating = df["Rating"].max()

print("\nAnime with the Highest Rating:")
print(df[df["Rating"] == highest_rating][["Title", "Rating"]])

# Look at the rating distribution
print("\nRating Counts:")
print(df["Rating"].value_counts().sort_index())

# Creating visualization using a bar chart 
rating_counts = df["Rating"].value_counts().sort_index()

rating_counts.plot(kind="bar")

plt.title("Anime Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Anime")
plt.xticks(rotation=0)
plt.show()

# Testing the hypothesis that most anime have a rating of 4.5

rating_45_count = (df["Rating"] == 4.5).sum()
total_anime = len(df)

percentage_45 = (rating_45_count / total_anime) * 100

print("\nHypothesis Test:")
print("Anime rated 4.5:", rating_45_count)
print("Percentage rated 4.5:", percentage_45, "%")

# EDA Findings:
# The dataset contains 35 anime records and 3 variables: Title, Rating, and URL.
# The Title and URL columns contain text data, while Rating is numerical data.
# There are no missing values, duplicate rows, or duplicate anime titles.
# The ratings range from 4.4 to 4.6, with an average rating of approximately 4.51.
# Most anime in the dataset have a rating of 4.5.
# 29 out of 35 anime (approximately 82.9%) have a rating of 4.5.
# Four anime have the highest rating of 4.6, while two anime have the lowest rating of 4.4.
# The small rating range indicates that the scraped dataset is concentrated around
# highly rated anime and does not contain a wide range of ratings.