# Task 7 - Basic Sales Summary using SQLite and Python

## Objective
This project demonstrates how to use Python with SQLite to store sales data, execute SQL queries, and visualize revenue using a bar chart.

## Tools Used
- Python
- SQLite
- Pandas
- Matplotlib

## SQL Query

```sql
SELECT
    product,
    SUM(quantity) AS total_quantity,
    SUM(quantity * price) AS revenue
FROM sales
GROUP BY product;
```

## Output
- Created SQLite database
- Inserted sample sales data
- Executed SQL query
- Displayed sales summary
- Generated revenue bar chart