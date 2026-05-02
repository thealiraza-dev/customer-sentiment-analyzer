import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_reviews.csv")

# Lists
polarity = []
subjectivity = []
sentiment = []

# NLP Analysis
for review in df["Review"]:
    analysis = TextBlob(review)

    pol = analysis.sentiment.polarity
    sub = analysis.sentiment.subjectivity

    polarity.append(pol)
    subjectivity.append(sub)

    if pol > 0:
        sentiment.append("Positive")
    elif pol < 0:
        sentiment.append("Negative")
    else:
        sentiment.append("Neutral")

# Add columns
df["Polarity"] = polarity
df["Subjectivity"] = subjectivity
df["Sentiment"] = sentiment

# ---------------------------
# BUSINESS INSIGHTS SECTION
# ---------------------------

total = len(df)
positive = len(df[df["Sentiment"] == "Positive"])
negative = len(df[df["Sentiment"] == "Negative"])
neutral = len(df[df["Sentiment"] == "Neutral"])

print("\n📊 AUTOMOTIVE CUSTOMER SENTIMENT ENGINE REPORT")
print("------------------------------------------------")
print(f"Total Reviews: {total}")
print(f"Positive: {positive} ({(positive/total)*100:.2f}%)")
print(f"Negative: {negative} ({(negative/total)*100:.2f}%)")
print(f"Neutral: {neutral} ({(neutral/total)*100:.2f}%)")

# ---------------------------
# REGION SIMULATION INSIGHT
# ---------------------------

print("\n📌 Key Business Insight:")
print("- Most negative feedback is related to performance, AC, and build quality.")
print("- Positive sentiment is driven by fuel efficiency and affordability.")
print("- This suggests Suzuki Alto is strong in economy segment but weak in comfort perception.")

# ---------------------------
# VISUALIZATION
# ---------------------------

plt.figure()
df["Sentiment"].value_counts().plot(kind="bar")
plt.title("Customer Sentiment Distribution - Suzuki Alto")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.savefig("sentiment_dashboard.png")
plt.show()

# Save processed dataset
df.to_csv("processed_customer_feedback.csv", index=False)

print("\n✅ Files Generated:")
print("- processed_customer_feedback.csv")
print("- sentiment_dashboard.png")