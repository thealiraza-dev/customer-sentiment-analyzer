import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("customer_reviews.csv")

# Lists to store results
polarity_scores = []
sentiment_labels = []

# Analyze sentiment using TextBlob
for review in df["Review"]:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    polarity_scores.append(polarity)

    if polarity >= 0:
        sentiment_labels.append("Positive")
    else:
        sentiment_labels.append("Negative")

# Add results to dataframe
df["Polarity"] = polarity_scores
df["Predicted_Sentiment"] = sentiment_labels

# Summary
positive_count = sentiment_labels.count("Positive")
negative_count = sentiment_labels.count("Negative")
total = len(sentiment_labels)

print("\n📊 Suzuki Alto Sentiment Analysis Report")
print("----------------------------------------")
print(f"Total Reviews: {total}")
print(f"Positive Reviews: {positive_count} ({(positive_count/total)*100:.2f}%)")
print(f"Negative Reviews: {negative_count} ({(negative_count/total)*100:.2f}%)")

# Visualization
plt.figure()
df["Predicted_Sentiment"].value_counts().plot(kind="bar")

plt.title("Suzuki Alto Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")

plt.savefig("sentiment_dashboard.png")
plt.show()

# Save updated dataset
df.to_csv("analyzed_reviews.csv", index=False)

print("\n✅ Files generated:")
print("- analyzed_reviews.csv")
print("- sentiment_dashboard.png")