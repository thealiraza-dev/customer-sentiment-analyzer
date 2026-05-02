import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("big_customer_reviews.csv")

st.title("🚗 Suzuki Alto Customer Sentiment Engine")

st.subheader("Dataset Preview")
st.write(df.head())

st.subheader("Sentiment Distribution")
fig, ax = plt.subplots()
df["Sentiment"].value_counts().plot(kind="bar", ax=ax)
st.pyplot(fig)

st.subheader("Key Insights")

st.write("""
- Majority of customers appreciate fuel efficiency and affordability.
- Negative feedback focuses on build quality and engine performance.
- Karachi shows higher negative sentiment due to traffic conditions.
""")