import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("population.csv")

# Bar Chart - Gender
plt.figure()
df['gender'].value_counts().plot(kind='bar')
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("gender_distribution.png")
plt.show()

# Histogram - Age
plt.figure()
df['age'].plot(kind='hist', bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_histogram.png")
plt.show()
