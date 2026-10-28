# Hotel Booking Data Analysis

**Portfolio owner: Tousif Anam**

A Python exploratory data analysis project examining hotel listing prices, ratings, room types, locations, bed types, and customer reviews.

## Project summary
The supplied academic report describes a dataset of **3,465 rows and 9 columns** from [Kaggle: Hotel Dataset — Rates, Reviews and Amenities](https://www.kaggle.com/datasets/joyshil0599/hotel-dataset-rates-reviews-and-amenities5k).

The analysis includes missing-value checks, duplicate handling, numeric conversion, price/rating categories, descriptive statistics and visualizations. The report describes **a weak association between hotel price and rating**; this finding has not been independently reproduced here.

## Technology
Python · pandas · NumPy · Matplotlib · exploratory data analysis · data cleaning

## Repository structure
- `analysis.py` — **adapted analysis script** based on the report, not the original submitted notebook
- `requirements.txt` — Python dependencies
- `docs/report_summary.md` — portfolio summary of the academic report
- `data/` — add the CSV dataset locally (not included in this repository)

## Run locally
1. Download the dataset from the linked Kaggle page and check the terms of use.
2. Save its CSV file as `data/hotels.csv`.
3. Install dependencies: `pip install -r requirements.txt`.
4. Inspect column names and, if needed, update the column mapping in `analysis.py`.
5. Run: `python analysis.py`.

Outputs are written under `outputs/`. No figures or results have yet been regenerated or validated from this script.

## Analytical questions
- How do room prices vary between room types and locations?
- Is room price related to customer rating?
- Which locations and room types appear most often?
- How are ratings and review counts distributed?

## Limitations
- This is a **descriptive data analytics project**, not a trained prediction model.
- Outliers and currency formats may affect calculated prices.
- Missing values should not be blindly forward-filled across unrelated hotels; the original report used forward fill, which may introduce inaccuracies.
- The sample may not represent the entire hotel market, and correlation does not imply causation.

## Source and attribution
Based on the submitted academic project report *Hotel Booking Data Analysis*. This portfolio adaptation is presented by Tousif Anam; the original academic group-work context is preserved. The original PDF is not modified.
