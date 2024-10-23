import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
def load_data():
    data = pd.read_csv('retail_sales_data.csv')
    data['Date'] = pd.to_datetime(data['Date'])
    return data

# Main Function
def main():
    st.title("Retail Sales Data Insights Dashboard")

    # Load data
    df = load_data()

    # Display the dataset
    st.write("Dataset:")
    st.dataframe(df)

    # Filter by date range
    st.sidebar.header("Filter Options")
    start_date = st.sidebar.date_input("Start Date", df['Date'].min())
    end_date = st.sidebar.date_input("End Date", df['Date'].max())
    filtered_data = df[(df['Date'] >= pd.to_datetime(start_date)) & (df['Date'] <= pd.to_datetime(end_date))]

    # Filter by category
    category = st.sidebar.selectbox("Select Category", df['Category'].unique())
    filtered_data = filtered_data[filtered_data['Category'] == category]

    # Filter by region
    region = st.sidebar.selectbox("Select Region", df['Region'].unique())
    filtered_data = filtered_data[filtered_data['Region'] == region]

    # Show filtered data
    st.write("Filtered Data:")
    st.dataframe(filtered_data)

    # Aggregated Metrics
    total_sales = filtered_data['Sales'].sum()
    total_quantity = filtered_data['Quantity'].sum()
    avg_discount = filtered_data['Discount'].mean()

    st.write(f"Total Sales: {total_sales}")
    st.write(f"Total Quantity Sold: {total_quantity}")
    st.write(f"Average Discount: {avg_discount}")

    # Visualization: Bar chart for total sales by region
    st.write("Total Sales by Region:")
    sales_by_region = df.groupby('Region')['Sales'].sum()
    st.bar_chart(sales_by_region)

    # Visualization: Pie chart for sales by category
    st.write("Sales Percentage by Category:")
    sales_by_category = df.groupby('Category')['Sales'].sum()
    fig, ax = plt.subplots()
    ax.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%')
    st.pyplot(fig)

# Run the app
if __name__ == "__main__":
    main()