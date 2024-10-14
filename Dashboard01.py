import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Create a dictionary of data for each month
data = {
    "May": {
        "dates": pd.date_range(start="2024-05-01", end="2024-05-30"),
        "transactions": [1818, 1878, 195, 1305, 180, 166, 2086, 2020, 1909, 217, 1819, 1481, 2037, 2125, 2076, 1947, 275, 1699, 1869, 1811, 1905, 1838, 1716, 134, 1664, 2009, 1729, 1985, 1864, 1935]
    },
    "June": {
        "dates": pd.date_range(start="2024-06-01", end="2024-06-30"),
        "transactions": [1683, 2134, 1958, 1916, 1541, 1757, 1753, 1808, 1929, 2020, 1863, 1733, 61, 49, 36, 49, 65, 90, 148, 129, 1507, 1823, 1831, 1960, 1994, 1981, 1593, 330]
    },
    # Add other months similarly...
}

# Set up the sidebar to select a month
selected_month = st.sidebar.selectbox("Select Month", list(data.keys()))

# Get the data for the selected month
month_data = data[selected_month]
dates = month_data["dates"]
transactions = month_data["transactions"]

# Create the plot
fig, ax = plt.subplots()
ax.plot(dates, transactions, marker='o', linestyle='-', color='b')
ax.set_title(f"Transactions in {selected_month} 2024")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Transactions")
ax.grid(True)

# Display the plot
st.pyplot(fig)
