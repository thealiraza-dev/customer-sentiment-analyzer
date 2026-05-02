import pandas as pd
import random

# Sample reviews
positive_reviews = [
    "Great service", "Excellent experience", "Very satisfied", "Good quality product"
]

negative_reviews = [
    "Bad service", "Very slow response", "Poor quality", "Not satisfied"
]

data = []

for i in range(500):
    if random.random() > 0.3:
        review = random.choice(positive_reviews)
        sentiment = "Positive"
    else:
        review = random.choice(negative_reviews)
        sentiment = "Negative"

    data.append([review, sentiment])

df = pd.DataFrame(data, columns=["Review", "Sentiment"])

df.to_csv("customer_reviews.csv", index=False)

print("✅ customer_reviews.csv created!")