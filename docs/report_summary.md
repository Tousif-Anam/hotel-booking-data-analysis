# Hotel Booking Data Analysis — Portfolio Report Summary

**Name: Tousif Anam**

*Adapted from the uploaded academic group-project report. It does not replace or change the original PDF or attribution.*

## Dataset and goal
The academic report describes **3,465 records, 9 fields** in a Kaggle hotel listing dataset. The goal was to explore price, customer rating, location, room type, bed type, and reviews. No prediction target or trained machine learning model was defined.

## Data preparation
The report describes:
- Checking missing and duplicate entries
- Removing duplicates
- Trimming column names
- Converting ratings and prices to numeric values
- Forward-filling missing entries
- Creating price and rating categories

**Methodological note:** Forward fill across independent hotel rows may introduce incorrect values. The adapted `analysis.py` keeps missingness visible instead.

## Analyses and charts
The report describes bar charts of locations and ratings, bed-type distributions, a price/rating correlation heatmap, review score histograms, and outlier analysis using IQR.

## Reported observations (not independently reproduced)
- Prices span a wide range with some high-priced outliers.
- Ratings are relatively concentrated.
- Price and rating show a weak relationship; higher price does not reliably indicate higher customer rating.
- Listings and reviews are unevenly distributed across locations and hotels.

## Limitations
Sample bias, data quality issues, potential price outliers, missing amenities/service-quality features, and the distinction between association and causation.

## Reproduction status
`analysis.py` was written as an **adapted implementation** of methods in the report. The original source CSV and original executable notebook have not been uploaded. Reported figures and conclusions should be rerun on the source data before being represented as independently verified.
