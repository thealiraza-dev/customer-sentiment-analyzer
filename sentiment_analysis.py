import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("customer_reviews.csv")

# Count sentiments
sentiment_counts = df["Sentiment"].value_counts()

print(sentiment_counts)

# Plot
plt.figure()
sentiment_counts.plot(kind='bar')

plt.title("Customer Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

# Save image
plt.savefig("sentiment_dashboard.png")

plt.show()

print("✅ sentiment_dashboard.png created!")