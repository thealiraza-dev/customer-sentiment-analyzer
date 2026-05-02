import pandas as pd
import random

# Realistic review patterns (expanded business-style data)
positive_reviews = [
    "Excellent fuel efficiency for daily use",
    "Very affordable maintenance cost",
    "Smooth driving experience in city",
    "Great value for money",
    "Reliable and economical car",
    "Comfortable for small families",
    "Good resale value in market",
    "Easy to park in crowded areas",
    "Low fuel consumption",
    "Perfect for daily commute"
]

negative_reviews = [
    "Poor build quality and weak body",
    "Engine performance is underpowered",
    "AC is not effective in hot weather",
    "Not suitable for long routes",
    "Suspension feels uncomfortable",
    "Low safety features",
    "Noisy engine at high speed",
    "Cheap interior materials",
    "Brake performance is weak",
    "Not durable for long term use"
]

data = []

cities = ["Karachi", "Lahore", "Islamabad", "Faisalabad", "Multan"]

for i in range(1000):
    sentiment_type = random.choice(["Positive", "Negative", "Positive", "Positive"])  # bias realistic

    if sentiment_type == "Positive":
        review = random.choice(positive_reviews)
    else:
        review = random.choice(negative_reviews)

    city = random.choice(cities)

    data.append([review, sentiment_type, city])

df = pd.DataFrame(data, columns=["Review", "Sentiment", "City"])

df.to_csv("big_customer_reviews.csv", index=False)

print("✅ 1000-row dataset created: big_customer_reviews.csv")
