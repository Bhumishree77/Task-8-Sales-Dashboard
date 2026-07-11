import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect("sales_data.db")

# Create a cursor object
cursor = conn.cursor()

# Create the sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Delete old data if any
cursor.execute("DELETE FROM sales")

# Insert sample sales data
sales_data = [
    ("Laptop", 5, 60000),
    ("Laptop", 3, 60000),
    ("Mouse", 15, 500),
    ("Keyboard", 8, 1500),
    ("Mouse", 10, 500),
    ("Monitor", 4, 12000),
    ("Keyboard", 6, 1500)
]

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", sales_data)

# Save data
conn.commit()

# SQL Query
query = """
SELECT
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product
"""

# Read SQL result into a DataFrame
df = pd.read_sql_query(query, conn)

# Display the result
print("Sales Summary")
print(df)

# Create Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["product"], df["revenue"])
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

# Save the chart
plt.savefig("sales_chart.png")

# Show the chart
plt.show()

# Close database connection
conn.close()