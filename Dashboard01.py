import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Dictionary containing transaction data for each month
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

    "July": {
        "start_date": "2024-07-01",
        "num_days": 31,
        "transactions": [2344, 2185, 2185, 2149, 192, 663, 2029, 1708, 2192, 2296, 
                         0, 0, 1889, 2279, 984, 1964, 2256, 2142, 242, 1936, 0, 2171, 
                         2029, 2209, 0, 0, 1947, 2148, 2099, 2136, 0]
    },
    "August": {
        "start_date": "2024-08-01",
        "num_days": 31,
        "transactions": [2066, 0, 1838, 2002, 2094, 1933, 1964, 2114, 0, 1705, 
                         2067, 2193, 2070, 1950, 1992, 0, 1853, 1998, 2050, 1934, 
                         1950, 1969, 0, 1831, 2079, 1911, 1870, 1958, 2090, 1743, 0]
    },
    "September": {
        "start_date": "2024-09-01",
        "num_days": 30,
        "transactions": [1487, 1730, 1985, 1774, 2131, 0, 1955, 1936, 1894, 1692, 
                         1856, 0, 0, 1632, 0, 2244, 2100, 1961, 2069, 0, 1746, 
                         1860, 1923, 1917, 1841, 0, 1763, 1849, 1907, 0]
    },
    "October": {
        "start_date": "2024-10-01",
        "num_days": 31,
        "transactions": [1813, 1826, 0, 0, 609, 0, 2234, 2118, 0, 1912, 0, 1778, 
                         2055, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    }
    # Add other months similarly...
}

# Transaction breakdown for a specific day (example: June 1)
transaction_details = {
    "1-Jun": {
        "نوع المعاملة": ["حجز مسبق", "استعلام سريان محرر", "معاملاتى المدفوعة", 
                         "معاملات مسبوقة الدفع", "معاملات اكتب محررك"],
        "عدد المعاملات": [356, 37, 5, 85, 1200],
        "المجموع": 1683
    },
    # Add other days' transaction details similarly...
}

# Function to generate transaction data (for scalability and extendability)
def generate_month_data(start_date, num_days, transactions):
    dates = pd.date_range(start=start_date, periods=num_days)
    if len(transactions) != len(dates):
        st.warning("Number of transactions doesn't match the number of dates!")
        return None, None
    return dates, transactions

# Set up the sidebar to select a month
selected_month = st.sidebar.selectbox("Select Month", list(data.keys()))

# Get the data for the selected month
month_data = data[selected_month]
dates, transactions = generate_month_data(
    month_data["start_date"], month_data["num_days"], month_data["transactions"]
)

# Plot the data if available
if dates is not None and transactions is not None:
    # Create the plot for the selected month
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

    # Show statistics, excluding 0s from the average calculation
    valid_transactions = [t for t in transactions if t > 0]
    if valid_transactions:
        st.write(f"**Total Transactions in {selected_month}**: {sum(valid_transactions)}")
        st.write(f"**Average Transactions per Day** (excluding zero days): {sum(valid_transactions) / len(valid_transactions):.2f}")
    
    # Display a table for the month
    table_data = pd.DataFrame({"Date": dates, "Transactions": transactions})
    st.table(table_data)

    # Create an expander for each day
    for i, day in enumerate(dates):
        day_str = day.strftime("%-d-%b")
        with st.expander(f"Details for {day_str}"):
            if day_str in transaction_details:
                day_detail = transaction_details[day_str]
                day_table = pd.DataFrame({
                    "نوع المعاملة": day_detail["نوع المعاملة"],
                    "عدد المعاملات": day_detail["عدد المعاملات"]
                })
                st.table(day_table)
                st.write(f"**Total Transactions on {day_str}:** {day_detail['المجموع']}")
            else:
                st.write(f"No detailed transaction data available for {day_str}.")
else:
    st.error("No data available for the selected month.")

# Plot all months together
all_dates = []
all_transactions = []

for month in data.values():
    month_dates, month_transactions = generate_month_data(month["start_date"], month["num_days"], month["transactions"])
    if month_dates is not None:
        all_dates.extend(month_dates)
        all_transactions.extend(month_transactions)

# Create a complete graph of all months together
if all_dates and all_transactions:
    fig, ax = plt.subplots()
    ax.plot(all_dates, all_transactions, marker='o', linestyle='-', color='g')
    ax.set_title("Complete Transaction Overview (May to October 2024)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Transactions")
    ax.grid(True)
    ax.tick_params(axis='x', rotation=90)

    st.pyplot(fig)
