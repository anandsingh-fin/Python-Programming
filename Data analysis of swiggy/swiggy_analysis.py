# Import the libraries we just installed
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load the dataset from the CSV file into a pandas DataFrame
# A DataFrame is like a table for your data in Python
df = pd.read_csv('swiggy state .csv')

print("--- 1. First 5 Rows of the Dataset ---")
print(df.head())

print("\n--- 2. Dataset Information (Columns, Data Types, Nulls) ---")
df.info()

print("\n--- 3. Checking for Missing Values ---")
print(df.isnull().sum())

print("\n--- 4. Checking for Duplicate Rows ---")
print(f"Number of duplicate rows: {df.duplicated().sum()}")

# Add this code to the end of your swiggy_analysis.py file

print("\n--- 5. Descriptive Statistics ---")
print(df.describe())

# Add this code to the end of your file

# Set a nice style for our plots
sns.set_style("whitegrid")

# Plot 1: Distribution of Price
print("\nGenerating plot 1: Price Distribution...")
plt.figure(figsize=(10, 6)) # Creates a blank canvas for the plot
sns.histplot(df['Price'], bins=30, kde=True) # Puts the histogram on the canvas
plt.title('Distribution of Price for Two') # Adds a title
plt.xlabel('Price (in INR)') # Labels the x-axis
plt.ylabel('Number of Restaurants') # Labels the y-axis
plt.savefig('price_distribution.png') # Saves the plot as an image
plt.clf() # Clears the canvas for the next plot

# Plot 2: Top 10 Cities
print("Generating plot 2: Top 10 Cities...")
plt.figure(figsize=(12, 7))
city_counts = df['City'].value_counts().nlargest(10)
sns.barplot(x=city_counts.index, y=city_counts.values, palette='viridis')
plt.title('Top 10 Cities with the Most Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=45, ha='right')
plt.tight_layout() # Adjusts plot to prevent labels from overlapping
plt.savefig('top_10_cities.png')
plt.clf()

# Plot 3: Price vs. Rating Scatterplot
print("Generating plot 3: Price vs. Rating...")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Avg ratings', data=df, alpha=0.5)
plt.title('Price vs. Average Rating')
plt.xlabel('Price (in INR)')
plt.ylabel('Average Rating')
plt.savefig('price_vs_rating.png')
plt.clf()

# Plot 4: Top 15 Cuisines
print("Generating plot 4: Top Cuisines...")
# First, process the text data
cuisine_counts = Counter(','.join(df['Food type'].dropna()).split(','))
cuisine_counts_cleaned = Counter()
for cuisine, count in cuisine_counts.items():
    cuisine_counts_cleaned[cuisine.strip()] += count
top_15_cuisines = cuisine_counts_cleaned.most_common(15)
df_cuisines = pd.DataFrame(top_15_cuisines, columns=['Cuisine', 'Count'])

# Now, create the plot
plt.figure(figsize=(12, 8))
sns.barplot(x='Count', y='Cuisine', data=df_cuisines, palette='rocket')
plt.title('Top 15 Most Common Cuisines on Swiggy')
plt.xlabel('Number of Restaurants')
plt.ylabel('Cuisine')
plt.tight_layout()
plt.savefig('top_15_cuisines.png')
plt.clf()

print("\nAll visualizations have been successfully generated and saved!")