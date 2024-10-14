import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate transaction data (for scalability and extendability)
def generate_month_data(start_date, num_days, transactions):
    dates = pd.date_range(start=start_date, periods=num_days)
    if len(transactions) != len(dates):
        st.warning("Number of transactions doesn't match the number of dates!")
        return None, None
    return dates, transactions

# Dictionary of data for each month with the simplified structure
data = {
    "May": {
        "start_date": "2024-05-01",
        "num_days": 30,
        "transactions": [1818, 1878, 195, 1305, 180, 166, 2086, 2020, 1909, 217, 
                         1819, 1481, 2037, 2125, 2076, 1947, 275, 1699, 1869, 1811, 
                         1905, 1838, 1716, 134, 1664, 2009, 1729, 1985, 1864, 1935]
    },
    "June": {
        "start_date": "2024-06-01",
        "num_days": 30,
        "transactions": [1683, 2134, 1958, 1916, 1541, 1757, 1753, 1808, 1929, 2020, 
                         1863, 1733, 61, 49, 36, 49, 65, 90, 148, 129, 1507, 1823, 
                         1831, 1960, 1994, 1981, 1593, 330]
    },
    # Add other months similarly...
}

# Set up the sidebar to select a month
selected_month = st.sidebar.selectbox("Select Month", list(data.keys()))

# Get the data for the selected month
month_data = data[selected_month]
dates, transactions = generate_month_data(
    month_data["start_date"], month_data["num_days"], month_data["transactions"]
)

# Plot the data if available
if dates is not None and transactions is not None:
    # Create the plot
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

    # Display some statistics
    st.write(f"**Total Transactions in {selected_month}**: {sum(transactions)}")
    st.write(f"**Average Transactions per Day**: {sum(transactions) / len(transactions):.2f}")
else:
    st.error("No data available for the selected month.")
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Function to generate transaction data (for scalability and extendability)
def generate_month_data(start_date, num_days, transactions):
    dates = pd.date_range(start=start_date, periods=num_days)
    if len(transactions) != len(dates):
        st.warning("Number of transactions doesn't match the number of dates!")
        return None, None
    return dates, transactions

# Dictionary of data for each month with the simplified structure
data = {
    "May": {
        "start_date": "2024-05-01",
        "num_days": 30,
        "transactions": [1818, 1878, 195, 1305, 180, 166, 2086, 2020, 1909, 217, 
                         1819, 1481, 2037, 2125, 2076, 1947, 275, 1699, 1869, 1811, 
                         1905, 1838, 1716, 134, 1664, 2009, 1729, 1985, 1864, 1935]
    },
    "June": {
        "start_date": "2024-06-01",
        "num_days": 30,
        "transactions": [1683, 2134, 1958, 1916, 1541, 1757, 1753, 1808, 1929, 2020, 
                         1863, 1733, 61, 49, 36, 49, 65, 90, 148, 129, 1507, 1823, 
                         1831, 1960, 1994, 1981, 1593, 330]
    },
    # Add other months similarly...
}

# Set up the sidebar to select a month
selected_month = st.sidebar.selectbox("Select Month", list(data.keys()))

# Get the data for the selected month
month_data = data[selected_month]
dates, transactions = generate_month_data(
    month_data["start_date"], month_data["num_days"], month_data["transactions"]
)

# Plot the data if available
if dates is not None and transactions is not None:
    # Create the plot
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

    # Display some statistics
    st.write(f"**Total Transactions in {selected_month}**: {sum(transactions)}")
    st.write(f"**Average Transactions per Day**: {sum(transactions) / len(transactions):.2f}")
else:
    st.error("No data available for the selected month.")
