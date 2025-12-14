# ==== IMPORT LIBRARIES ====
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==== LOAD DATA ====
df = pd.read_csv("population_sample.csv")

# Show first few rows
df.head()

# ==== BAR CHART: Distribution of Genders ====
plt.figure(figsize=(8,5))
sns.countplot(x="Gender", data=df, palette="Set2")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("gender_bar_chart.png")
plt.show()

# ==== HISTOGRAM: Distribution of Ages ====
plt.figure(figsize=(8,5))
plt.hist(df["Age"], bins=10, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_histogram.png")
plt.show()
