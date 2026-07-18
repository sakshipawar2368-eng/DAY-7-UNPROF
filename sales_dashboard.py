# ==========================
# Sales Dashboard
# ==========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read CSV
sales = pd.read_csv("sales.csv")

print(sales)

months = sales["Month"]
sales_amount = np.array(sales["Sales"])

print("\nTotal Sales =", np.sum(sales_amount))
print("Average Sales =", np.mean(sales_amount))
print("Maximum Sales =", np.max(sales_amount))
print("Minimum Sales =", np.min(sales_amount))

# -------------------------
# Bar Chart
# -------------------------
plt.figure(figsize=(8,5))
plt.bar(months, sales_amount)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# -------------------------
# Line Chart
# -------------------------
plt.figure(figsize=(8,5))
plt.plot(months, sales_amount, marker='o')
plt.title("Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# -------------------------
# Pie Chart
# -------------------------
plt.figure(figsize=(7,7))
plt.pie(
    sales_amount,
    labels=months,
    autopct='%1.1f%%',
    startangle=90
)
plt.title("Sales Distribution")
plt.show()
