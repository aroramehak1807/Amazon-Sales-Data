import  streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# 1. Page Configuration
st.set_page_config(page_title="Amazon Sales EDA",layout="wide")
st.title("📊 Amazon Sales Data Analytics & EDA Dashboard")
st.write("An intermediate-level Exploratory Analysis on Amazon Product Sales.")
@st.cache_data
def load_data():
    df=pd.read_csv("amazon_data.csv")
    return df
try:
    df=load_data()
except FileNotFoundError:
    st.error("Please place the 'amazon_data.csv' file in the same directory at this script. ")
    st.stop()
st.sidebar.header("Filter & Overview")
total_products=df.shape[0]
avg_rating=round(df["rating"].mean(),2)
st.sidebar.metric("Total Products Analyzed",total_products)
st.sidebar.metric("Average Product Rating",f"{avg_rating} ⭐")
categories=["All"]+list(df["main_category"].unique())
selected_category=st.sidebar.selectbox("Select Product Category",categories)
if selected_category != "All":
    filtered_df=df[df["main_category"]==selected_category]
else:
    filtered_df=df
tab1,tab2,tab3=st.tabs(["📋 Raw Data Summary","📈 Price & Discount Analysis","⭐ Ratings & Reviews"])
with tab1:
    st.subheader("Dataset Preview")
    st.dataframe(filtered_df.head(10))
    st.subheader("Statistical Summary (Numerical Columns)")
    st.write(filtered_df.describe())
with tab2:
    st.subheader("Price Distributions and Trends")
    col1,col2=st.columns(2)
    with col1:
        st.write("#### Discounted Price vs Actual Price")
        fig,ax=plt.subplots(figsize=(8,5))
        sns.lineplot(data=filtered_df,x="actual_price",y="discounted_price",alpha=0.6,ax=ax,color="blue")
        ax.set_title("Actual Price vs Discounted Price")
        ax.set_xlabel("Actual Price(₹)")
        ax.set_ylabel("Discounted Price(₹)")
        st.pyplot(fig)
    with col2:
        st.write("#### Distribution of Discount Percentages")
        fig,ax=plt.subplots(figsize=(8,5))
        sns.histplot(filtered_df["discount_percentage"],bins=20,kde=True,color="orange",ax=ax)
        ax.set_title("Distribution of Discounts")
        ax.set_xlabel("Discount %")
        st.pyplot(fig) 
    st.write("#### Average Discount By Product Category")
    cat_discount=df.groupby("main_category")["discount_percentage"].mean().sort_values(ascending=True).reset_index()
    fig,ax=plt.subplots(figsize=(10,4))
    sns.barplot(data=cat_discount,x="discount_percentage",hue="main_category",palette="viridis",ax=ax)
    ax.set_xlabel("Average Discount (%)")
    ax.set_ylabel("Category")
    st.pyplot(fig)
with tab3:
    st.subheader("Customer Ratings Analysis")
    col3,col4=st.columns(2)
    with col3:
        st.write("#### Distribution of Product Ratings")    
        fig,ax=plt.subplots(figsize=(8,5))
        sns.histplot(filtered_df["rating"],bins=15,kde=False,color="green",ax=ax)
        ax.set_title("How Users Rate Products")
        ax.set_xlabel("Rating (Out of 5)")
        st.pyplot(fig) 
    with col4:
        st.write("#### Ratings vs Number of Ratings (Popularity)")    
        fig,ax=plt.subplots(figsize=(8,5))
        sns.scatterplot(data=filtered_df,x="rating",y="rating_count",alpha=0.5,color="purple",ax=ax)
        ax.set_title("Rating vs Rating Count")
        ax.set_xlabel("Rating")
        ax.set_ylabel("Number of Ratings")
        st.pyplot(fig) 
    st.write("#### Top 5 Highest Rated Products in Selected Category")
    top_products=filtered_df.sort_values(by=["rating","rating_count"],ascending=False)[["product_name","rating","actual_price","discounted_price"]].head()
    st.table(top_products)
