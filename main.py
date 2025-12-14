import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv")

# Count countries per income group
income_counts = df['IncomeGroup'].value_counts().dropna()

# Convert to DataFrame (table used for histogram)
hist_data = income_counts.reset_index()
hist_data.columns = ['Income Group', 'Number of Countries']

# Save data table
hist_data.to_csv("histogram_data.csv", index=False)

# Create histogram
plt.hist(hist_data['Number of Countries'], bins=5)
plt.xlabel("Number of Countries")
plt.ylabel("Frequency")
plt.title("Histogram of Countries by Income Group")
plt.savefig("income_group_histogram.png")
plt.show()
