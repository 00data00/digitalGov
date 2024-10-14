import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Set up colors for cards
colors = {
    'total': '#FF6F61',
    'average': '#6B5B95',
    'max_day': '#88B04B',
    'min_day': '#F7CAC9'
}

# Load the data from the CSV file in the 'data/' folder
def load_data(file_path):
    return pd.read_csv(file_path)

# Read the data from the CSV file in the 'data/' folder
file_path = Path("data/data.csv")
df = load_data(file_path)

# List of months from the CSV
months = df['Month'].unique()

# Sidebar for selecting a month
selected_month = st.sidebar.selectbox("Select Month", months)

# Filter the data for the selected month
month_data = df[df['Month'] == selected_month]

# Dates and transactions for the selected month
dates = pd.to_datetime(month_data['Date'])
transactions = month_data['Total_Transactions'].fillna(0).astype(int)

# Display metrics as four cards
valid_transactions = transactions[transactions > 0]
total_transactions = valid_transactions.sum()
average_transactions = valid_transactions.mean()
max_transactions = valid_transactions.max()
min_transactions = valid_transactions.min()

# Display the four cards with color
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f"<div style='background-color:{colors['total']}; padding:20px; border-radius:10px;'>"
                f"<h3>Total Transactions</h3><h1>{total_transactions}</h1></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div style='background-color:{colors['average']}; padding:20px; border-radius:10px;'>"
                f"<h3>Average (No Zero Days)</h3><h1>{average_transactions:.2f}</h1></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div style='background-color:{colors['max_day']}; padding:20px; border-radius:10px;'>"
                f"<h3>Max Transactions</h3><h1>{max_transactions}</h1></div>", unsafe_allow_html=True)
with col4:
    st.markdown(f"<div style='background-color:{colors['min_day']}; padding:20px; border-radius:10px;'>"
                f"<h3>Min Transactions</h3><h1>{min_transactions}</h1></div>", unsafe_allow_html=True)

# Plot the data for the selected month (all days)
fig, ax = plt.subplots()
ax.plot(dates, transactions, marker='o', linestyle='-', color='b')
ax.set_title(f"Transactions in {selected_month} 2024")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Transactions")
ax.grid(True)

# Rotate the dates on the x-axis to be vertical
ax.tick_params(axis='x', rotation=90)

# Display the plot
st.pyplot(fig)

# Color the header of the table and display the table of daily transactions
st.markdown(
    """
    <style>
    thead th {
        background-color: #FF6F61;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the table of daily transactions
st.table(month_data[['Date', 'Total_Transactions']])

# Create an expander for each day with detailed transaction information
for _, row in month_data.iterrows():
    day_str = pd.to_datetime(row['Date']).strftime("%-d-%b")
    with st.expander(f"Details for {day_str}"):
        if pd.notna(row['الحجز المسبق']):
            st.write(f"**PreBooking:** {row['PreBooking']}")
            st.write(f"**استعلام محرر:** {row['StatusCheck']}")
            st.write(f"**مسبقة الدفع:** {row['PaidTransactions']}")
            st.write(f"**استعلات معلاتي:** {row['PrepaidTransactions']}")
            st.write(f"**اكتب محررك:** {row['WriteYourDoc']}")
        else:
            st.write(f"No detailed transaction data available for {day_str}.")
