import requests
from bs4 import BeautifulSoup
import re
import pandas as pd 

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