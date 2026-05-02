import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("big_customer_reviews.csv")

# Sentiment distribution
sentiment_counts = df["Sentiment"].value_counts()

# City-wise sentiment (business insight)
city_sentiment = df.groupby("City")["Sentiment"].value_counts().unstack().fillna(0)

# -----------------------
# 1. SENTIMENT PIE CHART
# -----------------------
plt.figure()
sentiment_counts.plot(kind="pie", autopct="%1.1f%%")
plt.title("Overall Customer Sentiment - Suzuki Alto")
plt.ylabel("")
plt.savefig("sentiment_pie.png")
plt.show()

# -----------------------
# 2. BAR CHART
# -----------------------
plt.figure()
sentiment_counts.plot(kind="bar")
plt.title("Sentiment Distribution")
plt.xlabel("Sentiment")
plt.ylabel("Count")
plt.savefig("sentiment_bar.png")
plt.show()

# -----------------------
# 3. CITY INSIGHT CHART
# -----------------------
plt.figure()
city_sentiment.plot(kind="bar", stacked=True)
plt.title("City-wise Sentiment Analysis")
plt.xlabel("City")
plt.ylabel("Count")
plt.savefig("city_sentiment.png")
plt.show()

print("✅ Dashboard generated successfully")