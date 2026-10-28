"""Hotel booking exploratory analysis, adapted from the supplied academic report.

This is a new, unexecuted implementation based on documented methods, not an
original source-code upload. Add data/hotels.csv and verify schema before running.
"""
from pathlib import Path
import re

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

DATA_PATH = Path("data/hotels.csv")
OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Dataset missing. Download the CSV from the Kaggle source described in README.md "
        "and save it as data/hotels.csv."
    )

df = pd.read_csv(DATA_PATH)
df.columns = df.columns.str.strip()
df = df.drop_duplicates().copy()

# Adapt mappings to actual source headers as needed. Never silently guess an
# unrecognized column or invent missing observations.
CANDIDATES = {
    "price": ["Room Price", "Price", "room_price", "price"],
    "rating": ["Rating", "rating", "Hotel Rating"],
    "location": ["Location", "location", "City", "city"],
    "room_type": ["Room Type", "room_type", "RoomType"],
    "bed_type": ["Bed Type", "bed_type", "BedType"],
    "reviews": ["Review Score", "review_score", "Number of Reviews", "Reviews", "reviews"],
}

def match_column(key):
    for name in CANDIDATES[key]:
        if name in df.columns:
            return name
    return None

columns = {key: match_column(key) for key in CANDIDATES}
print("Detected column mapping:", columns)
if not columns["price"] or not columns["rating"]:
    raise ValueError("Could not identify price/rating columns; inspect CSV header and edit CANDIDATES.")

def numeric(series):
    # Remove currency symbols and thousands separators, retain digits and signs.
    cleaned = series.astype(str).str.replace(r"[^0-9.\-]", "", regex=True)
    return pd.to_numeric(cleaned, errors="coerce")

df["price_numeric"] = numeric(df[columns["price"]])
df["rating_numeric"] = numeric(df[columns["rating"]])

# Keep missingness explicit rather than carrying one hotel's values to another.
print("Rows:", len(df))
print("Missing price:", df["price_numeric"].isna().sum())
print("Missing rating:", df["rating_numeric"].isna().sum())
print(df[["price_numeric", "rating_numeric"]].describe())

# Bins as reported in the academic project.
df["price_category"] = pd.cut(
    df["price_numeric"], bins=[0, 50000, 250000, 500000, np.inf],
    labels=["Low", "Medium", "High", "Luxury"], include_lowest=True,
)
df["rating_category"] = pd.cut(
    df["rating_numeric"], bins=[0, 4, 6, 8, 10],
    labels=["Poor", "Average", "Good", "Excellent"], include_lowest=True,
)

corr = df[["price_numeric", "rating_numeric"]].corr(numeric_only=True)
print("Price/rating correlation matrix:\n", corr)
corr.to_csv(OUTPUT_DIR / "correlation.csv")

plt.figure(figsize=(8, 5))
df["price_numeric"].dropna().hist(bins=30)
plt.xlabel("Room price (source currency; confirm units)")
plt.ylabel("Listing count")
plt.title("Distribution of Room Prices")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "price_distribution.png", dpi=150)
plt.close()

plt.figure(figsize=(7, 5))
plt.scatter(df["price_numeric"], df["rating_numeric"], alpha=0.35)
plt.xlabel("Room price")
plt.ylabel("Rating")
plt.title("Price vs Rating")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "price_vs_rating.png", dpi=150)
plt.close()

for category in ["location", "room_type", "bed_type"]:
    col = columns[category]
    if col is None:
        continue
    counts = df[col].fillna("Unknown").value_counts().head(12)
    plt.figure(figsize=(9, 5))
    counts.plot(kind="bar")
    plt.title(f"Top {category.replace('_', ' ').title()} Values")
    plt.ylabel("Number of listings")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / f"{category}_counts.png", dpi=150)
    plt.close()

df[["price_category", "rating_category"]].value_counts(dropna=False).to_csv(
    OUTPUT_DIR / "category_counts.csv"
)
print("Saved analysis outputs to", OUTPUT_DIR)
