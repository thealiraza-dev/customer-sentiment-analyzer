import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Customer Sentiment Engine",
    page_icon="🚗",
    layout="wide"
)

# -------------------------------
# CUSTOM CSS
# -------------------------------
st.markdown("""
    <style>
        .main { background-color: #0E1117; }

        .kpi-card {
            background-color: #1c1f26;
            padding: 20px;
            border-radius: 12px;
            text-align: center;
        }

        .kpi-title { font-size: 16px; color: #9aa0a6; }
        .kpi-value { font-size: 28px; font-weight: bold; color: #ffffff; }

        .section-title {
            font-size: 22px;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD DATA
# -------------------------------
df = pd.read_csv("processed_customer_feedback.csv")

# -------------------------------
# SIDEBAR FILTERS
# -------------------------------
st.sidebar.title("🔍 Filters")

city_filter = st.sidebar.multiselect(
    "Select City",
    df["City"].unique(),
    default=df["City"].unique()
)

sentiment_filter = st.sidebar.multiselect(
    "Select Sentiment",
    df["Sentiment"].unique(),
    default=df["Sentiment"].unique()
)

filtered_df = df[
    (df["City"].isin(city_filter)) &
    (df["Sentiment"].isin(sentiment_filter))
]

# -------------------------------
# HEADER
# -------------------------------
st.title("🚗 Suzuki Alto Customer Sentiment Engine")
st.caption("AI-powered customer insights dashboard for business decision-making")

# -------------------------------
# EMPTY CHECK
# -------------------------------
if filtered_df.empty:
    st.warning("⚠️ No data available for selected filters.")
    st.stop()

# -------------------------------
# KPI CARDS
# -------------------------------
total = len(filtered_df)
pos = len(filtered_df[filtered_df["Sentiment"] == "Positive"])
neg = len(filtered_df[filtered_df["Sentiment"] == "Negative"])
neu = len(filtered_df[filtered_df["Sentiment"] == "Neutral"])

positive_rate = round((pos / total) * 100, 1)
negative_rate = round((neg / total) * 100, 1)

col1, col2, col3, col4 = st.columns(4)

def kpi(title, value):
    st.markdown(f"""
        <div class="kpi-card">
            <div class="kpi-title">{title}</div>
            <div class="kpi-value">{value}</div>
        </div>
    """, unsafe_allow_html=True)

with col1:
    kpi("Total Reviews", total)

with col2:
    kpi("Positive %", f"{positive_rate}%")

with col3:
    kpi("Negative %", f"{negative_rate}%")

with col4:
    kpi("Neutral Count", neu)

# -------------------------------
# SEARCH FEATURE 🔎
# -------------------------------
st.markdown('<div class="section-title">🔎 Search Reviews</div>', unsafe_allow_html=True)

search_query = st.text_input("Search keywords in reviews")

if search_query:
    search_results = filtered_df[
        filtered_df["Review"].str.contains(search_query, case=False)
    ]
    st.write(f"Results found: {len(search_results)}")
    st.dataframe(search_results, use_container_width=True)

# -------------------------------
# DATA PREVIEW
# -------------------------------
st.markdown('<div class="section-title">📊 Dataset Preview</div>', unsafe_allow_html=True)
st.dataframe(filtered_df.head(), use_container_width=True)

# -------------------------------
# CHARTS
# -------------------------------
col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-title">Sentiment Distribution</div>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    filtered_df["Sentiment"].value_counts().plot(kind="bar", ax=ax)
    st.pyplot(fig)

with col2:
    st.markdown('<div class="section-title">Sentiment Share</div>', unsafe_allow_html=True)
    fig2, ax2 = plt.subplots()
    filtered_df["Sentiment"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        ax=ax2
    )
    ax2.set_ylabel("")
    st.pyplot(fig2)

# -------------------------------
# CITY ANALYSIS
# -------------------------------
st.markdown('<div class="section-title">🌍 City-wise Sentiment Analysis</div>', unsafe_allow_html=True)

city_sentiment = pd.crosstab(filtered_df["City"], filtered_df["Sentiment"])

fig3, ax3 = plt.subplots()
city_sentiment.plot(kind="bar", stacked=True, ax=ax3)
st.pyplot(fig3)

# -------------------------------
# BUSINESS INTELLIGENCE
# -------------------------------
st.markdown('<div class="section-title">🧠 Business Intelligence Insights</div>', unsafe_allow_html=True)

city_neg_ratio = (
    filtered_df.groupby("City")["Sentiment"]
    .apply(lambda x: (x == "Negative").sum() / len(x))
)

city_pos_ratio = (
    filtered_df.groupby("City")["Sentiment"]
    .apply(lambda x: (x == "Positive").sum() / len(x))
)

worst_city = city_neg_ratio.idxmax()
best_city = city_pos_ratio.idxmax()

st.error(f"🚨 Problem Area: {worst_city}")
st.success(f"🌟 Strong Market: {best_city}")

# -------------------------------
# DOWNLOAD FEATURE 📥
# -------------------------------
st.markdown('<div class="section-title">📥 Download Data</div>', unsafe_allow_html=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Data",
    data=csv,
    file_name="filtered_reviews.csv",
    mime="text/csv"
)

# -------------------------------
# RAW DATA TOGGLE
# -------------------------------
st.markdown('<div class="section-title">🧾 Raw Data</div>', unsafe_allow_html=True)

if st.checkbox("Show Full Dataset"):
    st.dataframe(filtered_df, use_container_width=True)

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.caption("Built by Ali Raza | Data Analyst Portfolio Project")